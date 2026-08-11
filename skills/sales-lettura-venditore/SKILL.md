---
name: sales-lettura-venditore
description: "La scheda di lettura di un venditore: dove e forte, dove e scarso, con la citazione che sostiene ogni osservazione e le domande da fargli. Usala quando serve capire come sta vendendo una persona, prepararle un confronto, o decidere su che cosa allenarla."
when_to_use: "Frasi tipiche: 'come sta andando questo venditore?', 'preparami il confronto con lui', 'su cosa lo alleno?', 'perche chiude meno degli altri?'."
funzione: F-C3
---

# Skill · Lettura del venditore, forte e scarso

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Questa skill scrive una scheda, non la manda
  alla persona e non la mette in mano a nessuno. Chi la consegna decide come e quando.
- **Tutto il sapere entra, nessun nome esce.** Vale anche verso l'interno: la scheda parla di **una**
  persona e non nomina i colleghi, nemmeno per dire che uno fa meglio.

**Questa skill produce un artefatto che parla di una persona reale**, ed e cio che la separa dalle
skill dei mestieri A e B. Uno script sbagliato costa una trattativa; una lettura sbagliata costa a
quella persona. Da qui la severita del self-check.

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato.

**Ogni input si legge in due posti distinti e non in uno:**

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** Una soglia che un'azienda usa
non e la soglia giusta: e la sua. L'assenza di un file di `forme/` **non e un guasto**, vuol dire
che quel nodo non ha ancora una forma di questa azienda, e la scheda lo dichiara invece di
riempirlo da solo.

**I nodi che portano la dottrina:**

- `N20_METRICHE_DEL_VENDITORE` · **che cosa si misura di chi vende**, ed e il nodo che detta quali
  osservazioni hanno diritto di stare nella scheda
- `N01_FONDAMENTALI_DELLA_VENDITA` · **dichiara quali sono le fasi**, ed e contro il suo elenco
  che si verifica che ogni osservazione riguardi una fase che il metodo dichiara
- `N44_L_ARTE_DELLA_DOMANDA` · come si conduce con le domande, ed e la prima cosa che si vede
  ascoltando una chiamata
- `N13_RAPPORTO_TONO_E_STORYTELLING` · il rapporto e il tono, che si osservano e non si misurano
- `N45_LE_TRE_CERTEZZE_APPLICATE` · le certezze che chi vende deve portare
- `N46_RESPONSABILITA_DI_CHI_VENDE` · dove finisce la responsabilita della persona e dove comincia
  quella del sistema, e serve a non attribuire a lei cio che e del processo
- `N48_CHE_COSA_E_LA_MENTALITA` · la parte che non e tecnica
- `N49_OBIETTIVO_MENTALITA_ED_EQUILIBRIO` · l'equilibrio fra spinta e tenuta
- `N50_I_GRADINI_DEL_PERCORSO` · a che punto del percorso sta la persona
- `N51_PONTI_FRA_MENTALITA_E_VENDITA` · come la mentalita si vede nei comportamenti di vendita

**I dati dell'azienda:**

- `N52_DIZIONARIO_DEI_DATI_E_DEGLI_STADI` · **il nome, la definizione e il denominatore di ogni
  numero**, ed e contro di lui che la condizione 2 si verifica

**Nessun numero si scrive a memoria.** Un tasso di chiusura senza il suo denominatore non e un
dato: e un'impressione con una percentuale davanti.

## 2. Produzione

La scheda si costruisce **per osservazione**, e ogni osservazione nasce da qualcosa che e stato
detto o da un numero che esiste. Non si parte dai giudizi cercando le prove: si parte da cio che
c'e e si guarda che cosa dice.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-C3`:

1. la scheda porta per ogni osservazione la citazione che la sostiene, e nessuna osservazione resta senza
2. ogni numero della scheda esiste nel dizionario dei dati con lo stesso denominatore
3. la scheda porta almeno 1 domanda da fare alla persona per ogni osservazione
4. la scheda dichiara il periodo su cui e stata costruita e quante chiamate ha guardato
5. la scheda non porta nessun valore complessivo sulla persona e nessun confronto con altre persone

**La condizione 1 e quella che separa una lettura da un'opinione.** *Fa poche domande* non e
un'osservazione: e un'impressione. **L'osservazione porta la frase**, cosi chi legge puo non essere
d'accordo con la lettura senza dover mettere in dubbio il fatto.

**La condizione 3 e quella che rende la scheda utile alla persona invece che su di lei.** Una
osservazione senza domanda e un verdetto. La domanda restituisce alla persona il diritto di
spiegare, e a volte la risposta ribalta la lettura: e proprio per questo che c'e.

