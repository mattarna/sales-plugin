---
name: sales-piano-lancio
description: "Il piano di lancio di un'offerta: la sequenza dei momenti, i canali con chi li presidia, che cosa deve essere pronto prima di aprire e che cosa si guarda per dire che sta andando. Usala quando si apre qualcosa al mercato e serve sapere in che ordine e chi fa cosa."
when_to_use: "Frasi tipiche: 'come lancio questa offerta?', 'in che ordine faccio le cose?', 'che cosa deve essere pronto prima di aprire?', 'su che canali vado?', 'come faccio a capire se il lancio sta andando?'."
funzione: F-B2
---

# Skill · Strategia di lancio

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Questa skill scrive un piano, non apre niente,
  non prenota niente e non manda niente: le sue voci sono lavoro che eseguono delle persone.
- **Tutto il sapere entra, nessun nome esce.** Nel piano compaiono **ruoli**, non nomi di persone, e
  nessun nome di formatore terzo o di azienda cliente.

## 1. Contratto degli input

**Ogni input si legge in due posti distinti e non in uno**, e confonderli e il modo in cui questo prodotto
smetterebbe di servire piu di un'azienda:

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** Un canale che ha funzionato per
un'azienda non e una legge di mercato: e la forma di quella. Il piano puo partire da li, e deve dire
che e da li che parte.

L'assenza di un file di `forme/` **non e un guasto**: vuol dire che quel nodo non ha ancora una forma
di questa azienda, e il piano lo dichiara invece di riempirlo da solo.

**Gli input:**

- `N14_FONDAMENTA_DELLA_GESTIONE` · che cosa regge un lavoro fatto da piu persone
- `N15_PROGETTO_CONTRO_PROCESSO` · **la distinzione che decide la forma del piano**: un lancio e un
  progetto, cioe ha una fine, e cio che resta acceso dopo e processo
- `N16_OBIETTIVO_PRIORITA_E_VALUTA` · come si sceglie che cosa viene prima
- `N21_MERCATO_E_QUADRO_ECONOMICO` · il contesto in cui il lancio cade
- `N22_PSICOLOGIA_DEL_COMPRATORE` · chi deve muoversi, e che cosa lo muove
- `N29_LEGGE_DELLA_NAVIGAZIONE` · **l'ordine**, cioe che nessun momento puo stare prima di cio che lo
  abilita
- `N31_OFFERTA_E_PROVE_DELL_AZIENDA` · che cosa si lancia, a quale prezzo, con quali prove
- `N32_CLIENTE_IDEALE_DELL_AZIENDA` · a chi si lancia, e quindi **quali canali lo raggiungono**
- `N38_CRESCERE_CONTRO_EVOLVERE` · se questo lancio fa piu della stessa cosa o una cosa diversa
- `N41_LE_TRE_LEVE_DELLA_VENDITA` · le leve che il lancio deve azionare
- `N52_DIZIONARIO_DEI_DATI_E_DEGLI_STADI` · **i nomi e le definizioni dei numeri**, ed e il nodo
  contro cui si verifica la condizione 4

**Il prezzo, le condizioni e le promesse non si scrivono qui.** Stanno nel campo `prezzo_e_modalita`
del nodo dell'offerta, e si leggono da li ogni volta.

## 2. Produzione

Il piano si costruisce **all'indietro dal momento in cui si apre**, e non in avanti dal giorno in cui
lo si scrive: si fissa l'apertura, si mette davanti cio che la abilita, e cio che resta e la sequenza.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-B2`:

1. il piano dichiara la sequenza dei momenti del lancio, e ogni momento ha una data oppure il vincolo
   che la determina
2. ogni canale nominato porta chi lo presidia
3. il piano elenca che cosa deve essere pronto prima di aprire, e ogni voce ha 1 responsabile
4. il piano dichiara che cosa si guarda per dire che il lancio sta andando, e ogni numero citato
   esiste nel dizionario dei dati
5. dove il piano prescrive un testo da usare, dichiara se e un copione da dire come e scritto oppure
   un obiettivo da colpire con parole proprie

**La condizione 1 ammette due forme, e la seconda e quella che serve davvero.** Una data si scrive
quando c'e; quando non c'e, si scrive **il vincolo che la determina**, per esempio *il giorno dopo che
la pagina e in aria*. Un piano di sole date inventate invecchia il giorno in cui una slitta; un piano
di vincoli si ricalcola da solo.

