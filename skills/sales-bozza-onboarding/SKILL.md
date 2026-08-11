---
name: sales-bozza-onboarding
description: "Il percorso di ingresso di una persona nuova nel reparto: che cosa riceve, in che giorno, da chi, e che cosa deve saper fare alla fine di ogni settimana. Usalo quando entra qualcuno e serve un percorso scritto invece di un affiancamento improvvisato."
when_to_use: "Frasi tipiche: 'entra una persona nuova, come la formo?', 'preparami l onboarding del closer', 'cosa deve sapere la prima settimana?', 'chi gli da gli accessi?'."
funzione: F-E2
---

# Skill · Bozze di onboarding

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Qui e anche la **condizione 5**: i messaggi
  che il percorso prevede restano **bozze da rileggere prima di partire**. Questa skill non manda
  nessun messaggio di benvenuto e non crea nessun accesso
- **Tutto il sapere entra, nessun nome esce.** Nel percorso compaiono **ruoli**, non nomi: chi
  consegna una cosa e un ruolo, cosi il percorso sopravvive a chi lo esegue oggi

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato.

**Ogni input si legge in due posti distinti e non in uno:**

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Qui i due file pesano piu che altrove:** un onboarding e per meta metodo e per meta questa
azienda, perche una persona nuova deve imparare **come si vende** e insieme **dove sta ogni cosa**.
Confonderli e il modo in cui questo percorso smetterebbe di servire piu di un'azienda. L'assenza di
un file di `forme/` **non e un guasto**, e il percorso lo dichiara invece di riempirlo da solo.

**I nodi che portano la dottrina:**

- `N30_IL_MANSIONARIO_COME_STRUMENTO` · **che cosa la persona dovra saper fare**, ed e il nodo
  contro cui la condizione 4 si costruisce
- `N17_I_TRE_RUOLI_DEL_REPARTO` · in quale ruolo la persona entra, e chi le sta intorno
- `N12_REGOLE_NON_NEGOZIABILI` · cio che va detto il primo giorno e non il terzo mese
- `N28_VALORI_E_TRASPARENZA` · che cosa si dichiara a chi entra
- `N08_COPIONE_DI_PRIMO_CONTATTO` · il copione che dovra saper usare
- `N10_DOPO_IL_SI` · cio che succede a valle, che serve a capire dove finisce il proprio pezzo
- `N34_MATERIALE_SORGENTE_DEL_CORPUS` · da dove viene il sapere, per chi vuole andare a fondo

**I dati dell'azienda:**

- `N31_OFFERTA_E_PROVE_DELL_AZIENDA` · **che cosa vende questa azienda e con quali prove**, e una
  persona nuova non puo dedurlo
- `N33_STRUMENTI_E_RECAPITI_DELL_AZIENDA` · **gli strumenti e i loro indirizzi**, ed e contro di lui
  che la condizione 3 si verifica

**Nessun indirizzo, nessun recapito e nessun link si scrive qui.** Stanno nel nodo degli strumenti e
si leggono da li ogni volta. La ragione viene prima del controllo: **un indirizzo copiato dentro
una skill sopravvive al cambio di strumento**, e manda una persona nuova nel posto sbagliato il suo
primo giorno, che e il giorno in cui ha meno modo di accorgersene.

## 2. Produzione

