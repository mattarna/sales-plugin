---
name: sales-scelta-manager
description: "Il referto per scegliere chi guidera il reparto: un parametro per riga, ognuno con l'evidenza che lo sostiene e le domande ancora aperte. Usala quando c'e da promuovere qualcuno a responsabile, valutare un candidato esterno, o capire perche chi guida non sta funzionando."
when_to_use: "Frasi tipiche: 'chi promuovo a capo del reparto?', 'e pronto per guidare?', 'questo candidato regge il ruolo?', 'perche il reparto non gira sotto di lui?'."
funzione: F-C4
---

# Skill · Scelta del manager

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Questa skill scrive un referto, non promuove
  nessuno e non scarta nessuno. **La decisione resta di chi decide**, ed e il punto della
  condizione 4.
- **Tutto il sapere entra, nessun nome esce.** I casi storici pubblici restano e sono materia
  legittima: citare una storia nota non e citare un terzo.

**Questo referto entra in una decisione che cambia la vita lavorativa di qualcuno.** Un referto che
si presenta come una risposta invece che come un'istruttoria toglie a chi decide proprio la parte
che gli compete.

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato.

**Ogni input si legge in due posti distinti e non in uno:**

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** Il profilo che un'azienda cerca
non e il profilo giusto: e il suo. L'assenza di un file di `forme/` **non e un guasto**, e il
referto lo dichiara invece di riempirlo da solo.

**I nodi che portano la dottrina:**

- `N18_PILASTRI_E_PARAMETRI_DEL_GESTORE` · **i parametri, e sono l'ossatura del referto**: la
  condizione 1 chiede una riga per ognuno di quelli che questo nodo dichiara, e nessuno in piu
- `N35_I_CINQUE_LIVELLI_DELLA_LEADERSHIP` · a che livello guida oggi la persona, che non e lo stesso
  del ruolo che ricopre
- `N26_LEGGE_DEL_COPERCHIO` · quanto il reparto puo salire oltre chi lo guida
- `N27_INFLUENZA_E_PROCESSO` · l'influenza come lavoro e non come carattere
- `N29_LEGGE_DELLA_NAVIGAZIONE` · saper tracciare la rotta prima di chiedere di seguirla
- `N36_IMPERATIVO_DEL_COMANDO` · cio che chi guida non puo delegare
- `N39_FORMULE_E_PRINCIPI_CARDINE` · i principi contro cui si legge un comportamento
- `N37_IL_CASO_STUDIO_STORICO` · il caso lungo, che serve a vedere i parametri in movimento invece
  che in astratto
- `N47_I_CASI_STORICI_DELLA_MENTALITA` · gli altri casi noti, per la parte non tecnica

**Nessun parametro si inventa e nessuno si toglie.** L'elenco lo detta il nodo dei pilastri: un
parametro aggiunto perche sembrava sensato e una preferenza di chi scrive travestita da metodo.

## 2. Produzione

Il referto si costruisce **per parametro**, nell'ordine in cui il nodo dei pilastri li dichiara. Non
si parte dall'impressione sulla persona cercando i parametri che la confermano: si scorre l'elenco e
si guarda che evidenza c'e per ognuno, **compresa quella che non c'e**.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-C4`:

1. il referto porta 1 riga per ogni parametro che il nodo dei pilastri dichiara
2. ogni parametro porta la citazione o il numero osservato che lo sostiene, e la fonte di ognuno
3. il referto porta le domande ancora aperte, cioe i parametri su cui non c e evidenza
4. il referto non produce nessun valore complessivo sulla persona: chi decide legge i parametri e decide

**La condizione 3 e la piu importante e la piu facile da saltare.** Un parametro senza evidenza e un
dato del referto, non un buco da riempire a intuito: dice a chi decide **che cosa deve ancora
andare a vedere**. Un referto che tace i parametri scoperti sembra piu completo ed e meno utile,
perche fa passare per accertato cio che nessuno ha guardato.

**La condizione 1 e un conteggio, e va fatto.** Se il nodo dichiara sette parametri e le righe sono
sei, manca una riga: non e una svista di forma, e un parametro su cui il referto non dice niente
senza dichiarare di non dirlo.

**La condizione 4 non e una cautela, e il vincolo `L-PUNTEGGIO`.** Il momento in cui un referto
diventa un voto e quando qualcuno aggiunge in fondo una riga di sintesi, con le migliori intenzioni.
Da quel momento nessuno legge piu i parametri: leggono la riga.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N18_PILASTRI_E_PARAMETRI_DEL_GESTORE` non e leggibile, **fermati**: senza di lui non esiste
  l'elenco dei parametri, e la condizione 1 non e nemmeno formulabile
- se `N35_I_CINQUE_LIVELLI_DELLA_LEADERSHIP` non e leggibile, **fermati**: e il nodo
  contro cui si verifica che i parametri **senza evidenza** finiscano fra le domande
  aperte. Senza di lui la condizione 3 diventa un elenco a discrezione, e la parte che
  sparisce e sempre quella scomoda
- se `N26_LEGGE_DEL_COPERCHIO` non e leggibile, fermati e dillo
- se `N27_INFLUENZA_E_PROCESSO` non e leggibile, fermati e dillo
- se `N29_LEGGE_DELLA_NAVIGAZIONE` non e leggibile, fermati e dillo
- se `N36_IMPERATIVO_DEL_COMANDO` non e leggibile, fermati e dillo
- se `N39_FORMULE_E_PRINCIPI_CARDINE` non e leggibile, fermati e dillo
- se `N37_IL_CASO_STUDIO_STORICO` non e leggibile, fermati e dillo
- se `N47_I_CASI_STORICI_DELLA_MENTALITA` non e leggibile, fermati e dillo

**Il vincolo del catalogo, che vale anche quando tutti gli input ci sono:**

- vincolo `L-PUNTEGGIO`: **nessun valore complessivo sulla persona**. Non un voto, non una fascia,
  non un pronto oppure non pronto. Cio che esce sono parametri con la loro evidenza e domande
  aperte. Se stai per scrivere una raccomandazione finale, fermati: quella e la decisione, e non e
  tua

**Rifiuti che non dipendono da un input mancante:**

- se il numero delle righe non coincide con il numero dei parametri dichiarati, fermati e conta
- se un parametro non ha ne una citazione ne un numero osservato, **non inventare l'evidenza**:
  quel parametro va nelle domande ancora aperte, ed e li che serve
- se stai per scrivere che la persona e adatta oppure non adatta, fermati: e esattamente il valore
  complessivo che la condizione 4 vieta
- se stai per mettere la persona a confronto con chi ricopre oggi il ruolo, fermati: il referto
  parla di parametri, e il confronto e un'altra domanda
- se stai per prendere un profilo dal file di `forme/` e presentarlo come cio che il metodo
  prescrive, fermati: quella e la forma di un'azienda, e va detto
- se un caso storico sta per essere usato come prova invece che come lente, fermati: i casi
  illustrano un parametro, non lo verificano su questa persona

## 4. Consegna

L'artefatto e **un file**, e resta un file.

In fondo al referto vanno due elenchi, e senza di loro non e finito:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni parametro;
- **le fonti citate**, cioe da quale nodo viene ogni lettura, cosi chi legge puo risalire al nodo da
  cui viene ogni affermazione.

**Il referto si consegna a chi decide, non alla persona di cui parla**, e la differenza non e di
riservatezza: e che la persona ha diritto a un confronto, e un confronto non si fa passando un
documento. Per quello c'e la scheda della skill `sales-lettura-venditore`, che nasce per essere
letta insieme.
