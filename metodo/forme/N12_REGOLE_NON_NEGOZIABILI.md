# Le regole non negoziabili

> Questo documento e prodotto da `scripts/genera_metodo.py` e non si
> corregge a mano. La sorgente vive nel ramo che non si distribuisce: un
> errore si corregge la' e si rigenera. Verso questo albero si scrive solo
> con `scripts/scrivi_distribuibile.py`.

Le regole che valgono comunque, il setup che deve essere in ordine prima della prima chiamata, e la ragione per cui una regola si segue anche quando non se ne capisce ancora il motivo.

**Questo e un modello e non un documento gia riempito.** Le doppie graffe
sono i punti in cui va il dato di una azienda: finche restano cosi il file
dice la forma del sistema di vendita e non i fatti di nessuno.

## Che cosa dice il metodo

- Il venditore ha un numero di telefono dedicato a {{AZIENDA}} e non usa il proprio numero personale
- Il campo della descrizione della scheda porta {{PROMESSA}}
- Il campo della categoria della scheda porta {{CATEGORIA_ATTIVITA}}
- Il campo dell'indirizzo della scheda porta {{INDIRIZZO_AZIENDA}}
- Il campo del link della scheda porta {{SITO_AZIENDA}}
- I tutorial dello strumento di gestione dei contatti stanno agli indirizzi {{LINK_TUTORIAL_CRM}}
- La registrazione di ogni chiamata si manda a {{RECAPITO_REGISTRAZIONI}}
- La registrazione si manda entro la fine della giornata in cui la chiamata e avvenuta, non il giorno dopo e non quando si ha tempo
- Le note complete della chiamata si inseriscono entro la soglia di minuti dichiarata dal reparto dalla fine della chiamata, e non a fine giornata
- Nel gruppo di messaggistica creato all'onboarding entrano il coach, {{FORMATORE_1}} e {{REFERENTE_OPERATIVO}}
- Non si chiama oltre l'orario serale dichiarato dal reparto senza un accordo esplicito con il lead
- Si evita la fascia pomeridiana dichiarata dal reparto per i lead con lavori fisici o in turno, perche sono spesso in pausa o nel momento di massima stanchezza
- Il primo contatto si fa entro la soglia di minuti dichiarata dal reparto dall'ingresso del lead in pipeline
- Durante l'interruzione del pagamento il cliente si aggiorna alla cadenza di minuti dichiarata dal reparto
- Parlando con un lead il venditore rappresenta {{NOME_METODO}}, {{FORMATORE_1}}, {{REFERENTE_OPERATIVO}} e l'intero team

## Dove le fonti non concordano

Questo nodo tocca 1 conflitto dichiarato fra le fonti del metodo. Il
conflitto e scritto e non risolto, e la sua regola operativa dice quando
vale una posizione e quando vale l'altra.

- `TNS-01`, in `metodo/tensioni/TNS-01.md`

## Che cosa questo file NON porta

Non porta i puntatori al materiale da cui il metodo nasce, ne le citazioni
testuali delle fonti: quelli vivono nel ramo che non si distribuisce. Non
porta lo stato della lavorazione, perche il metodo non cambia quando cambia
l'avanzamento di chi lo scrive.