Il percorso si costruisce **per giorno**, e dentro il giorno **per cosa consegnata**. Non si parte
dagli argomenti da spiegare: si parte da cio che la persona **riceve**, perche e quello che si puo
verificare, e la formazione si appoggia sopra.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-E2`:

1. il percorso porta 1 riga per ogni cosa che la persona nuova riceve, con il giorno in cui la riceve
2. ogni riga nomina chi consegna quella cosa
3. ogni strumento nominato risolve contro il nodo degli strumenti, con il suo indirizzo
4. il percorso dichiara che cosa la persona deve saper fare alla fine di ogni settimana, e ogni voce si verifica guardando un artefatto
5. le bozze dei messaggi restano da rileggere prima di partire

**La condizione 2 e quella che fa la differenza fra un percorso e un elenco di buone intenzioni.**
*Riceve gli accessi* non e una riga: manca chi li da, e una cosa che tutti danno per scontata non la
fa nessuno. **Chi consegna e un ruolo**, cosi il percorso regge quando la persona che lo faceva
cambia lavoro.

**La condizione 4 chiede che ogni voce si verifichi guardando un artefatto**, ed e la stessa
severita del mansionario. *Alla fine della prima settimana conosce il prodotto* non e verificabile.
*Alla fine della prima settimana ha compilato una scheda di scoperta su una chiamata registrata*
si guarda.

**La condizione 5 e la regola madre applicata ai messaggi.** Un onboarding contiene testi che
partono verso una persona vera: il benvenuto, la presentazione al reparto, le istruzioni per gli
accessi. **Restano bozze**, e il percorso lo scrive accanto a ognuna invece di lasciarlo capire.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N33_STRUMENTI_E_RECAPITI_DELL_AZIENDA` non e leggibile, **fermati**: la condizione 3 chiede
  che ogni strumento porti il suo indirizzo, e un indirizzo inventato manda una persona nuova nel
  posto sbagliato il primo giorno
- se `N30_IL_MANSIONARIO_COME_STRUMENTO` non e leggibile, **fermati**: senza di lui non sai che cosa
  la persona deve saper fare, e la condizione 4 non e formulabile
- se `N31_OFFERTA_E_PROVE_DELL_AZIENDA` non e leggibile, **fermati**: che cosa vende questa azienda
  non si deduce, e una persona nuova formata su un'offerta inventata la ripetera ai clienti
- se `N17_I_TRE_RUOLI_DEL_REPARTO` non e leggibile, **fermati**: e il nodo contro cui si
  verifica che **cio che la persona deve saper fare corrisponda a cio che ha ricevuto
  prima**. E la giuntura fra la condizione 1 e la condizione 4, cioe fra quello che le
  dai e quello che pretendi: senza, il percorso chiede alla fine di una settimana una
  cosa che in quella settimana nessuno le ha insegnato
- se `N12_REGOLE_NON_NEGOZIABILI` non e leggibile, fermati e dillo
- se `N28_VALORI_E_TRASPARENZA` non e leggibile, fermati e dillo
- se `N08_COPIONE_DI_PRIMO_CONTATTO` non e leggibile, fermati e dillo
- se `N10_DOPO_IL_SI` non e leggibile, fermati e dillo
- se `N34_MATERIALE_SORGENTE_DEL_CORPUS` non e leggibile, fermati e dillo

**Rifiuti che non dipendono da un input mancante:**

- se una riga non dice **chi consegna**, fermati: e la condizione 2, ed e la riga che nessuno fara
- se una riga non ha un giorno, fermati: un percorso senza giorni e un elenco
- se stai per scrivere un indirizzo, un link o un recapito **a memoria**, fermati e vai a leggerlo
  nel nodo degli strumenti
- se una voce di fine settimana non si verifica guardando un artefatto, fermati: non e ancora
  scritta
- se stai per scrivere un messaggio di benvenuto senza dire che resta una bozza da rileggere,
  fermati: e la condizione 5
- se un nome di persona sta per comparire al posto di un ruolo, sostituiscilo con il ruolo
- se stai per prendere una consuetudine dal file di `forme/` e presentarla come cio che il metodo
  prescrive, fermati: quella e la forma di un'azienda, e va detto

## 4. Consegna

L'artefatto e **un file**, e resta un file. **I messaggi che contiene non partono da qui**: sono
bozze, e chi li manda li rilegge prima.

In fondo al percorso vanno due elenchi, e senza di loro non e finito:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni voce del percorso;
- **le fonti citate**, cioe da quale nodo viene ogni voce, cosi chi legge puo risalire al nodo da
  cui viene ogni affermazione.

**Un percorso di onboarding si rilegge dopo il primo che lo usa**, ed e il momento in cui si scopre
quale riga era ovvia solo per chi l'ha scritta.
