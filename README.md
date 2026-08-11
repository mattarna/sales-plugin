# Sales Manager AI · Scalers Sales System

Un plugin Claude che mette un **direttore vendite** dentro la sessione: una knowledge base di
vendita, leadership e organizzazione (il sapere), piu le funzioni che da quel sapere producono
artefatti concreti (script di call, procedure, mansionari, referti su KPI e CRM, piani, bozze).

Il metodo si chiama **Scalers Sales System** ed e il prodotto vero: sapere trasferibile, neutro
rispetto all'azienda su cui gira. Ogni azienda reale e una **istanza** che riempie i segnaposto,
e i segnaposto sono anche il questionario di onboarding.

## Cosa produce

Sempre e solo file. Un artefatto che puoi leggere, correggere, stampare, mandare tu. Niente
azioni eseguite al posto tuo, niente scritture su sistemi di terzi.

## Stato

In costruzione. Oggi il plugin porta lo scheletro: manifest, marketplace locale e due skill
segnaposto che servono a provare che l'installazione funziona. Il contenuto di metodo e le
funzioni di produzione arrivano nelle fasi successive.

## Installazione (marketplace locale, in sviluppo)

Tre comandi, in quest'ordine, da una sessione aperta sulla radice del repo:

```
/plugin marketplace add ./plugin
/plugin install sales-manager-ai@sales-manager-ai-marketplace
/reload-plugins
```

Il terzo e quello che si dimentica: senza, le skill non compaiono nell'elenco.

## Cosa questo sistema non fa oggi

**Il sistema produce artefatti e non li consegna.** Non invia messaggi, non scrive su CRM, non
esegue azioni verso l'esterno: prepara risorse che poi un umano usa. In concreto:

- le funzioni di comunicazione producono **bozze**, non messaggi partiti;
- la redistribuzione dei lead e un **piano proposto**, non uno spostamento eseguito;
- i referti sono documenti, non notifiche mandate a qualcuno.

Il titolo dice **oggi** apposta, e non e una sfumatura. Questa e la postura di questo ciclo,
perche il sistema non ha tool di invio collegati: non e una legge permanente del prodotto, e
questo file non te la promette come tale. Cio che resta fermo e la **giuntura fra produzione e
consegna**: chi un domani invia consuma l'artefatto invece di riscriverlo, cosi collegare un
mittente sara un'aggiunta e non una riscrittura. Il giorno in cui la postura cambia, cambia qui
e nella skill di contratto, dichiarato.

Perche sta nel README e non in una nota interna: e una caratteristica del prodotto, e chi lo
installa ha diritto di sapere in anticipo dove finisce il perimetro.

## Da dove viene il metodo

La posizione, in una riga: **originale e la sintesi, l'ordine, l'impianto operativo e il
collegamento al sistema di controllo. I principi di base del mestiere non sono nostri e non li
rivendichiamo.**

In pratica. Il sapere di vendita, leadership e organizzazione che il sistema porta viene da un
corpus di formazione, esperienza sul campo e pratica documentata di reparto. Cio che questo
prodotto aggiunge e l'impianto: come i pezzi si tengono, in che ordine si usano, quali artefatti
producono, e come ogni artefatto viene verificato invece di essere dichiarato buono. Dove un
principio e patrimonio comune della disciplina, il sistema lo dice: chiamare "pratica standard
del settore" cio che lo e costa nulla e toglie il fianco.

Niente "metodo esclusivo" su contenuti di base, quindi. La domanda "da dove viene questo?" deve
sempre avere una risposta, e questa e la risposta.
