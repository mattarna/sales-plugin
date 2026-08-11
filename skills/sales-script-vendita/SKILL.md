---
name: sales-script-vendita
description: "Lo script di una chiamata di vendita, fase per fase, con le domande da fare e le risposte alle obiezioni ricorrenti. Usala quando serve il copione di una call: primo contatto, scoperta, chiusura, oppure la sua revisione dopo che qualcosa non ha funzionato."
when_to_use: "Frasi tipiche: 'scrivimi lo script della discovery', 'come apro la chiamata?', 'rifammi il copione della closing', 'che domande faccio in questa fase?', 'come rispondo a questa obiezione?'."
funzione: F-A1
---

# Skill · Script di vendita

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa, per questo artefatto:

- **Il sistema produce artefatti e non li consegna.** Questa skill scrive uno script, non lo manda a
  nessuno e non lo carica da nessuna parte. Chi lo usera lo legge da un file.
- **Tutto il sapere entra, nessun nome esce.** Nello script non compaiono nomi di formatori terzi, di
  aziende clienti o di persone. I casi storici e le aziende pubbliche restano con il loro nome.

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato
dentro questa skill.

**Ogni input si legge in due posti distinti e non in uno**, e confonderli e il modo in cui questo prodotto
smetterebbe di servire piu di un'azienda:

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** Una domanda che un'azienda fa
in scoperta non e una regola della scoperta: e la forma di quella. Lo script puo partire da li, e
deve dire che e da li che parte.

L'assenza di un file di `forme/` **non e un guasto**: vuol dire che quel nodo non ha ancora una forma
di questa azienda, e lo script lo dichiara invece di riempirlo da solo.

**I nodi, e la colonna che conta e la seconda.** Quelli qui sotto portano la dottrina che vale per
qualunque azienda:

- `N01_FONDAMENTALI_DELLA_VENDITA` · i principi che valgono in ogni fase
- `N02_PERCORSO_DAL_LEAD_AL_CLIENTE` · **le fasi**, ed e il nodo che decide le sezioni dello script
- `N03_PREPARAZIONE_DELLA_CHIAMATA` · che cosa sta davanti a chi chiama prima di cominciare
- `N04_SCOPERTA` · la fase in cui si indaga il problema
- `N05_CHIUSURA` · la chiamata in cui la decisione si stringe
- `N06_OBIEZIONI_E_RESISTENZE` · **le obiezioni ricorrenti**, e ognuna vuole la sua risposta
- `N11_SFIDA_PROIEZIONE_E_COSTO_DELL_INAZIONE` · le leve che fanno pesare il non decidere
- `N13_RAPPORTO_TONO_E_STORYTELLING` · come si costruisce il rapporto
- `N22_PSICOLOGIA_DEL_COMPRATORE` · chi ho davanti e come si riconosce
- `N41_LE_TRE_LEVE_DELLA_VENDITA` · le tre leve che attraversano ogni interazione
- `N42_APERTURA_E_PRESA_DI_CONTROLLO` · l'ingresso nella chiamata
- `N43_IL_PITCH` · la presentazione della soluzione
- `N44_L_ARTE_DELLA_DOMANDA` · i tre obiettivi di una domanda
- `N45_LE_TRE_CERTEZZE_APPLICATE` · i tre pilastri su cui la persona deve essere certa

**I dati dell'azienda, che cambiano da cliente a cliente:**

- `N08_COPIONE_DI_PRIMO_CONTATTO` · il copione che quest'azienda usa gia
- `N09_COPIONE_SU_CLIENTE_GIA_DENTRO` · il copione su chi e gia dentro
- `N31_OFFERTA_E_PROVE_DELL_AZIENDA` · **che cosa vende e a quale prezzo**
- `N32_CLIENTE_IDEALE_DELL_AZIENDA` · a chi lo vende

**Il prezzo, le condizioni e le promesse non si scrivono qui.** Stanno nel campo
`prezzo_e_modalita` del nodo dell'offerta, e si leggono da li **ogni volta**: una cifra ricordata a
memoria e una cifra che il giorno del cambio di listino resta ferma e nessuno se ne accorge.

## 2. Produzione

Lo script si costruisce **fase per fase, nell'ordine che il nodo del percorso dichiara**, e non
nell'ordine in cui viene comodo scriverlo.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-A1`:

1. lo script porta 1 sezione per ognuna delle fasi che il nodo del percorso dal lead al cliente
   dichiara, e nessuna sezione senza una fase
2. ogni sezione porta almeno 3 domande scritte per esteso, non descritte
3. ogni obiezione ricorrente nominata dal nodo delle obiezioni ha almeno 1 risposta dentro lo script
4. ogni passaggio in cui la fonte detta il testo parola per parola e riportato per esteso e non
   riassunto
5. ogni affermazione dello script risolve contro almeno 1 dei nodi dichiarati come input
6. lo script dichiara, per ogni passaggio dettato, in quale delle 3 condizioni della tensione
   `TNS-01` chi vende puo staccarsene

