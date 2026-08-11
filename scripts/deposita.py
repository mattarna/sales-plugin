#!/usr/bin/env python3
"""Il deposito: scrive la cartella-prodotto e dichiara i segnaposto che restano.

Gira a casa di chi installa il plugin, accanto al motore, e vale per lui la stessa
regola: nessun percorso assoluto, nessun riferimento fuori dalla cartella del
plugin, e il workspace gli viene passato invece di essere cercato.

Il deposito non scrive un manifest: lo completa. Il motore ne produce uno con
`artefatti` e `segnaposto_non_risolti` vuoti, ed e giusto cosi, perche quando
fotografa gli artefatti non esistono ancora. Il deposito arriva dopo che le skill
hanno prodotto, e fa tre cose: cerca i segnaposto dentro ogni artefatto, riempie
`artefatti` con percorso, funzione e segnaposto trovati, e riempie
`segnaposto_non_risolti` con la loro unione.

Cosi il criterio 4 della fase diventa vero per costruzione, e la rete M9 del
validatore diventa quello che deve essere: la prova che la costruzione ha
funzionato, non la sua unica difesa. M9 resta viva perche la cartella-prodotto puo
essere toccata dopo il deposito, e li e la sola cosa che se ne accorge.

I due rifiuti, e sono tutti e due sulla stessa idea. Un artefatto senza `funzione`
dichiarata non si deposita, perche il manifest deve dire quale funzione lo ha
prodotto e inventarlo sarebbe la prima bugia della cartella. Un artefatto con un
segnaposto malformato non si deposita, perche una graffa rotta e esattamente il
posto in cui qualcosa puo essere sopravvissuto alla sostituzione, e dichiararlo
come se fosse a posto vorrebbe dire consegnarlo.

La forma del segnaposto e l'unica cosa duplicata da fuori. Vive nel cancello di
anonimizzazione, che sta nel ramo privato e non si distribuisce, quindi e scritta
qui col motivo accanto. Un controllo al livello del repo pretende che le due
coincidano: una forma duplicata senza controllo e una deriva in attesa.

Uso:
    python deposita.py --manifest percorso --artefatti cartella --dove workspace
    python deposita.py ... --prova       dice cosa farebbe, senza scrivere

Uscite:
    0  depositato
    1  errore d'uso, manifest o artefatti illeggibili
    4  un artefatto non dichiara la funzione che lo ha prodotto
    5  un artefatto porta un segnaposto malformato

Python 3.12, sola libreria standard piu PyYAML.
"""

import re
import shutil
import sys
from pathlib import Path

import yaml

# La forma canonica di un segnaposto, COPIATA ALLA LETTERA dal cancello di
# anonimizzazione. La prima stesura ne aveva scritta una piu larga, e il
# controllo al livello del repo l'ha presa alla prima corsa: la forma del
# cancello e piu stretta in tre punti, cioe esclude una graffa che precede o
# segue, vieta un a capo dentro la chiave e le mette un tetto. Una copia piu
# larga avrebbe dichiarato segnaposto che il cancello non riconosce.
# La forma e la stessa del cancello di anonimizzazione:
# doppie graffe e una chiave in capitali. Duplicata qui perche il cancello vive nel
# ramo privato e a casa di chi installa non esiste. Il controllo che le tiene
# uguali sta al livello del repo, in `scripts/prova_deposito.py`.
ZONA_GRAFFE = re.compile('(?<!\\{)\\{\\{([^{}\\n]{0,80})\\}\\}(?!\\})')
CHIAVE_CANONICA = re.compile(r"^[A-Z][A-Z0-9_]*$")

# Le graffe che non chiudono, o che chiudono male: si cercano apposta, perche una
# graffa rotta e il posto in cui qualcosa puo essere sopravvissuto.
GRAFFA_ROTTA = re.compile(r"\{\{[^{}]*$|^[^{}]*\}\}|\{[^{}]*\}(?!\})")

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.S)


class Fermata(Exception):
    """Non si deposita. Nessuna cartella a meta."""

    def __init__(self, messaggio, codice=1):
        super().__init__(messaggio)
        self.codice = codice


