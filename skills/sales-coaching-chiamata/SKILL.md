---
name: sales-coaching-chiamata
description: "La scheda di coaching che nasce da una singola chiamata: che cosa e successo in ogni fase, con la citazione che lo sostiene e le domande da fare alla persona. Usala per preparare un confronto dopo una chiamata ascoltata, o per allenare qualcuno su un caso concreto invece che in astratto."
when_to_use: "Frasi tipiche: 'ho ascoltato questa chiamata, come e andata?', 'preparami il debrief', 'su cosa lo riprendo dopo questa call?', 'fammi vedere dove ha perso il controllo'."
funzione: F-D4
---

# Skill · Scheda di coaching da una chiamata

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Vale anche qui, e qui va detto con precisione
  perche la condizione 5 chiede che la scheda **sia consegnata alla persona di cui parla**. Le due
  cose stanno insieme cosi: **la skill dichiara il destinatario dentro l'artefatto, non compie la
  consegna.** Chi consegna consuma la scheda, non la riscrive
- **Tutto il sapere entra, nessun nome esce.** Verso l'esterno: nella scheda non compare il cliente
  della chiamata. La persona di cui la scheda parla e il suo destinatario, ed e un'altra cosa

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato.

**Ogni input si legge in due posti distinti e non in uno:**

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** Il modo in cui un'azienda apre
le chiamate non e il modo giusto: e il suo. L'assenza di un file di `forme/` **non e un guasto**, e
la scheda lo dichiara.

**Il nodo contro cui la condizione 2 si verifica:**

- `N01_FONDAMENTALI_DELLA_VENDITA` · **dichiara quali sono le fasi**, e ogni osservazione deve
  nominarne una che esiste in questo elenco

**I nodi delle singole fasi**, che dicono che cosa succede dentro ognuna:

- `N42_APERTURA_E_PRESA_DI_CONTROLLO` · come si apre e chi conduce
- `N04_SCOPERTA` · la fase di indagine
- `N43_IL_PITCH` · come si presenta
- `N06_OBIEZIONI_E_RESISTENZE` · come si sta dentro un'obiezione
- `N05_CHIUSURA` · come si chiude

**Le lenti con cui si legge cio che e stato detto:**

- `N41_LE_TRE_LEVE_DELLA_VENDITA` · le leve su cui la chiamata si e mossa
- `N44_L_ARTE_DELLA_DOMANDA` · la qualita delle domande fatte, che si vede nel testo
- `N11_SFIDA_PROIEZIONE_E_COSTO_DELL_INAZIONE` · se il costo di non fare niente e stato messo in campo
- `N45_LE_TRE_CERTEZZE_APPLICATE` · quali certezze sono passate e quali no
- `N13_RAPPORTO_TONO_E_STORYTELLING` · il rapporto, che si legge in cio che e stato detto
- `N51_PONTI_FRA_MENTALITA_E_VENDITA` · dove la parte non tecnica si e vista

**I dati dell'azienda:**

- `N52_DIZIONARIO_DEI_DATI_E_DEGLI_STADI` · il nome e la definizione di ogni stadio, per dire in
  quale stadio la chiamata si e fermata senza inventare il vocabolario

**Questo nodo non ha dottrina, ed e voluto**, e se manca vale la regola scritta nel self-check.

## 2. Produzione

La scheda si costruisce **per osservazione**, e ogni osservazione nasce da una frase della chiamata.
Si segue l'ordine in cui le cose sono successe, non l'ordine di gravita: una scheda che comincia dal
peggio e un rimprovero con le citazioni in fondo.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-D4`:

1. la scheda porta per ogni osservazione la citazione della chiamata che la sostiene
2. ogni osservazione nomina la fase in cui e avvenuta, e la fase esiste fra quelle che il metodo dichiara
3. la scheda porta almeno 1 domanda da fare alla persona per ogni osservazione
4. la scheda dichiara quale chiamata ha guardato e quando
5. la scheda e consegnata alla persona di cui parla, e il documento lo dichiara
6. la scheda riporta cio che e stato detto, e non deriva stati d animo da come e stato detto

**La condizione 3 e quella che rende la scheda utile alla persona invece che su di lei.** Una
osservazione senza domanda e un verdetto. La domanda le restituisce il diritto di spiegare, e a
volte la risposta ribalta la lettura: e per questo che c'e.

**La condizione 5 non chiede alla skill di consegnare**, chiede che il documento **dichiari** il
proprio destinatario. Ed e una dichiarazione che cambia come la scheda va scritta: **un documento
che la persona leggera non si scrive come un documento che parla di lei alle sue spalle.** Se una
frase non la scriveresti sapendo che la legge, quella frase e sbagliata anche se e vera.

**La condizione 6 e il vincolo `L-EMOZIONI`, e sulla singola chiamata e piu insidiosa che altrove:**
avendo il testo di una conversazione intera, la tentazione di dire come suonava e forte. *Ha detto:
non so se riusciamo a partire prima dell'estate* e un fatto. *Era imbarazzato* e una lettura, e in
una scheda che la persona legge diventa un'accusa che non puo confutare.

**Questa scheda parla di UNA chiamata.** Se dalla lettura esce un'osservazione che vale in generale,
quella non appartiene a questa scheda: appartiene al referto del reparto, che e la skill
`sales-referto-chiamate`, e li si scrive col suo conteggio.

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N42_APERTURA_E_PRESA_DI_CONTROLLO` non e leggibile, **fermati**: la condizione 2 chiede che
  ogni osservazione nomini una fase esistente, e una fase mancante rende non verificabile la meta
  delle osservazioni
