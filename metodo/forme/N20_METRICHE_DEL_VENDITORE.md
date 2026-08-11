# Le metriche del venditore

> Questo documento e prodotto da `scripts/genera_metodo.py` e non si
> corregge a mano. La sorgente vive nel ramo che non si distribuisce: un
> errore si corregge la' e si rigenera. Verso questo albero si scrive solo
> con `scripts/scrivi_distribuibile.py`.

I numeri con cui un venditore si guarda, quali dipendono da lui e quali no, e che cosa si cambia quando uno di quei numeri e basso.

**Questo e un modello e non un documento gia riempito.** Le doppie graffe
sono i punti in cui va il dato di una azienda: finche restano cosi il file
dice la forma del sistema di vendita e non i fatti di nessuno.

## Che cosa dice il metodo

- Il tasso di conversione in chiusura si legge contro il benchmark {{BENCHMARK_CHIUSURA}} del reparto: sotto la fascia c'e un problema strutturale nel modo di condurre la chiusura, dentro la fascia si e nella media e si puo migliorare, sopra la fascia si e sopra la media e si lavora per mantenere e aumentare
- Oltre la soglia di durata della scoperta si stanno facendo domande che non servono o si sta perdendo il controllo della conversazione, e si identifica dove si perde tempo e si taglia
- Oltre la soglia di durata della chiusura, e sistematicamente, c'e un problema nella gestione dei loop: troppo tempo per il consenso a cascata, loop troppo lunghi, oppure poca direttezza
- La durata di riferimento di una chiusura efficace e la soglia bassa dichiarata dal reparto
- Sopra la soglia di loop per chiusura la scoperta non ha alzato abbastanza il livello di certezza, e chiudere spesso al primo o al secondo loop e il segno che si sta lavorando bene
- Sotto la soglia bassa di conversione del follow up si stanno mettendo in follow up lead che non erano mai qualificati, oppure il sistema di nurturing e troppo passivo
- Il foglio dei numeri del venditore sta all'indirizzo {{LINK_KPI}}
- Prima di riascoltare si aspetta la distanza minima dichiarata dal reparto, poi si riascolta con distacco
- Si riascolta una scoperta alla cadenza dichiarata dal reparto, preferibilmente una che non ha convertito, per capire dove si e rotto il processo
- Si riascolta una chiusura alla cadenza dichiarata dal reparto, una persa oppure una chiusa dopo molti loop, per identificare dove si poteva essere piu efficaci
- Il riascolto costa il tempo dichiarato dal reparto ogni settimana
- Il numero di giorni oltre il quale un lead si considera non raggiungibile e la soglia dichiarata dal reparto
- La revisione dei numeri della settimana precedente si fa alla cadenza, nel giorno e nel tempo dichiarati dal reparto, prima di iniziare le chiamata

## Che cosa questo file NON porta

Non porta i puntatori al materiale da cui il metodo nasce, ne le citazioni
testuali delle fonti: quelli vivono nel ramo che non si distribuisce. Non
porta lo stato della lavorazione, perche il metodo non cambia quando cambia
l'avanzamento di chi lo scrive.
