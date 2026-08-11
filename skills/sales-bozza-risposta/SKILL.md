---
name: sales-bozza-risposta
description: "La bozza di una risposta a un venditore o a un responsabile: risponde al punto, ogni frase si appoggia a un nodo del metodo, e resta un testo da rileggere prima di partire. Usala quando qualcuno ha sollevato una questione e serve una risposta che dica il metodo invece del buon senso."
when_to_use: "Frasi tipiche: 'mi ha scritto questo, cosa rispondo?', 'come glielo dico senza demolirlo?', 'preparami la risposta a questa lamentela', 'devo rispondere a una richiesta di aumento'."
funzione: F-E1
---

# Skill · Bozze di risposta a venditori e responsabili

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Qui non e solo la regola di sfondo: e la
  **condizione 4** di questa funzione, che pretende che la bozza lo dichiari dentro di se. **Questa
  skill non manda niente a nessuno**, e il testo che produce lo dice a chi lo legge
- **Tutto il sapere entra, nessun nome esce.** Nella bozza non compaiono terzi ne clienti. Il
  destinatario e una persona che lavora qui, e non e un nome che esce: e chi riceve il testo

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato.

**Ogni input si legge in due posti distinti e non in uno:**

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** Il modo in cui un'azienda
risponde e il suo, e la bozza puo partire da li dicendo che e da li che parte. L'assenza di un file
di `forme/` **non e un guasto**.

**I nodi che portano la dottrina, e sono l'elenco chiuso contro cui la condizione 2 si verifica:**

- `N12_REGOLE_NON_NEGOZIABILI` · cio che non e trattabile, e va detto senza ammorbidirlo
- `N23_CULTURA_DELL_ERRORE` · che cosa succede quando qualcuno sbaglia
- `N24_RIPRESA_CALIBRATA` · **come si riprende**, con il dove e il davanti a chi
- `N28_VALORI_E_TRASPARENZA` · che cosa si dice e che cosa non si tace
- `N46_RESPONSABILITA_DI_CHI_VENDE` · dove finisce la responsabilita della persona
- `N19_MUFFA_ORGANIZZATIVA_E_FEUDO` · le zone che nessuno guarda, quando la questione nasce li
- `N26_LEGGE_DEL_COPERCHIO` · quanto una squadra puo salire oltre chi la guida
- `N27_INFLUENZA_E_PROCESSO` · l'influenza come lavoro
- `N35_I_CINQUE_LIVELLI_DELLA_LEADERSHIP` · a che livello si sta guidando
- `N36_IMPERATIVO_DEL_COMANDO` · cio che chi guida non puo delegare
- `N39_FORMULE_E_PRINCIPI_CARDINE` · i principi contro cui si legge una situazione
- `N37_IL_CASO_STUDIO_STORICO` · il caso lungo, quando serve mostrare invece che spiegare
- `N47_I_CASI_STORICI_DELLA_MENTALITA` · gli altri casi noti
- `N48_CHE_COSA_E_LA_MENTALITA` · la parte non tecnica
- `N49_OBIETTIVO_MENTALITA_ED_EQUILIBRIO` · l'equilibrio fra spinta e tenuta
- `N50_I_GRADINI_DEL_PERCORSO` · a che punto del percorso sta chi riceve la risposta
- `N51_PONTI_FRA_MENTALITA_E_VENDITA` · dove la mentalita si vede nei comportamenti

**Questo elenco e chiuso, ed e il punto della funzione.** Una risposta che si appoggia a qualcosa
che non e in questa lista non sta dicendo il metodo: sta dicendo un'opinione con il tono del metodo.

## 2. Produzione

La bozza si costruisce **dal punto ricevuto**, non dall'argomento in generale: si cita cio che la
persona ha detto o chiesto, e si risponde a quello. Poi, frase per frase, si guarda contro quale
nodo ognuna si appoggia.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-E1`:

1. la bozza risponde al punto che le e stato dato, e lo cita in apertura
2. ogni affermazione della bozza risolve contro almeno 1 dei nodi dichiarati come input
3. la bozza dichiara chi la deve rileggere prima che parta
4. la bozza resta un testo da rileggere e da mandare a mano: il documento dichiara che il sistema prepara e non consegna

**La condizione 2 e la piu stretta di tutta questa famiglia di skill, e la ragione va detta.** Una
bozza di risposta e il posto in cui e piu facile scrivere **buon senso**: frasi ragionevoli, vere,
che nessuno contesterebbe e che non vengono da nessuna parte. Il buon senso non risolve contro
nessun nodo. **Chi riceve la risposta crede di stare leggendo il metodo dell'azienda**, e se non lo
e, quella frase diventa metodo il giorno dopo perche qualcuno l'ha letta scritta.

**Zero vincoli non vuol dire liberta.** Questa funzione non porta codici di vincolo perche non
produce numeri ne letture su persone: il suo argine e la condizione 2, ed e piu stretto di un
vincolo, non piu largo.

**La condizione 1 chiede la citazione in apertura**, non un riassunto. Un riassunto e gia una
risposta: decide che cosa la persona ha detto prima di risponderle.

**La condizione 3 non e una formalita.** Una bozza che non dice chi la rilegge e una bozza che parte
cosi com'e, e questa funzione esiste perche non parta cosi com'e.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N12_REGOLE_NON_NEGOZIABILI` non e leggibile, **fermati**: una risposta che ammorbidisce una
  regola non negoziabile fa piu danno del silenzio