**La condizione 4 e quella che si sbaglia per prima, e il difetto ha un nome.** Un piano che dice *si
guarda il tasso di conversione* non ha detto niente finche non si sa **su quale denominatore** quel
numero si calcola, e la definizione non la decide chi scrive il piano: sta nel dizionario dei dati.
Due persone che guardano lo stesso numero calcolato in due modi litigheranno sul lancio invece che
sul mercato.

**La condizione 5 e il punto in cui questo metodo non finge.** Le fonti non concordano su quanto un
testo prescritto vada seguito alla lettera: il conflitto e dichiarato in
`${CLAUDE_PLUGIN_ROOT}/metodo/tensioni/TNS-01.md`, che **va letto prima di scrivere**. Il piano
dichiara, per ogni testo che prescrive, **quale delle due cose e**.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N15_PROGETTO_CONTRO_PROCESSO` non e leggibile, fermati: senza di lui non sai dove finisce il
  lancio e dove comincia cio che resta acceso, e un piano senza fine e un elenco di intenzioni
- se `N29_LEGGE_DELLA_NAVIGAZIONE` non e leggibile, fermati: la sequenza e la sostanza di questo
  artefatto, e senza l'ordine restano delle voci
- se `N52_DIZIONARIO_DEI_DATI_E_DEGLI_STADI` non e leggibile, **fermati e dillo**: e il nodo contro
  cui si verifica la condizione 4, oggi non ha nessun file nel plugin, e si riempie in onboarding.
  Senza, i numeri del piano sarebbero nomi senza definizione
- se `N14_FONDAMENTA_DELLA_GESTIONE` non e leggibile, fermati e dillo
- se `N16_OBIETTIVO_PRIORITA_E_VALUTA` non e leggibile, fermati e dillo
- se `N21_MERCATO_E_QUADRO_ECONOMICO` non e leggibile, fermati e dillo
- se `N22_PSICOLOGIA_DEL_COMPRATORE` non e leggibile, fermati e dillo
- se `N31_OFFERTA_E_PROVE_DELL_AZIENDA` non e leggibile, **fermati**: senza l'offerta non si sa che
  cosa si sta lanciando
- se `N32_CLIENTE_IDEALE_DELL_AZIENDA` non e leggibile, fermati: la scelta dei canali si giustifica
  contro di lui, e senza diventa una preferenza
- se `N38_CRESCERE_CONTRO_EVOLVERE` non e leggibile, fermati e dillo
- se `N41_LE_TRE_LEVE_DELLA_VENDITA` non e leggibile, fermati e dillo

**Rifiuti che non dipendono da un input mancante:**

- se un momento della sequenza non ha ne una data ne il vincolo che la determina, fermati: la
  condizione 1 non e soddisfatta da un momento senza collocazione
- se una voce del pronto prima di aprire non ha 1 responsabile, fermati: una voce senza responsabile
  e una voce che non fara nessuno
- se stai per citare un numero che il dizionario dei dati non definisce, fermati: o lo prendi con il
  nome che ha li, oppure dichiari che quella definizione manca
- se stai per prendere un canale, una cadenza o una prova dal file di `forme/` e presentarlo come cio
  che il metodo prescrive, fermati: quella e la forma di un'azienda, e va detto
- se stai per scrivere un prezzo o una condizione **a memoria**, fermati e vai a leggerlo nel campo
  `prezzo_e_modalita` del nodo dell'offerta
- se stai per prescrivere un testo senza dire se e un copione o un obiettivo, fermati: la condizione 5
  chiede quale delle due cose e
- se un nome di persona sta per finire nel piano al posto di un ruolo, sostituiscilo con il ruolo

## 4. Consegna

L'artefatto e **un file**, e resta un file: questa skill non apre niente e non prenota niente.

In fondo al piano vanno due elenchi, e senza di loro non e finito:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni affermazione che il
  piano porta;
- **le fonti citate**, cioe da quale nodo viene ogni scelta, e per le scelte che vengono da `forme/`
  lo dichiara: chi legge deve poter distinguere il nodo da cui viene una regola del metodo da quello
  da cui viene l'abitudine di un'azienda.

**Un piano di lancio si contesta prima di eseguirlo**, ed e il suo mestiere: chi lo riceve deve poter
chiedere *perche questo prima di quello* e trovare la risposta scritta, invece di doverla chiedere a
chi lo ha scritto.