**La condizione 5 non e una cautela, e il vincolo `L-PUNTEGGIO`.** Un valore complessivo su una
persona e cio che sopravvive alla scheda: le osservazioni si dimenticano, il numero resta e comincia
a girare. E il confronto con altri fa lo stesso danno, in piu velocemente.

**Il periodo della condizione 4 va scritto anche quando e corto**, anzi soprattutto: una scheda
costruita su 3 chiamate dice cose diverse da una costruita su 40, e chi legge deve saperlo senza
chiedere.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N20_METRICHE_DEL_VENDITORE` non e leggibile, **fermati**: senza di lui non sai quali
  osservazioni hanno diritto di stare nella scheda, e una scheda improvvisata e un elenco di
  impressioni
- se `N52_DIZIONARIO_DEI_DATI_E_DEGLI_STADI` non e leggibile, **fermati**: la condizione 2 non e
  verificabile, e un numero senza denominatore verificato e peggio di nessun numero
- se `N01_FONDAMENTALI_DELLA_VENDITA` non e leggibile, **fermati**: e il nodo che
  dichiara le fasi, e la verifica di coerenza chiede che ogni osservazione riguardi una
  fase che il metodo dichiara. Senza, un'osservazione puo nominare una fase che non
  esiste e nessuno se ne accorge
- se `N44_L_ARTE_DELLA_DOMANDA` non e leggibile, **fermati**: la condizione 3 chiede una
  domanda per ogni osservazione, e la verifica chiede che quelle domande **aprano** un
  discorso invece di chiuderlo. Una domanda chiusa e un verdetto con un punto
  interrogativo in fondo, ed e proprio cio che la condizione 3 esiste per impedire
- se `N13_RAPPORTO_TONO_E_STORYTELLING` non e leggibile, fermati e dillo
- se `N45_LE_TRE_CERTEZZE_APPLICATE` non e leggibile, fermati e dillo
- se `N46_RESPONSABILITA_DI_CHI_VENDE` non e leggibile, fermati e dillo
- se `N48_CHE_COSA_E_LA_MENTALITA` non e leggibile, fermati e dillo
- se `N49_OBIETTIVO_MENTALITA_ED_EQUILIBRIO` non e leggibile, fermati e dillo
- se `N50_I_GRADINI_DEL_PERCORSO` non e leggibile, fermati e dillo
- se `N51_PONTI_FRA_MENTALITA_E_VENDITA` non e leggibile, fermati e dillo

**I vincoli del catalogo, che valgono anche quando tutti gli input ci sono:**

- vincolo `L-PUNTEGGIO`: **nessun valore complessivo sulla persona**. Non un voto, non una fascia,
  non un colore, non una faccina. Cio che esce sono osservazioni citate, numeri con la loro fonte e
  domande. Se stai per scrivere una sintesi che vale come giudizio, fermati
- vincolo `L-AGGREGAZIONE`: **il livello e individuale, e va dichiarato**. Questa funzione produce
  una `scheda`, che e la sola forma in cui il livello individuale esiste. Se il materiale che hai
  copre piu persone, non impastarle: o fai una scheda per persona, o fermati e dillo

**Rifiuti che non dipendono da un input mancante:**

- se un'osservazione non ha la sua citazione, fermati: non e ancora un'osservazione
- se stai per scrivere un numero senza averlo trovato nel dizionario dei dati con lo stesso
  denominatore, fermati e vai a leggerlo
- se stai per confrontare la persona con un collega, anche in positivo, fermati: la condizione 5
  non distingue fra il confronto che lusinga e quello che punisce
- se il periodo su cui hai lavorato non e dichiarabile perche non sai quante chiamate hai guardato,
  fermati: la condizione 4 non e un'intestazione, e la misura di quanto vale il resto
- se stai per prendere una soglia dal file di `forme/` e presentarla come cio che il metodo
  prescrive, fermati: quella e la forma di un'azienda, e va detto
- se stai per attribuire alla persona un esito che il nodo della responsabilita assegna al sistema,
  fermati e rileggilo

## 4. Consegna

L'artefatto e **un file**, e resta un file. **Non si manda alla persona da questa skill**, e non
perche sia delicato: perche chi consegna decide il momento, e il momento e meta del lavoro.

In fondo alla scheda vanno due elenchi, e senza di loro non e finita:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni osservazione;
- **le fonti citate**, cioe da quale nodo viene ogni lettura, cosi chi legge puo risalire al nodo da
  cui viene ogni affermazione.

**Una scheda si discute con la persona di cui parla**, ed e il suo mestiere. Se non regge quella
conversazione, non era una scheda: era un verdetto scritto meglio.
