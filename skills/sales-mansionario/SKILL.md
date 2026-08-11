---
name: sales-mansionario
description: "Il mansionario di un ruolo di vendita: che cosa fa ogni giorno, con quale cadenza, e con quale criterio di fatto si dice che l'ha fatto. Usala quando serve mettere per iscritto il lavoro di un ruolo, o rivederlo perche qualcuno non sa che cosa deve fare."
when_to_use: "Frasi tipiche: 'scrivimi il mansionario del closer', 'che cosa deve fare ogni giorno?', 'come faccio a sapere se l'ha fatto?', 'rifammi le procedure del reparto'."
funzione: F-A2
---

# Skill · Procedure e mansionario

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Questa skill scrive un mansionario, non lo
  assegna a nessuno e non lo carica su nessuno strumento.
- **Tutto il sapere entra, nessun nome esce.** Nel mansionario compaiono **ruoli**, non nomi di
  persone.

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato.

**Ogni input si legge in due posti distinti e non in uno**, e confonderli e il modo in cui questo prodotto
smetterebbe di servire piu di un'azienda:

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** Una cadenza che un'azienda tiene
non e la cadenza giusta: e la sua. Il mansionario puo partire da li, e deve dire che e da li che
parte.

L'assenza di un file di `forme/` **non e un guasto**: vuol dire che quel nodo non ha ancora una forma
di questa azienda, e il mansionario lo dichiara invece di riempirlo da solo.

**I nodi che portano la dottrina:**

- `N30_IL_MANSIONARIO_COME_STRUMENTO` · **che cosa e un mansionario e a che cosa serve**, ed e il
  nodo che detta la forma dell'artefatto
- `N12_REGOLE_NON_NEGOZIABILI` · **le regole che diventano voci**, e nessuna puo restare fuori
- `N02_PERCORSO_DAL_LEAD_AL_CLIENTE` · le fasi che il ruolo attraversa
- `N03_PREPARAZIONE_DELLA_CHIAMATA` · il setup obbligatorio prima di cominciare
- `N04_SCOPERTA` · che cosa il ruolo fa nella fase di indagine
- `N07_FOLLOW_UP_E_NURTURING` · il lavoro che non finisce con la chiamata
- `N10_DOPO_IL_SI` · cio che va fatto quando la vendita e chiusa

**I dati dell'azienda:**

- `N33_STRUMENTI_E_RECAPITI_DELL_AZIENDA` · **gli strumenti e i loro indirizzi**

**Nessun indirizzo, nessun recapito e nessun link si scrive qui.** Stanno nel nodo degli strumenti e
si leggono da li ogni volta: un indirizzo copiato dentro una skill e un indirizzo che sopravvive al
cambio di strumento.

## 2. Produzione

Il mansionario si costruisce **per attivita ricorrente**, non per fase della trattativa: le fasi
descrivono una chiamata, il mansionario descrive una giornata.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-A2`:

1. il mansionario porta 1 voce per ogni attivita ricorrente del ruolo, e ognuna dichiara la propria
   cadenza
2. ogni voce porta il criterio di fatto con cui si dice che e stata fatta, e il criterio si verifica
   guardando un artefatto o un numero
3. ogni regola non negoziabile del nodo omonimo compare come voce
4. ogni strumento nominato risolve contro il nodo degli strumenti, e nessuno strumento compare senza
   il suo indirizzo
5. il mansionario dichiara dove il copione va tenuto e in quali condizioni chi lo usa puo staccarsene,
   invece di dire solo che va seguito

**La condizione 2 e quella che separa un mansionario da un elenco di buone intenzioni.** *Fare i
follow up* non e una voce: e un proposito. **Il criterio di fatto si verifica guardando qualcosa**:
un artefatto compilato, un numero su un foglio, un messaggio partito. Se non riesci a dire dove si
guarda, quella voce non e ancora scritta.

**La condizione 5 e il punto in cui questo metodo non finge.** Le fonti non concordano su quanto il
copione vada seguito alla lettera: il conflitto e dichiarato in
`${CLAUDE_PLUGIN_ROOT}/metodo/tensioni/TNS-01.md`, che **va letto prima di scrivere**. Un mansionario
che dicesse soltanto *segui il copione* prenderebbe una posizione che le fonti non prendono.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N30_IL_MANSIONARIO_COME_STRUMENTO` non e leggibile, fermati: senza di lui non sai che forma
  deve avere l'artefatto, e un mansionario improvvisato e un elenco di attivita
- se `N12_REGOLE_NON_NEGOZIABILI` non e leggibile, fermati: la condizione 3 non e verificabile, e
  proprio quelle regole sono la parte che nessuno puo dedurre
- se `N02_PERCORSO_DAL_LEAD_AL_CLIENTE` non e leggibile, fermati e dillo
- se `N03_PREPARAZIONE_DELLA_CHIAMATA` non e leggibile, fermati e dillo
- se `N04_SCOPERTA` non e leggibile, fermati e dillo
- se `N07_FOLLOW_UP_E_NURTURING` non e leggibile, fermati e dillo
- se `N10_DOPO_IL_SI` non e leggibile, fermati e dillo
- se `N33_STRUMENTI_E_RECAPITI_DELL_AZIENDA` non e leggibile, **fermati**: la condizione 4 chiede che
  ogni strumento porti il suo indirizzo, e un indirizzo inventato manda una persona nel posto
  sbagliato

**Rifiuti che non dipendono da un input mancante:**

- se una voce non ha un criterio di fatto che si verifichi guardando un artefatto o un numero,
  fermati: quella voce non e ancora scritta
- se stai per scrivere un indirizzo, un link o un recapito **a memoria**, fermati e vai a leggerlo nel
  nodo degli strumenti
- se stai per scrivere che il copione *va seguito* e basta, fermati: la condizione 5 chiede anche
  **quando ci si stacca**, e la tensione `TNS-01` dice quali sono le tre condizioni
- se stai per prendere una cadenza o una procedura dal file di `forme/` e presentarla come cio che il
  metodo prescrive, fermati: quella e la forma di un'azienda, e va detto
- se un nome di persona sta per finire in una voce al posto di un ruolo, sostituiscilo con il ruolo

## 4. Consegna

L'artefatto e **un file**, e resta un file.

In fondo al mansionario vanno due elenchi, e senza di loro non e finito:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni voce;
- **le fonti citate**, cioe da quale nodo viene ogni voce, cosi chi legge puo risalire al nodo da cui
  viene ogni affermazione.

**Un mansionario si discute**, ed e il suo mestiere: chi lo riceve deve poter chiedere *perche questa
voce* e trovare la risposta senza chiedere a chi l'ha scritto.