- se `N04_SCOPERTA` non e leggibile, fermati: manca una fase
- se `N43_IL_PITCH` non e leggibile, fermati: manca una fase
- se `N06_OBIEZIONI_E_RESISTENZE` non e leggibile, fermati: manca una fase
- se `N05_CHIUSURA` non e leggibile, fermati: manca una fase
- se `N01_FONDAMENTALI_DELLA_VENDITA` non e leggibile, **fermati**: e il nodo che
  dichiara **l'elenco delle fasi**, e la verifica deterministica chiede che ogni
  osservazione abbia la sua citazione **e la sua fase**. Senza l'elenco, la condizione 2
  puo essere soddisfatta nominando una fase che il metodo non dichiara
- se `N41_LE_TRE_LEVE_DELLA_VENDITA` non e leggibile, fermati e dillo
- se `N44_L_ARTE_DELLA_DOMANDA` non e leggibile, **fermati**: la condizione 3 chiede una
  domanda per ogni osservazione, e la verifica chiede che quelle domande **aprano** un
  discorso invece di chiuderlo. In una scheda che la persona legge, una domanda chiusa
  non e una domanda: e un'accusa a cui si puo solo rispondere si oppure no
- se `N11_SFIDA_PROIEZIONE_E_COSTO_DELL_INAZIONE` non e leggibile, fermati e dillo
- se `N45_LE_TRE_CERTEZZE_APPLICATE` non e leggibile, fermati e dillo
- se `N13_RAPPORTO_TONO_E_STORYTELLING` non e leggibile, fermati e dillo
- se `N51_PONTI_FRA_MENTALITA_E_VENDITA` non e leggibile, fermati e dillo
- se `N52_DIZIONARIO_DEI_DATI_E_DEGLI_STADI` non e leggibile, **non fermarti**: scrivi la scheda con
  le osservazioni e le citazioni, e dichiara che lo stadio in cui la chiamata si e fermata non e
  nominabile col vocabolario di questa azienda, che non l'ha ancora dichiarato. **E un buco di
  istanza e non un guasto**, e si chiude in onboarding

**I vincoli del catalogo, che valgono anche quando tutti gli input ci sono:**

- vincolo `L-AGGREGAZIONE`: **il livello e individuale, e questa e la sola forma in cui esiste**.
  Una `scheda` e la porta stretta che il vincolo lascia aperta: se il materiale copre piu chiamate o
  piu persone, non e questa la funzione, e il referto del reparto
- vincolo `L-PUNTEGGIO`: **nessun valore complessivo sulla persona**. Non un voto alla chiamata, non
  un andata bene oppure andata male. Cio che esce sono osservazioni citate e domande
- vincolo `L-EMOZIONI`: **nessuno stato d'animo dedotto da come e stato detto**. Si riporta il detto

**Rifiuti che non dipendono da un input mancante:**

- se un'osservazione non ha la citazione della chiamata, fermati: non e ancora un'osservazione
- se un'osservazione non nomina la fase, o nomina una fase che il metodo non dichiara, fermati
- se un'osservazione non ha almeno una domanda, fermati: senza, e un verdetto
- se stai per dare un giudizio complessivo sulla chiamata, fermati: e il vincolo `L-PUNTEGGIO`, e
  in una scheda che la persona legge e anche la riga che si ricordera al posto di tutte le altre
- se stai per scrivere come suonava la voce invece di cio che e stato detto, fermati e cerca la frase
- se stai per scrivere il nome del cliente della chiamata, fermati e togli il nome
- se stai per mettere la persona a confronto con un collega, fermati: qui c'e una chiamata sola, e
  il confronto non ha nemmeno il materiale per esistere
- se stai per scrivere una frase che non scriveresti sapendo che la legge la persona, fermati e
  riscrivila: la condizione 5 dice che la leggera

## 4. Consegna

L'artefatto e **un file**, e resta un file. **La skill non lo manda a nessuno**: scrive in testa a
chi e destinato, e chi consegna decide il momento. Il momento e meta del lavoro.

In fondo alla scheda vanno due elenchi, e senza di loro non e finita:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni osservazione;
- **le fonti citate**, cioe da quale nodo viene ogni lettura, cosi chi legge puo risalire al nodo da
  cui viene ogni affermazione.

**La scheda si legge insieme alla persona, non le si consegna e basta.** Le domande della
condizione 3 esistono per essere fatte: se nessuno le fa, la scheda ha prodotto un verdetto con un
punto interrogativo alla fine.
