# plugin/scripts

Questa cartella ospita **solo** gli script che una skill invoca a runtime, raggiunti via
`${CLAUDE_PLUGIN_ROOT}/scripts/`. Viene copiata sulla macchina di chi installa il plugin, quindi
qui dentro puo stare soltanto codice che ha senso girare a casa di un altro: nessun percorso
assoluto, nessun riferimento a file che vivono fuori dalla cartella del plugin. Nella fase 1 e
vuota, e va bene cosi: le skill di produzione nascono nella fase 9.

I **controllori di progetto** stanno altrove, in `scripts/` alla radice del repo, e non finiscono
mai qui. Sono gli script che leggono l'albero privato `materiale/` per provare la garanzia
anti-perdita e il confine: un plugin installato non puo raggiungere file fuori dalla propria
cartella, quindi un controllore piazzato qui sarebbe rotto per costruzione a casa dell'utente, e
in piu porterebbe fuori la mappa di cosa c'e nel ramo privato.