def leggi_yaml(percorso, chi):
    if not percorso.is_file():
        raise Fermata("%s non esiste: %s" % (chi, percorso))
    try:
        return yaml.safe_load(percorso.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as errore:
        raise Fermata("%s non e YAML valido: %s" % (chi, errore))


def funzione_di(testo, nome):
    """La funzione che ha prodotto l'artefatto, dal suo frontmatter."""
    trovato = FRONTMATTER.match(testo)
    if trovato:
        try:
            dati = yaml.safe_load(trovato.group(1)) or {}
        except yaml.YAMLError:
            dati = {}
        codice = str((dati or {}).get("funzione") or "").strip()
        if codice:
            return codice
    raise Fermata("l'artefatto %s non dichiara `funzione` nel frontmatter: il "
                  "manifest deve dire quale funzione lo ha prodotto, e "
                  "inventarlo sarebbe la prima bugia della cartella" % nome, 4)


def segnaposto_di(testo, nome):
    """Le chiavi dei segnaposto ben formati. Uno malformato ferma tutto."""
    chiavi = []
    for numero, riga in enumerate(testo.splitlines(), start=1):
        senza = ZONA_GRAFFE.sub("", riga)
        if GRAFFA_ROTTA.search(senza):
            raise Fermata("l'artefatto %s porta una graffa rotta alla riga %d: "
                          "una graffa rotta e il posto in cui qualcosa puo essere "
                          "sopravvissuto alla sostituzione, e dichiararla a posto "
                          "vorrebbe dire consegnarla" % (nome, numero), 5)
        for trovato in ZONA_GRAFFE.finditer(riga):
            chiave = trovato.group(1)
            if CHIAVE_CANONICA.match(chiave):
                chiavi.append(chiave)
            else:
                raise Fermata("l'artefatto %s porta un segnaposto non canonico "
                              "alla riga %d" % (nome, numero), 5)
    return chiavi


def leggi_artefatti(cartella):
    """[(nome, testo)] per ogni artefatto prodotto, in ordine."""
    if not cartella.is_dir():
        raise Fermata("la cartella degli artefatti non esiste: %s" % cartella)
    fuori = []
    for percorso in sorted(cartella.rglob("*.md")):
        fuori.append((percorso.relative_to(cartella).as_posix(),
                      percorso.read_text(encoding="utf-8", errors="replace"),
                      percorso))
    return fuori


def completa(manifest, artefatti):
    """Il manifest con `artefatti` e `segnaposto_non_risolti` riempiti."""
    voci, conteggio = [], {}
    for nome, testo, _p in artefatti:
        chiavi = segnaposto_di(testo, nome)
        for c in chiavi:
            conteggio[c] = conteggio.get(c, 0) + 1
        voci.append({
            "percorso": nome,
            "funzione": funzione_di(testo, nome),
            "segnaposto_dentro": sorted(set(chiavi)),
        })
    manifest["artefatti"] = voci
    manifest["segnaposto_non_risolti"] = [
        {"chiave": c, "quanti": n} for c, n in sorted(conteggio.items())]
    return manifest


def deposita(manifest, artefatti, dove):
    azienda = str(manifest.get("azienda") or "").strip()
    if not azienda:
        raise Fermata("il manifest non dichiara `azienda`")
    cartella = dove / ".scalers-sales" / "prodotto" / azienda
    (cartella / "artefatti").mkdir(parents=True, exist_ok=True)
    for nome, _testo, percorso in artefatti:
        destinazione = cartella / "artefatti" / nome
        destinazione.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(percorso, destinazione)
    (cartella / "manifest.yaml").write_text(
        yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False, width=100),
        encoding="utf-8", newline="\n")
    return cartella


def opzione(argv, nome):
    if nome in argv:
        i = argv.index(nome)
        if i + 1 < len(argv):
            return argv[i + 1]
    return None


def main(argv):
    if "--help" in argv or "-h" in argv or "--manifest" not in argv:
        print(__doc__)
        return 0
    try:
        percorso = Path(opzione(argv, "--manifest") or "").resolve()
        cartella = Path(opzione(argv, "--artefatti") or "").resolve()
        manifest = leggi_yaml(percorso, "il manifest")
        artefatti = leggi_artefatti(cartella)
        manifest = completa(manifest, artefatti)
        if "--prova" in argv:
            print("artefatti trovati: %d" % len(manifest["artefatti"]))
            print("segnaposto da dichiarare: %d"
                  % len(manifest["segnaposto_non_risolti"]))
            for v in manifest["segnaposto_non_risolti"]:
                print("  %s  %d" % (v["chiave"], v["quanti"]))
            return 0
        dove = Path(opzione(argv, "--dove") or "").resolve()
        prodotta = deposita(manifest, artefatti, dove)
        print("depositato: %s" % prodotta)
        print("  artefatti: %d   segnaposto dichiarati: %d"
              % (len(manifest["artefatti"]),
                 len(manifest["segnaposto_non_risolti"])))
        return 0
    except Fermata as errore:
        print("FERMATO: %s" % errore, file=sys.stderr)
        return errore.codice


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
