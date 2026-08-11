---
name: sales-referto-chiamate
description: "Il referto che nasce da molte chiamate e torna dentro lo script: che cosa succede in ogni fase, quali obiezioni nuove stanno arrivando, dove il copione non regge. Usalo quando serve capire che cosa sta cambiando nelle conversazioni, o prima di rimettere mano allo script."
when_to_use: "Frasi tipiche: 'che cosa esce dalle chiamate di questo mese?', 'quali obiezioni nuove stanno arrivando?', 'dove si perdono?', 'devo aggiornare lo script, da dove parto?'."
funzione: F-D3
---

# Skill · Referto delle chiamate che rialimenta lo script

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Questa skill scrive un referto, non riscrive
  lo script e non aggiorna niente da sola: chi cura il copione consuma il referto.
- **Tutto il sapere entra, nessun nome esce.** Qui vale due volte, perche il materiale di partenza
  sono chiamate di persone vere: **nel referto non compare nessun venditore e nessun cliente**, ed e
  anche la condizione 5.

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato.

**Ogni input si legge in due posti distinti e non in uno:**

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** Le obiezioni che un'azienda
sente non sono le obiezioni: sono le sue, e sono proprio la materia che questo referto guarda.
L'assenza di un file di `forme/` **non e un guasto**, e il referto lo dichiara.

**Il nodo contro cui la condizione 1 si conta:**

- `N01_FONDAMENTALI_DELLA_VENDITA` · **dichiara quali sono le fasi**, e il conteggio delle
  sezioni si fa contro il suo elenco

**I nodi delle singole fasi**, che dicono che cosa succede dentro ognuna:

- `N42_APERTURA_E_PRESA_DI_CONTROLLO` · come si apre e chi conduce
- `N04_SCOPERTA` · la fase di indagine
- `N43_IL_PITCH` · come si presenta
- `N06_OBIEZIONI_E_RESISTENZE` · **le obiezioni**, ed e il nodo contro cui si dice se un'obiezione e
  nuova oppure gia nota
- `N05_CHIUSURA` · come si chiude

**I nodi che portano le lenti con cui si legge cio che e successo:**

- `N41_LE_TRE_LEVE_DELLA_VENDITA` · le leve su cui una chiamata si muove
- `N44_L_ARTE_DELLA_DOMANDA` · la qualita delle domande, che si vede nel testo
- `N11_SFIDA_PROIEZIONE_E_COSTO_DELL_INAZIONE` · come si mette in campo il costo di non fare niente
- `N45_LE_TRE_CERTEZZE_APPLICATE` · le certezze che devono passare
- `N13_RAPPORTO_TONO_E_STORYTELLING` · il rapporto e il tono, che si osservano nel detto e non si
  deducono da come suona
- `N51_PONTI_FRA_MENTALITA_E_VENDITA` · dove la parte non tecnica si vede nei comportamenti

**I dati dell'azienda:**

- `N52_DIZIONARIO_DEI_DATI_E_DEGLI_STADI` · **il nome, la definizione e il denominatore di ogni
  numero**, ed e contro di lui che i conteggi della condizione 2 si verificano

**Questo nodo non ha dottrina, ed e voluto:** il dizionario dei dati e di ogni azienda, non del
metodo. Se manca, vale la regola scritta sotto, nel self-check.

## 2. Produzione

Il referto si costruisce **per fase della chiamata**, nell'ordine in cui le fasi si succedono, e
dentro ogni fase **per osservazione ricorrente**. Non si parte dalle chiamate migliori o peggiori:
si scorrono tutte quelle del periodo e si guarda che cosa torna.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-D3`:

1. il referto porta 1 sezione per ogni fase della chiamata che il metodo dichiara
2. ogni osservazione porta il conteggio delle chiamate in cui compare, sul totale guardato
3. ogni obiezione nuova porta la citazione che la sostiene e la fase in cui e comparsa
4. il referto dichiara quante chiamate ha guardato e in quale periodo
5. i numeri sono aggregati sul reparto e nessuna persona compare per nome
6. il referto riporta cio che e stato detto, e non deriva stati d animo di chi parla

**La condizione 2 chiede due numeri e non uno**, e il secondo e quello che di solito manca: *compare
in 7 chiamate* non dice niente finche non si sa **su quante**. Sette su nove e un fatto del reparto,
sette su settanta e rumore.

**La condizione 3 e quella per cui questo referto esiste.** Un'obiezione nuova e l'unica cosa che
puo cambiare lo script: senza la **citazione** chi cura il copione non sa che parole usare, e senza
la **fase** non sa dove metterla.

**La condizione 5 e il vincolo `L-AGGREGAZIONE` applicato al verso del reparto.** Questo artefatto e
un `referto`, quindi il livello e il reparto: se un'osservazione vale per una persona sola, o si
riscrive come osservazione del reparto o esce dal referto. **La forma individuale esiste, e un'altra
funzione**, ed e la scheda della skill `sales-coaching-chiamata`.

**La condizione 6 e il vincolo `L-EMOZIONI`, e la regola pratica e corta:** si scrive cio che e
stato **detto**, non come sembrava. *Ha detto: devo parlarne con il mio socio* e un fatto verificabile
da chi l'ha detto. *Era titubante* e una lettura di chi ascoltava, e la persona non ha modo di
contestarla.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N06_OBIEZIONI_E_RESISTENZE` non e leggibile, **fermati**: senza di lui non sai dire quale
  obiezione e nuova, e la condizione 3 e il motivo per cui questo referto si scrive
