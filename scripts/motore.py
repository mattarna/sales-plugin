#!/usr/bin/env python3
"""Il motore: fotografa un'azienda, mappa il materiale sui nodi, e chiede il resto.

Gira a casa di chi installa il plugin, e la cartella che lo ospita era riservata a
questo dal piano 01-01. Il README accanto dice cosa non puo starci: nessun percorso
assoluto, nessun riferimento fuori dalla cartella del plugin, e mai un controllore
di progetto. Questo file legge la cartella `catalog` che gli sta accanto dentro
il plugin, e il file delle risposte, che gli viene passato invece di essere
cercato.

La divisione che regge tutto. Il motore fa la meta deterministica e si ferma dove
comincia il giudizio:

    quali campi sono risposti, vuoti, assenti          motore
    la propagazione di `non serve ancora`              motore
    quali domande fare, e a chi non farle              motore
    i riferimenti ai criteri, con la loro impronta     motore
    se `tre ruoli distinti` sono davvero tre           il modello che legge

Il manifest che esce e vero ma grossolano. Un modello che lo rilegge puo solo
renderlo piu fine, e ogni raffinamento deve ripassare le stesse dieci reti del
validatore. Il motore non inventa mai un verdetto: dove il criterio chiede un
giudizio, lo stato resta quello che i campi permettono di dire e il criterio
citato e quello che il giudizio dovra guardare.

La regola dello stato, in quest'ordine e non in un altro:

    nessun campo risposto e almeno un nodo da cui dipende e vuoto  non_serve_ancora
    nessun campo risposto                                          mancante
    qualche campo risposto o dichiarato assente                     parziale
    tutti i campi risposti e nessuno vuoto                          pieno

La propagazione viene prima, ed e la regola scelta il 2026-08-10 al posto di una
tassonomia di stadi aziendali che nessuno aveva mai definito. Un nodo senza
dipendenze non puo mai essere `non serve ancora`, e le nove radici del catalogo lo
dimostrano da sole senza nessun elenco di eccezioni.

Un campo assente e diverso da un campo vuoto. Assente vuol dire `non chiesto`;
vuoto vuol dire `chiesto, e l'azienda non ce l'ha`. Senza la distinzione il motore
richiederebbe per sempre le cose che l'azienda non ha, ed e meta di MOT-05.

Uso:
    python motore.py --risposte percorso              stampa il manifest
    python motore.py --risposte percorso --domande    stampa le domande da fare
    python motore.py --risposte percorso --precedente percorso   il giro dopo
    python motore.py --risposte percorso --catalogo percorso su una copia del catalogo

Uscite:
    0  fatto
    1  errore d'uso, risposte o catalogo illeggibili

Python 3.12, sola libreria standard piu PyYAML.
"""

import hashlib
import sys
from pathlib import Path

import yaml

# L'uscita si forza a UTF-8. Senza, su una macchina con la codepage locale il
# figlio scrive byte che il genitore non sa decodificare, la lettura muore in
# SILENZIO e l'uscita arriva vuota con codice 0: un'uscita che sparisce senza
# rumore e indistinguibile da un `niente da dire`. Trovato il 2026-08-11 da un
# banco che ha concluso `il giro 1 non fa domande` mentre ne faceva 22.
for _flusso in (sys.stdout, sys.stderr):
    if hasattr(_flusso, "reconfigure"):
        _flusso.reconfigure(encoding="utf-8", errors="replace")

RADICE_PLUGIN = Path(__file__).resolve().parent.parent
CATALOGO_PREDEFINITO = RADICE_PLUGIN / "catalog"

# Le cifre dell'impronta. Sono le stesse che il contratto del manifest dichiara, e
# qui sono scritte perche questo file non puo leggere il ramo privato: sta dentro
# il plugin e a casa dell'utente quel ramo non esiste. E l'unica cosa duplicata,
# ed e un numero: il validatore la rileggerebbe dal contratto e le due si
# confrontano al primo manifest che il banco fa passare dalle dieci reti.
CIFRE_IMPRONTA = 8

CLASSI = ("absent_when", "partial_when", "complete_when")

