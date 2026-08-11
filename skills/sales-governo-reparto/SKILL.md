---
name: sales-governo-reparto
description: "Il disegno di come si governa il reparto vendite: chi fa che cosa fra i tre ruoli, come si riprende chi sbaglia, quali zone nessuno sta guardando. Usalo quando il reparto cresce e smette di reggersi a voce, o quando le cose cadono fra una persona e l'altra."
when_to_use: "Frasi tipiche: 'come organizzo il reparto?', 'chi deve fare cosa?', 'le cose cadono e non si sa di chi erano', 'come riprendo uno senza umiliarlo?', 'sta diventando un feudo'."
funzione: F-C5
---

# Skill · Disegno del governo del reparto

## 0. Contratto

Le regole madri vivono nella skill `sales-contratto`, che e sapere di sfondo sempre disponibile:
**si citano e non si riscrivono**. In forma operativa:

- **Il sistema produce artefatti e non li consegna.** Questa skill scrive un disegno, non
  riorganizza nessuno e non comunica niente a nessuno.
- **Tutto il sapere entra, nessun nome esce.** Nel disegno compaiono **ruoli e attivita**, non
  persone: e anche la condizione 5, quindi qui la regola madre e il contratto della funzione dicono
  la stessa cosa da due parti diverse.

## 1. Contratto degli input

Gli input sono **riferimenti** ai file di metodo che il plugin porta con se, mai contenuto incollato.

**Ogni input si legge in due posti distinti e non in uno:**

- `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/<nodo>.md` dice **che cosa il metodo afferma**, e vale per
  qualunque azienda;
- `${CLAUDE_PLUGIN_ROOT}/metodo/forme/<nodo>.md` dice **come questa azienda lo fa**, e porta i
  segnaposto che l'azienda riempie.

**Cio che sta in `forme/` non e dottrina e non si generalizza mai.** L'organizzazione che
un'azienda si e data non e l'organizzazione giusta: e la sua, e spesso e proprio cio che il disegno
sta rivedendo. L'assenza di un file di `forme/` **non e un guasto**, e il disegno lo dichiara
invece di riempirlo da solo.

**I nodi che portano la dottrina:**

- `N17_I_TRE_RUOLI_DEL_REPARTO` · **i tre ruoli**, ed e il nodo contro cui la condizione 1 si
  verifica: ogni attivita ricorrente deve atterrare su uno di loro
- `N14_FONDAMENTA_DELLA_GESTIONE` · che cosa vuol dire gestire, prima di come
- `N15_PROGETTO_CONTRO_PROCESSO` · che cosa e un processo che si ripete e che cosa e un progetto che
  finisce, e sbagliarne il tipo e il modo piu comune di disegnare male
- `N19_MUFFA_ORGANIZZATIVA_E_FEUDO` · **le zone che nessuno guarda**, ed e il nodo della
  condizione 3
- `N23_CULTURA_DELL_ERRORE` · che cosa succede quando qualcuno sbaglia, prima di chi lo riprende
- `N24_RIPRESA_CALIBRATA` · **come si riprende**, con il dove e il davanti a chi, ed e il nodo della
  condizione 2
- `N25_VALORE_DEL_TEMPO` · dove il tempo di chi guida deve andare
- `N28_VALORI_E_TRASPARENZA` · cio che il disegno deve rendere visibile per non dipendere dalle
  persone
- `N38_CRESCERE_CONTRO_EVOLVERE` · la differenza fra fare piu cose e farle in un altro modo

**I dati dell'azienda:**

- `N53_CADENZA_OPERATIVA_DEL_REPARTO` · **quali momenti fissi esistono gia**, con che frequenza e
  chi c'e, ed e contro di lui che la condizione 4 si verifica

**Questo nodo non ha dottrina, ed e voluto.** La cadenza di un reparto non e una cosa che il metodo
afferma: e una cosa che ogni azienda ha o non ha. Se il file non c'e, **non e un guasto del
prodotto**: vuol dire che quella azienda non ha ancora dichiarato la sua cadenza, e si dichiara in
onboarding. Il disegno lo scrive invece di inventare riunioni che nessuno fa.

## 2. Produzione

Il disegno si costruisce **per attivita ricorrente**, e ogni attivita va appoggiata a un ruolo. Si
parte dall'elenco di cio che il reparto fa davvero ogni settimana, non dall'organigramma: un
organigramma dice chi sta sopra a chi, un disegno del governo dice che cosa cade se qualcuno non
c'e.

Le condizioni che dicono quando l'artefatto e finito, e sono quelle della funzione `F-C5`:

1. il disegno dichiara come il lavoro si divide fra i tre ruoli, e ogni attivita ricorrente ha 1 ruolo
2. il disegno dichiara come si riprende chi sbaglia, con il dove e il davanti a chi
3. il disegno nomina le zone che nessuno guarda e che cosa si guarda perche non lo restino
4. ogni momento del governo che il disegno prevede esiste nella cadenza operativa, oppure la cadenza viene aggiornata insieme
5. il disegno non ordina le persone e non le mette a confronto: parla di ruoli e di attivita