- se `N42_APERTURA_E_PRESA_DI_CONTROLLO` non e leggibile, fermati: manca una fase, e la
  condizione 1 chiede una sezione per ognuna
- se `N04_SCOPERTA` non e leggibile, fermati: manca una fase
- se `N43_IL_PITCH` non e leggibile, fermati: manca una fase
- se `N05_CHIUSURA` non e leggibile, fermati: manca una fase
- se `N01_FONDAMENTALI_DELLA_VENDITA` non e leggibile, **fermati**: e il nodo che
  dichiara **l'elenco delle fasi**, ed e contro di lui che la condizione 1 si conta. Gli
  altri nodi delle fasi dicono che cosa succede dentro ognuna; questo dice **quali
  sono**, e senza l'elenco il conteggio delle sezioni non ha un termine di paragone
- se `N41_LE_TRE_LEVE_DELLA_VENDITA` non e leggibile, fermati e dillo
- se `N44_L_ARTE_DELLA_DOMANDA` non e leggibile, fermati e dillo
- se `N11_SFIDA_PROIEZIONE_E_COSTO_DELL_INAZIONE` non e leggibile, fermati e dillo
- se `N45_LE_TRE_CERTEZZE_APPLICATE` non e leggibile, fermati e dillo
- se `N13_RAPPORTO_TONO_E_STORYTELLING` non e leggibile, fermati e dillo
- se `N51_PONTI_FRA_MENTALITA_E_VENDITA` non e leggibile, fermati e dillo
- se `N52_DIZIONARIO_DEI_DATI_E_DEGLI_STADI` non e leggibile, **non fermarti**: scrivi il referto
  con le osservazioni e le citazioni, e dichiara per esteso che i conteggi della condizione 2 non
  sono verificabili perche questa azienda non ha ancora dichiarato il suo dizionario dei dati.
  **E un buco di istanza e non un guasto**, e si chiude in onboarding

**I vincoli del catalogo, che valgono anche quando tutti gli input ci sono:**

- vincolo `L-AGGREGAZIONE`: **il livello e il reparto, e va dichiarato**. Questo e un `referto`, non
  una `scheda`: nessun numero riferito a una persona sola
- vincolo `L-PUNTEGGIO`: **nessun valore complessivo su nessuno**. Non un voto al reparto, non una
  fascia, non un indice di salute. Cio che esce sono conteggi con il loro totale e citazioni
- vincolo `L-EMOZIONI`: **nessuno stato d'animo dedotto dalla voce**. Si riporta il detto

**Rifiuti che non dipendono da un input mancante:**

- se un'osservazione non ha il conteggio **e** il totale, fermati: e mezza condizione 2
- se un'obiezione nuova non ha la citazione o non ha la fase, fermati: cosi non rientra nello
  script, ed e il lavoro per cui il referto nasce
- se stai per scrivere il nome di un venditore o di un cliente, fermati e togli il nome: se
  l'osservazione non regge senza, non e un'osservazione del reparto
- se stai per scrivere che qualcuno era teso, insicuro, convinto o a disagio, fermati e cerca la
  frase: se la frase non c'e, l'osservazione non c'e
- se non sai dire quante chiamate hai guardato e in quale periodo, fermati: la condizione 4 e la
  misura di quanto vale tutto il resto
- se stai per prendere un'obiezione dal file di `forme/` e presentarla come cio che il metodo
  prevede, fermati: quella e la forma di un'azienda, e va detto

## 4. Consegna

L'artefatto e **un file**, e resta un file. **Non riscrive lo script**: lo script e un altro
artefatto, di un'altra funzione, e chi lo cura decide che cosa del referto entra.

In fondo al referto vanno due elenchi, e senza di loro non e finito:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni osservazione;
- **le fonti citate**, cioe da quale nodo viene ogni lettura, cosi chi legge puo risalire al nodo da
  cui viene ogni affermazione.

**Le obiezioni nuove vanno in una sezione loro e non sparse fra le fasi**, perche sono la parte che
qualcuno andra a prendere per lavorarci: se sono sparse, quel qualcuno le rilegge tutte ogni volta.
