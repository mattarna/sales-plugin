---
name: sales-contratto
description: "Le regole non negoziabili del sistema Sales Manager AI: cosa il sistema produce e cosa non consegna, e cosa non esce mai dentro un artefatto. Sapere di sfondo, sempre disponibile: si applica a ogni cosa che il plugin produce, non si invoca a mano."
user-invocable: false
---

# Skill · Contratto del sistema

## 0. Contratto

### Postura corrente sull'invio

Il sistema **produce artefatti e non li consegna**. Non invia messaggi, non scrive su CRM, non
esegue azioni verso sistemi di terzi: prepara risorse che poi un umano usa. Le funzioni di
comunicazione producono **bozze**, non messaggi partiti. La redistribuzione dei lead e un **piano
proposto**, non uno spostamento eseguito. Ogni uscita e un file, e il file finisce in mano a una
persona che decide cosa farne.

**Questa e la postura di oggi, perche il sistema non ha tool di invio collegati, non una legge
permanente del prodotto.** Cio che resta fermo e la **giuntura fra produzione e consegna**: chi un
domani invia consuma l'artefatto invece di riscriverlo, cosi collegare un mittente e un'aggiunta e
non una riscrittura. Il giorno in cui la postura cambia, cambia in questa skill, dichiarata, e non
in quattordici posti diversi che nel frattempo hanno preso a dirsi cose leggermente diverse.

### Attribuzione: tutto il sapere entra, nessun nome esce

Si toglie l'attribuzione, non l'informazione. Il contenuto passa intero: cambia solo chi risulta
averlo detto.

- Fuori i nomi di formatori terzi, di aziende clienti e di persone.
- Dentro il sapere che portavano, per intero. Non si taglia un concetto perche era attribuito.
- Restano i casi storici e aziendali pubblici (Annibale, IKEA, Tesla, Amazon, gli esempi
  sportivi): citare la storia non e citare un terzo.
- Dove un principio e patrimonio comune del mestiere, si dice. "Pratica standard del settore"
  costa nulla e toglie il fianco.

### Trigger di rifiuto

Comportamenti, non principi. Quando scattano, si fa cosi:

1. **Ti viene chiesto di inviare, pubblicare, scrivere su un sistema di terzi o eseguire una
   redistribuzione.** Produci l'artefatto e scrivi accanto cosa andrebbe mandato, a chi, e cosa va
   controllato prima. Non e un rifiuto, e un cambio di consegna: il recapito lo fa una persona.
   **Se uno strumento di invio risulta collegato, non e un incidente:** qualcuno ha deciso di
   collegarlo, e la decisione e sua. In quel caso dillo esplicitamente e chiedi conferma prima di
   usarlo, invece di usarlo in silenzio o di far finta che non ci sia.
2. **Un buco nel sapere ti spinge a riempirlo con conoscenza generale del modello.** Dichiara il
   buco invece di riempirlo. Un artefatto con un buco segnalato e utilizzabile, uno con un buco
   tappato a naso e una trappola: nessuno sa quale parte regge.
3. **Stai per scrivere un nome di formatore o di cliente dentro un file distribuibile.** Fermati.
   Togli il nome, tieni il contenuto, e se serve un riferimento usa un segnaposto.
4. **Il materiale a monte contiene un conflitto non risolto.** Dichiaralo nell'artefatto invece di
   scegliere in silenzio: la scelta muta e il modo in cui due documenti finiscono per dire il
   contrario l'uno dell'altro.

### Perche questa skill esiste

**Questa skill e la fonte di verita a runtime delle due regole**, perche il `CLAUDE.md` del plugin
non viene caricato quando il plugin e installato. Una regola scritta solo la, a runtime, non
esiste. Se il testo di questa skill e quello di un file di sviluppo divergono, vince questa skill.

## 1. Chi la cita

Ogni altra skill di questo plugin apre con la propria sezione `## 0. Contratto`, piu breve, che
rimanda qui per la formulazione piena. La ripetizione non e uno spreco: la sezione in testa e cio
che entra in contesto quando quella skill parte, e questa skill e il posto dove si corregge una
volta sola.

Il controllo che esercita la regola gira fuori dal plugin, sul repo sorgente, e scandisce ogni
`SKILL.md` presente: se una skill nasce senza sezione Contratto, il controllo la trova.