- se `N24_RIPRESA_CALIBRATA` non e leggibile, **fermati** quando il punto e una ripresa: il dove e
  il davanti a chi sono la sostanza, e nessuno li puo dedurre
- se `N23_CULTURA_DELL_ERRORE` non e leggibile, **fermati**: e il nodo contro cui si
  verifica che **il modo di dirlo** regga la cultura dell'errore dichiarata. Una
  risposta puo essere giusta nel contenuto e smentire nel tono cio che l'azienda dice
  di credere, e chi la riceve crede al tono
- se `N28_VALORI_E_TRASPARENZA` non e leggibile, fermati e dillo
- se `N46_RESPONSABILITA_DI_CHI_VENDE` non e leggibile, fermati e dillo
- se `N19_MUFFA_ORGANIZZATIVA_E_FEUDO` non e leggibile, fermati e dillo
- se `N26_LEGGE_DEL_COPERCHIO` non e leggibile, fermati e dillo
- se `N27_INFLUENZA_E_PROCESSO` non e leggibile, **fermati**: e il nodo contro cui si
  verifica la condizione 2, cioe che **ogni affermazione risolva contro un nodo di
  ingresso**. E la condizione piu stretta di questa skill, e senza questo nodo il
  controllo che la sostiene non esiste
- se `N35_I_CINQUE_LIVELLI_DELLA_LEADERSHIP` non e leggibile, fermati e dillo
- se `N36_IMPERATIVO_DEL_COMANDO` non e leggibile, fermati e dillo
- se `N39_FORMULE_E_PRINCIPI_CARDINE` non e leggibile, fermati e dillo
- se `N37_IL_CASO_STUDIO_STORICO` non e leggibile, fermati e dillo
- se `N47_I_CASI_STORICI_DELLA_MENTALITA` non e leggibile, fermati e dillo
- se `N48_CHE_COSA_E_LA_MENTALITA` non e leggibile, fermati e dillo
- se `N49_OBIETTIVO_MENTALITA_ED_EQUILIBRIO` non e leggibile, fermati e dillo
- se `N50_I_GRADINI_DEL_PERCORSO` non e leggibile, fermati e dillo
- se `N51_PONTI_FRA_MENTALITA_E_VENDITA` non e leggibile, fermati e dillo

**Rifiuti che non dipendono da un input mancante:**

- se una frase della bozza non risolve contro nessuno dei nodi dell'elenco, **togli la frase**: e la
  condizione 2, ed e il difetto per cui questa funzione ha diciassette input
- se stai per scrivere una frase ragionevole che non sai a quale nodo appoggiare, fermati: e buon
  senso, e chi legge lo prendera per metodo
- se non hai il punto ricevuto per esteso, fermati: senza, la condizione 1 non e verificabile e stai
  rispondendo a una tua parafrasi
- se stai per riassumere il punto invece di citarlo, fermati e cita
- se non sai dire chi deve rileggere la bozza, fermati: la condizione 3 chiede un ruolo, non una
  formula di cortesia
- se stai per scrivere che il testo puo partire cosi com'e, fermati: la condizione 4 dice il
  contrario, e il contrario e la regola madre di questo prodotto
- se stai per prendere una formula dal file di `forme/` e presentarla come cio che il metodo
  prescrive, fermati: quella e la forma di un'azienda, e va detto

## 4. Consegna

L'artefatto e **una bozza**, e resta un file. **Questa skill non manda niente**: il testo va
riletto da chi la condizione 3 nomina, e mandato a mano.

In fondo alla bozza vanno due elenchi, e senza di loro non e finita:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni affermazione;
- **le fonti citate**, cioe da quale nodo viene ogni frase, cosi chi rilegge puo risalire al nodo da
  cui viene ogni affermazione.

**Gli elenchi qui servono a chi rilegge piu che a chi riceve**, ed e il loro uso principale in
questa skill: chi rilegge deve poter controllare la condizione 2 riga per riga senza rifare il
lavoro. Prima di mandare, gli elenchi si tolgono: **fanno parte della bozza, non del messaggio.**