STATO_PIENO = "pieno"
STATO_PARZIALE = "parziale"
STATO_NON_SERVE = "non_serve_ancora"
STATO_MANCANTE = "mancante"
STATI_VUOTI = (STATO_MANCANTE, STATO_NON_SERVE)


class Fermata(Exception):
    """Il motore non puo girare. Uscita 1, mai un manifest a meta."""


def leggi_yaml(percorso, chi):
    if not percorso.is_file():
        raise Fermata("%s non esiste: %s" % (chi, percorso))
    try:
        return yaml.safe_load(percorso.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as errore:
        raise Fermata("%s non e YAML valido: %s" % (chi, errore))


def impronta(testo):
    """L'impronta di un criterio, sul testo con gli spazi normalizzati."""
    piatto = " ".join(str(testo).split())
    return hashlib.sha256(piatto.encode("utf-8")).hexdigest()[:CIFRE_IMPRONTA]


def impronta_risposte(risposte_del_nodo):
    """L'impronta delle risposte di un nodo, per sapere se sono cambiate.

    Si ordina per chiave prima di impastare, cosi due file che dicono la stessa
    cosa in ordine diverso danno la stessa impronta: l'ordine di un dizionario non
    e una risposta dell'azienda.

    Un nodo senza risposte ha comunque la sua impronta, quella del vuoto, e non e
    un dettaglio: al giro dopo dice `non hai ancora risposto, e non hai risposto
    nemmeno adesso`, che e diverso da `non lo so`.
    """
    pezzi = []
    for chiave in sorted((risposte_del_nodo or {}).keys()):
        pezzi.append("%s=%s" % (chiave, risposte_del_nodo[chiave]))
    piatto = chr(10).join(pezzi)
    return hashlib.sha256(piatto.encode("utf-8")).hexdigest()[:CIFRE_IMPRONTA]


def carica(catalogo):
    nodi = leggi_yaml(catalogo / "NODI.yaml", "il file dei nodi")
    rubriche = leggi_yaml(catalogo / "RUBRICHE.yaml", "il file delle rubriche")
    domande = leggi_yaml(catalogo / "DOMANDE.yaml", "il file delle domande")
    if not nodi:
        raise Fermata("il file dei nodi e vuoto")
    return nodi, rubriche, domande


def e_vuoto(valore):
    """Vero se il campo non porta niente, in QUALUNQUE forma in cui si scriva niente.

    PERCHE NON BASTA CONFRONTARE CON LA STRINGA VUOTA, ed e un difetto vero trovato
    l'11 agosto 2026 mentre si preparava la prima azienda. La riga di prima diceva
    `str(valore).strip() == ""`, e su un campo scritto `null` calcolava
    `str(None)`, cioe la stringa `None`, che vuota non e: **il campo passava per
    risposto e il nodo usciva `pieno`**.

    Perche era grave e non pignolo. `null` e esattamente cio che scrive chiunque
    voglia dire "non ce l'ho", ed e cio che produce qualunque strumento che
    serializzi un valore mancante. Un'azienda senza principi di vendita sarebbe
    stata dichiarata COMPLETA su quel nodo, la propagazione avrebbe sbloccato i
    nodi a valle, e ogni artefatto costruito sopra sarebbe nato da un presupposto
    falso. Un verde su un buco e peggio di un rosso: nessuno lo va a guardare.

    Perche le forme sono quattro e non una. YAML scrive `niente` in piu modi e
    nessuno di questi e piu legittimo degli altri: la chiave senza valore e `~` e
    `null` arrivano tutti come `None`, la stringa vuota come `""`, e una lista o
    una mappa vuote sono il modo naturale di dire "nessuna voce" su un campo che
    ne ammette molte. Coprirne una sola avrebbe lasciato aperte le altre tre.

    CIO CHE NON E VUOTO, ED E LA META CHE CONTA. Lo **zero** e una risposta vera:
    `organico_attuale: 0` vuol dire che non c'e nessuno in quel ruolo, e non che la
    domanda non e stata fatta. Lo stesso vale per `false`. Un controllo scritto con
    la falsita di Python li avrebbe ingoiati tutti e due, trasformando la
    correzione di un difetto nella nascita di un altro, piu difficile da vedere
    perche colpisce solo le aziende che rispondono zero.
    """
    if valore is None:
        return True
    if isinstance(valore, (str, bytes)):
        return not valore.strip()
    if isinstance(valore, (list, tuple, set, dict)):
        return len(valore) == 0
    return False


def stato_dei_campi(nodo, risposte_del_nodo):
    """(risposti, vuoti, assenti) fra i campi che il nodo dichiara."""
    campi = [str(c) for c in (nodo.get("campi") or [])]
    risposti, vuoti, assenti = [], [], []
    for c in campi:
        if c not in risposte_del_nodo:
            assenti.append(c)
        elif e_vuoto(risposte_del_nodo[c]):
            vuoti.append(c)
        else:
            risposti.append(c)
    return risposti, vuoti, assenti


def primo_giro(nodi, risposte):
    """{codice: (stato provvisorio, risposti, vuoti, assenti)}, senza propagazione.

    Provvisorio perche `non serve ancora` si puo decidere solo dopo aver guardato
    tutti gli altri nodi: un nodo dipende da un altro, e finche non si sa se
    quell'altro e vuoto non si sa nemmeno che cosa dire di questo.
    """
    fuori = {}
    for codice, nodo in nodi.items():
        risposti, vuoti, assenti = stato_dei_campi(nodo, risposte.get(codice) or {})
        if not risposti and not vuoti:
            stato = STATO_MANCANTE
        elif assenti or vuoti:
            stato = STATO_PARZIALE
        else:
            stato = STATO_PIENO
        fuori[codice] = (stato, risposti, vuoti, assenti)
    return fuori


def propaga(nodi, provvisori):
    """{codice: (stato, ..., ragioni)}. Un `mancante` che dipende da un vuoto non serve ancora.

    La propagazione e a un solo passo, ed e una scelta dichiarata. Un nodo diventa
    `non serve ancora` se un nodo da cui dipende e vuoto nel primo giro, non nel
    risultato della propagazione stessa. A piu passi la catena si allungherebbe
    finche tutto il catalogo diventa `non serve ancora` per colpa di una radice
    sola, e un manifest che non dichiara niente non e prudente: e vuoto.
    """
    fuori = {}
    for codice, (stato, risposti, vuoti, assenti) in provvisori.items():
        ragioni = []
        if stato == STATO_MANCANTE:
            for altro in (nodi[codice].get("depends_on") or []):
                altro = str(altro)
                if altro in provvisori and provvisori[altro][0] in STATI_VUOTI:
                    ragioni.append(altro)
            if ragioni:
                stato = STATO_NON_SERVE
        fuori[codice] = (stato, risposti, vuoti, assenti, ragioni)
    return fuori


def motivi(codice, stato, rubriche, risposti, vuoti, assenti):
    """I criteri non soddisfatti, con la loro impronta. Mai un verdetto senza.

    Il motore non giudica il testo del criterio: sceglie la classe giusta per lo
    stato che i campi permettono di dire, e cita i criteri di quella classe. Se
    `tre ruoli distinti` siano davvero tre lo dira chi legge, e citera lo stesso
    criterio perche il riferimento e gia scritto qui.
    """
    if stato == STATO_PIENO:
        return []
    classe = "absent_when" if stato in STATI_VUOTI else "partial_when"
    elenco = (rubriche.get(codice) or {}).get(classe) or []
    if not elenco:
        # Una classe vuota non puo produrre un verdetto muto: si ripiega sulla
        # classe che il nodo porta, perche uno stato senza motivo e un voto a
        # naso, e il validatore lo rifiuta con la rete M4.
        for altra in CLASSI:
            elenco = (rubriche.get(codice) or {}).get(altra) or []
            if elenco:
                classe = altra
                break
    if not elenco:
        return []
    return [{"classe": classe, "indice": 0, "impronta": impronta(elenco[0])}]


def trust_di(nodo, risposti):
    """Da dove viene cio che il nodo porta."""
    strato = str(nodo.get("strato") or "")
    if strato == "istanza":
        return "istanza"
    return "misto" if risposti else "dottrina"


def domande_da_fare(nodi, domande, stati):
    """[(codice, chiave, domanda)] per cio che manca davvero.

    Non si chiede cio che si sa gia, ed e MOT-01. Non si chiede nemmeno a chi non
    serve ancora: una domanda su un nodo che non e il suo momento e la forma piu
    educata di far perdere tempo.
    """
    fuori = []
    for codice in sorted(nodi):
        stato, risposti, vuoti, assenti, _ragioni = stati[codice]
        if stato in (STATO_PIENO, STATO_NON_SERVE):
            continue
        for voce in (domande.get(codice) or []):
            if not isinstance(voce, dict):
                continue
            chiave = str(voce.get("chiave") or "")
            if chiave not in assenti:
                continue
            quando = str(voce.get("quando") or "")
            if stato == STATO_MANCANTE and "assente" not in quando:
                continue
            fuori.append((codice, chiave, str(voce.get("domanda") or "")))
    return fuori


def costruisci_manifest(azienda, nodi, rubriche, stati, giro, data, risposte,
                        precedente=None):
    """Le voci del manifest, tenendo quelle che il giro prima ha gia deciso.

    Cio che il manifest sa e le risposte no e il GIUDIZIO: il motore produce uno
    stato grossolano, e un modello che rilegge puo raffinarlo. Ricalcolando da
    zero, il giro dopo lo butterebbe via e richiederebbe una cosa gia risolta.

    Si tiene una voce quando l'impronta delle sue risposte non e cambiata. Si
    ricalcola quando e cambiata, e quando il nodo nel manifest vecchio non c'era:
    quello e il nodo nato dopo, e non ha un giudizio da conservare.
    """
    vecchie = {}
    if precedente:
        for v in (precedente.get("nodi") or []):
            if isinstance(v, dict) and v.get("codice"):
                vecchie[str(v["codice"])] = v
    voci, tenuti, ricalcolati = [], [], []
    for codice in sorted(nodi):
        stato, risposti, vuoti, assenti, ragioni = stati[codice]
        impronta = impronta_risposte(risposte.get(codice) or {})
        vecchia = vecchie.get(codice)
        if vecchia is not None and str(vecchia.get("impronta_risposte") or "") == impronta:
            voce = dict(vecchia)
            voce["impronta_risposte"] = impronta
            voci.append(voce)
            tenuti.append(codice)
            continue
        ricalcolati.append(codice)
        voci.append({
            "codice": codice,
            "stato": stato,
            "motivo": motivi(codice, stato, rubriche, risposti, vuoti, assenti),
            "trust": trust_di(nodi[codice], risposti),
            "campi_vuoti": sorted(vuoti + assenti),
            "non_serve_perche": ragioni,
            "impronta_risposte": impronta,
        })
    costruisci_manifest.ultimo = (tenuti, ricalcolati)
    stato_finale = {v["codice"]: v["stato"] for v in voci}
    buchi = {"di_prodotto": [], "di_istanza": []}
    for codice in sorted(nodi):
        stato = stato_finale.get(codice, stati[codice][0])
        if stato in (STATO_PIENO, STATO_NON_SERVE):
            continue
        strato = str(nodi[codice].get("strato") or "")
        if strato == "istanza":
            buchi["di_istanza"].append(codice)
        else:
            buchi["di_prodotto"].append(codice)
    return {
        "versione_del_manifest": "1.0",
        "azienda": azienda,
        "data_della_corsa": data,
        "giro": giro,
        "anonimizzazione": {"verificata_il": data, "esito": "non_verificata"},
        "nodi": voci,
        "buchi": buchi,
        "segnaposto_non_risolti": [],
        "artefatti": [],
    }


def corri(risposte_percorso, catalogo, data, precedente_percorso=None):
    dati = leggi_yaml(risposte_percorso, "il file delle risposte")
    azienda = str(dati.get("azienda") or "").strip()
    if not azienda:
        raise Fermata("il file delle risposte non dichiara `azienda`")
    risposte = dati.get("risposte")
    risposte = risposte if isinstance(risposte, dict) else {}
    nodi, rubriche, domande = carica(catalogo)
    stati = propaga(nodi, primo_giro(nodi, risposte))

    precedente, giro = None, 1
    if precedente_percorso is not None:
        precedente = leggi_yaml(precedente_percorso, "il manifest precedente")
        vecchio_giro = precedente.get("giro")
        giro = (vecchio_giro if isinstance(vecchio_giro, int) else 0) + 1

    manifest = costruisci_manifest(azienda, nodi, rubriche, stati, giro, data,
                                   risposte, precedente)
    # Le domande si fanno sullo stato FINALE, non su quello ricalcolato: un nodo
    # tenuto perche gia risolto non si richiede, ed e la meta di MOT-05 che si
    # vede da fuori.
    # SI SOSTITUISCE SOLO LO STATO, e il resto resta quello calcolato adesso.
    # La prima stesura passava `campi_vuoti` al posto degli assenti, e i due non
    # sono la stessa cosa: `campi_vuoti` unisce chi non ha risposto e chi ha
    # risposto che non ce l'ha. Il secondo NON si richiede, ed e la distinzione
    # che lo schema delle risposte dichiara. Il difetto si vedeva da un numero:
    # le domande passavano da 22 a 23 su un'azienda che non era cambiata.
    finale = {}
    for v in manifest["nodi"]:
        codice = v["codice"]
        _s, risposti, vuoti, assenti, ragioni = stati[codice]
        finale[codice] = (v["stato"], risposti, vuoti, assenti, ragioni)
    return manifest, domande_da_fare(nodi, domande, finale), stati


def conta_stati(manifest):
    """La distribuzione degli stati DEL MANIFEST, non di quelli ricalcolati.

    La prima stesura contava gli stati appena calcolati, e al secondo giro
    mentiva: i nodi tenuti portano lo stato del giro prima, quindi il referto
    descriveva un manifest diverso da quello che stava producendo. Un referto che
    non descrive il proprio prodotto e peggio di nessun referto.
    """
    fuori = {}
    for v in manifest["nodi"]:
        fuori[v["stato"]] = fuori.get(v["stato"], 0) + 1
    return fuori


def main(argv):
    if "--help" in argv or "-h" in argv:
        print(__doc__)
        return 0
    if "--risposte" not in argv:
        print(__doc__)
        return 0
    i = argv.index("--risposte")
    if i + 1 >= len(argv):
        print("Uso: --risposte vuole un percorso", file=sys.stderr)
        return 1
    catalogo = CATALOGO_PREDEFINITO
    if "--catalogo" in argv:
        j = argv.index("--catalogo")
        if j + 1 < len(argv):
            catalogo = Path(argv[j + 1]).resolve()
    data = "1970-01-01"
    if "--data" in argv:
        j = argv.index("--data")
        if j + 1 < len(argv):
            data = argv[j + 1]

    precedente = None
    if "--precedente" in argv:
        j = argv.index("--precedente")
        if j + 1 < len(argv):
            precedente = Path(argv[j + 1]).resolve()

    try:
        manifest, domande, stati = corri(Path(argv[i + 1]).resolve(), catalogo,
                                         data, precedente)
    except Fermata as errore:
        print("FERMATO: %s" % errore, file=sys.stderr)
        return 1

    if "--conta" in argv:
        for stato, n in sorted(conta_stati(manifest).items()):
            print("  %-18s %d" % (stato, n))
        print("  %-18s %d" % ("domande da fare", len(domande)))
        # LA MISURA E SU CIO CHE NON E STATO RIFATTO, ed e una classe nuova per
        # questo progetto: un giro che rifa tutto e uno che non rifa niente
        # producono lo stesso manifest se le risposte non sono cambiate. Un
        # numero che nessuno stampa e un comportamento che nessuno puo provare.
        tenuti, ricalcolati = getattr(costruisci_manifest, "ultimo", ([], []))
        print("  %-18s %d" % ("giro", manifest["giro"]))
        print("  %-18s %d" % ("nodi tenuti", len(tenuti)))
        print("  %-18s %d" % ("nodi ricalcolati", len(ricalcolati)))
        return 0
    if "--domande" in argv:
        for codice, chiave, domanda in domande:
            print("%s · %s · %s" % (codice, chiave, domanda))
        return 0
    print(yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False,
                         width=100))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