**La condizione 4 e quella che si sbaglia per prima.** Dove la fonte detta il testo parola per
parola, per esempio l'annuncio del prezzo o la sequenza che chiude la sfida, **si riporta per esteso**:
riassumere un passaggio dettato lo rende inservibile, perche il valore di quel passaggio sta
esattamente nelle parole.

**La condizione 6 non e una formalita, ed e il punto in cui questo metodo non finge.** Le fonti non
concordano su quanto il copione vada seguito alla lettera: il conflitto e dichiarato in
`${CLAUDE_PLUGIN_ROOT}/metodo/tensioni/TNS-01.md`, che **va letto prima di scrivere**. La regola
operativa dice che il copione e il predefinito e nomina tre condizioni in cui ci si stacca; lo script
le riporta **accanto al passaggio a cui si applicano**, non in una nota in fondo.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N02_PERCORSO_DAL_LEAD_AL_CLIENTE` non e leggibile, fermati: senza le fasi non c'e nessuna
  struttura da riempire, e inventarle vorrebbe dire scrivere lo script di un altro processo
- se `N06_OBIEZIONI_E_RESISTENZE` non e leggibile, fermati e dillo: la condizione 3 non e verificabile
- se `N01_FONDAMENTALI_DELLA_VENDITA` non e leggibile, fermati e dillo
- se `N03_PREPARAZIONE_DELLA_CHIAMATA` non e leggibile, fermati e dillo
- se `N04_SCOPERTA` non e leggibile, fermati e dillo
- se `N05_CHIUSURA` non e leggibile, fermati e dillo
- se `N08_COPIONE_DI_PRIMO_CONTATTO` non e leggibile, fermati e dillo: e un dato dell'azienda, e
  senza di lui lo script sarebbe dottrina senza istanza
- se `N09_COPIONE_SU_CLIENTE_GIA_DENTRO` non e leggibile, fermati e dillo
- se `N11_SFIDA_PROIEZIONE_E_COSTO_DELL_INAZIONE` non e leggibile, fermati e dillo
- se `N13_RAPPORTO_TONO_E_STORYTELLING` non e leggibile, fermati e dillo
- se `N22_PSICOLOGIA_DEL_COMPRATORE` non e leggibile, fermati e dillo
- se `N31_OFFERTA_E_PROVE_DELL_AZIENDA` non e leggibile, **fermati**: senza l'offerta non si puo
  scrivere ne il pitch ne l'annuncio del prezzo, e riempirli a memoria e il difetto che questa skill
  esiste per non fare
- se `N32_CLIENTE_IDEALE_DELL_AZIENDA` non e leggibile, fermati e dillo
- se `N41_LE_TRE_LEVE_DELLA_VENDITA` non e leggibile, fermati e dillo
- se `N42_APERTURA_E_PRESA_DI_CONTROLLO` non e leggibile, fermati e dillo
- se `N43_IL_PITCH` non e leggibile, fermati e dillo
- se `N44_L_ARTE_DELLA_DOMANDA` non e leggibile, **fermati**: e il nodo contro cui si
  verifica che le domande di ogni fase colpiscano l'obiettivo di QUELLA fase. Senza di
  lui restano domande sensate messe nel posto sbagliato, che e il difetto piu difficile
  da vedere rileggendo uno script finito
- se `N45_LE_TRE_CERTEZZE_APPLICATE` non e leggibile, fermati e dillo

**Rifiuti che non dipendono da un input mancante:**

- se stai per scrivere un prezzo, una garanzia o una condizione **a memoria**, fermati e vai a
  leggerlo nel campo `prezzo_e_modalita` del nodo dell'offerta
- se stai per riassumere un passaggio che la fonte detta parola per parola, fermati: la condizione 4
  chiede il testo per esteso
- se stai per scegliere fra le due posizioni di `TNS-01`, fermati: la tensione **si dichiara e non si
  risolve**, e la regola operativa dice quando vale l'una e quando l'altra
- se stai per prendere una domanda o una risposta dal file di `forme/` e presentarla come cio che il
  metodo prescrive, fermati: quella e la forma di un'azienda, e va detto
- se un nome di formatore terzo o di azienda cliente sta per finire nello script, toglilo e tieni
  l'informazione

## 4. Consegna

L'artefatto e **un file**, e resta un file: questa skill non lo manda a nessuno.

In fondo allo script vanno due elenchi, e senza di loro l'artefatto non e finito:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni affermazione che lo
  script porta;
- **le fonti citate**, cioe da quale nodo viene ogni sezione, cosi chi legge puo risalire al nodo da
  cui viene ogni affermazione e verificarla.

**Chi riceve lo script deve poter rifare il percorso all'indietro senza chiedere niente a nessuno.**
Un artefatto senza quei due elenchi si legge come se qualcuno lo avesse scritto a memoria, ed e
esattamente cio che non e successo.