**La condizione 1 chiede 1 ruolo, non almeno uno.** Un'attivita con due ruoli e un'attivita di
nessuno: e la forma in cui le cose cadono senza che nessuno se ne accorga, perche ognuno dei due
ha ragione di pensare che la facesse l'altro.

**La condizione 2 ha due parti, e la seconda e quella che si dimentica.** *Si riprende in privato*
non e ancora una risposta: il **dove** e il **davanti a chi** sono la sostanza, perche una ripresa
fatta davanti al reparto e un'altra cosa dalla stessa frase detta a quattr'occhi.

**La condizione 3 non chiede solo di nominare le zone scoperte, ma che cosa si guarda perche non lo
restino.** Una zona nominata e poi lasciata li e una zona scoperta con un'etichetta.

**La condizione 4 e quella che tiene il disegno attaccato alla realta.** Un momento di governo che
non esiste nella cadenza e un momento che non avverra: o si trova nella cadenza, o si dichiara che
la cadenza va aggiornata insieme al disegno. **Le due cose viaggiano insieme o non viaggiano.**

## 3. Self-check

Prima di consegnare, verifica una per una. **Se un input non e leggibile, fermati e dillo: non
inventare il contenuto mancante.**

- se `N17_I_TRE_RUOLI_DEL_REPARTO` non e leggibile, **fermati**: senza i tre ruoli la condizione 1
  non e verificabile, e un disegno che si inventa i ruoli e un organigramma
- se `N24_RIPRESA_CALIBRATA` non e leggibile, **fermati**: la condizione 2 chiede il dove e il
  davanti a chi, e sono proprio le due cose che nessuno puo dedurre da solo
- se `N19_MUFFA_ORGANIZZATIVA_E_FEUDO` non e leggibile, fermati: la condizione 3 non e formulabile
- se `N14_FONDAMENTA_DELLA_GESTIONE` non e leggibile, fermati e dillo
- se `N15_PROGETTO_CONTRO_PROCESSO` non e leggibile, fermati e dillo
- se `N23_CULTURA_DELL_ERRORE` non e leggibile, **fermati**: e il nodo contro cui si
  verifica che il modo di riprendere **regga** la cultura dell'errore dichiarata. La
  condizione 2 chiede il dove e il davanti a chi, e senza questo nodo si scrive una
  procedura che contraddice cio che l'azienda dice di credere
- se `N25_VALORE_DEL_TEMPO` non e leggibile, fermati e dillo
- se `N28_VALORI_E_TRASPARENZA` non e leggibile, fermati e dillo
- se `N38_CRESCERE_CONTRO_EVOLVERE` non e leggibile, fermati e dillo
- se `N53_CADENZA_OPERATIVA_DEL_REPARTO` non e leggibile, **non fermarti**: scrivi il disegno e
  dichiara per esteso che la cadenza di questa azienda non e stata raccolta, quindi la condizione 4
  resta **aperta** e va chiusa in onboarding. **Questo e un buco di istanza e non un guasto**, e la
  differenza va scritta nell'artefatto invece che lasciata capire

**Rifiuti che non dipendono da un input mancante:**

- se un'attivita ricorrente non ha un ruolo, oppure ne ha due, fermati: la condizione 1 chiede 1
  ruolo, e il caso a due e proprio quello da cui nasce il problema che il disegno risolve
- se la ripresa e descritta senza il dove e il davanti a chi, fermati: manca la meta che conta
- se stai per nominare una zona scoperta senza dire che cosa si guarda perche non lo resti,
  fermati: e un'etichetta, non una risposta
- se stai per prevedere un momento di governo che nella cadenza operativa non esiste, fermati:
  o lo trovi, o scrivi che la cadenza va aggiornata insieme
- se una persona sta per comparire al posto di un ruolo, sostituiscila con il ruolo
- se stai per scrivere chi lavora meglio o chi peggio, fermati: la condizione 5 vieta l'ordinamento
  e il confronto, e questo disegno non e il posto in cui si valutano le persone
- se stai per prendere un assetto dal file di `forme/` e presentarlo come cio che il metodo
  prescrive, fermati: quella e la forma di un'azienda, e spesso e proprio l'assetto che stai
  rivedendo

## 4. Consegna

L'artefatto e **un file**, e resta un file.

In fondo al disegno vanno due elenchi, e senza di loro non e finito:

- **i codici dei concetti consumati**, nella forma `SSS-C-NNNN`, uno per ogni scelta di assetto;
- **le fonti citate**, cioe da quale nodo viene ogni regola, cosi chi legge puo risalire al nodo da
  cui viene ogni affermazione.

**Se la condizione 4 e rimasta aperta, va scritto in testa e non in fondo**: chi legge deve saperlo
prima di cominciare a usare il disegno, non dopo averlo adottato.
