# CLAUDE.md · sales-manager-ai (ramo distribuibile)

> **Nota di scope:** questo file e il contratto di SVILUPPO per le sessioni che lavorano SUL
> sorgente di questo plugin. Questo file **non viene caricato** quando il plugin e installato (comportamento
> documentato di Claude Code). Tutto cio che serve al plugin installato vive nelle skill
> (`skills/*/SKILL.md`). Una regola scritta solo qui, a runtime, non esiste.

Questa cartella e la **radice del plugin**: tutto cio che sta qui dentro e destinato a uscire.
La copia del marketplace, uno zip, un backup fatto a mano: sono tutti modi in cui questa cartella
lascia la macchina di chi la costruisce.

## 1. Le due regole dure, in forma operativa

**Fonte di verita a runtime:** `plugin/skills/sales-contratto/SKILL.md`. Quel file e il testo che
entra davvero nel contesto del plugin installato. Quanto segue e la sua versione per chi sviluppa:
se le due divergono, vince la skill e questo file va corretto.

1. **Il sistema produce artefatti e non li consegna.** Postura corrente di questo ciclo, non legge
   permanente del prodotto: oggi non ha tool di invio collegati, e finche non ne ha l'invio non e
   nel suo perimetro. Le funzioni di comunicazione producono bozze, quella sui lead un piano
   proposto. Cio che resta fermo e la **giuntura fra produzione e consegna**: chi un domani invia
   consuma l'artefatto, non lo riscrive. La formulazione canonica sta in `.planning/PROJECT.md`
   sezione Constraints, e si cita, non si riscrive.
2. **Tutto il sapere entra, nessun nome esce.** Si toglie l'attribuzione, non l'informazione. Fuori
   i nomi di formatori terzi, di aziende clienti e di persone. Restano i casi storici e aziendali
   pubblici (Annibale, IKEA, Tesla, Amazon, gli esempi sportivi): citare la storia non e citare un
   terzo.

## 2. Il confine dei due rami

Il progetto ha due alberi fisicamente separati sotto la radice del repo:

- `plugin/` (questa cartella) e cio che si distribuisce;
- `materiale/` e cio che non esce mai: sorgente congelato, strato normalizzato, valori reali.

**Nessun file di `materiale/` puo essere referenziato da dentro `plugin/`, nemmeno con un percorso
relativo che risale (`..`).** Motivo tecnico, non stilistico: l'installazione copia **solo** la
cartella del plugin, quindi un riferimento che esce da qui punta a un file che sulla macchina
dell'utente non esiste. E con sorgente di tipo directory il `.gitignore` non ferma la copia: il
confine e topologico, il gitignore e solo la seconda difesa.

Corollario pratico: cio che serve dentro il plugin si **duplica** dentro il plugin, con i
segnaposto al posto dei valori reali. Mai un rimando all'esterno, mai un percorso assoluto, mai un
symlink. I riferimenti interni si scrivono con `${CLAUDE_PLUGIN_ROOT}` e `${CLAUDE_SKILL_DIR}`.

Il controllo che esercita questa regola e `scripts/prova_confine.py` alla radice del repo (non qui
dentro: vedi `scripts/README.md`). Copia questa cartella in una cartella vuota e dichiara cosa e
arrivato.

## 3. `allowed-tools` pre-approva, non restringe

Trappola nota, e il nome inganna:

| Campo | Cosa fa davvero |
|---|---|
| `allowed-tools` | **Pre-approva** strumenti per il turno che invoca la skill. Ogni altro strumento resta comunque chiamabile: non e una barriera, e un lasciapassare |
| `disallowed-tools` | **Toglie** strumenti dal pool, e vale finche l'utente non manda il messaggio successivo. E questo il campo che restringe |

**Divieto esplicito:** nessun `allowed-tools` di questo plugin puo pre-approvare strumenti di rete
o strumenti di scrittura fuori dal workspace dell'utente. La revisione di ogni skill guarda il
frontmatter prima del corpo.

## 4. L'unico warning atteso di `claude plugin validate` e quello sulla version

`claude plugin validate ./ --strict` emette **un solo** warning, ed e questo:

```
plugins[0] plugin.json -> version: No version specified.
```

**E una decisione, non un difetto.** La `version` e omessa apposta: senza, Claude Code usa lo SHA
del commit e ogni commit e un aggiornamento, quindi nessun bump a mano puo essere dimenticato. Si
mettera esplicita alla prima consegna a un'azienda. Senza `--strict` il validatore esce 0.

Nota storica, corretta nel piano 01-04: fino al piano 01-02 questa sezione dichiarava atteso un
warning diverso, quello sul fatto che questo file non venga caricato dal plugin installato. Quel
warning **il validatore non lo emette piu**. Il fatto resta vero e resta il punto di questo file
(vedi la nota di scope in testa), ma non e piu una riga che compare a schermo.

## 5. Rito di chiusura: il cancello di confine

Prima di chiudere qualunque fase si lancia, dalla radice del progetto:

```
python scripts/check_confine.py
```

**Nove verdi su nove e la condizione per considerare la fase chiusa.** Non e un traguardo della
fase 1: dalla fase 2 in poi vale per ogni fase, perche ogni fase aggiunge file a questa cartella e
ogni file aggiunto e un'occasione di sbagliare.

| Codice | Cosa verifica |
|---|---|
| C1 | Nessun MCP dichiarato: zero `.mcp.json`, zero chiavi `mcpServers` |
| C2 | Ogni `SKILL.md` trovata a runtime apre con `## 0. Contratto` e porta le due regole dure |
| C3 | `marketplace.json` dichiara `source` nella forma di due caratteri che vuole la specifica |
| C4 | Confine topologico: copiando questa cartella altrove non arriva nulla del ramo privato |
| C5 | Pacchettizzazione coerente: il build **rileva** ogni file non dichiarato e ogni voce dichiarata mancante, e li nomina con il loro percorso. Rileva, non filtra: vedi il paragrafo qui sotto |
| C6 | Nessun `allowed-tools` nel frontmatter di nessuna skill (vedi sezione 3) |
| C8 | Cancello pre-commit armato: `core.hooksPath` di questo repo punta alla cartella `githooks` e l'hook esiste. Fuori da un albero di lavoro git il controllo e verde con nota, perche li non c'e niente da misurare |

C2 e C6 si costruiscono l'elenco delle skill **camminando la cartella**, mai da una lista scritta
nel codice: una skill nuova nasce gia sotto controllo. C5 legge `PACKAGING_ALLOWLIST.txt`, che sta
in questa cartella: **aggiungere un file qui dentro obbliga a dichiararlo li**, altrimenti il
cancello diventa rosso. E voluto.

### Chi rileva e chi impedisce: perche il cancello sta prima del commit

Fino al 2026-07-31 questa sezione lasciava credere che l'allowlist impedisse la distribuzione di un
file non dichiarato. Non e vero. `marketplace.json` tiene `source: "./"`, cioe la sorgente e questa
cartella, quindi l'installazione la copia **per intero**, e la copia filtrata che il build produce
non e consumata da nessun comando di installazione. L'allowlist **rileva** un file non dichiarato e
lo nomina, ma non ne impedisce la copia.

Cio che impedisce e un hook git **pre-commit** che lancia il cancello di confine prima che il commit
esista. Il commit e il punto vero in cui un file smette di essere locale, perche da un commit nasce
ogni install e ogni update: un file non dichiarato non arriva a un commit, quindi non arriva a un
install ne a un update. Si arma una volta per repo con `python scripts/installa_hook_git.py`, e C8
diventa rosso se qualcuno lo disarma.

**Dove il pre-commit si ferma, scritto qui e non in una nota:** `git commit --no-verify` lo salta ed
e una scelta di git, non correggibile; misura l'albero di lavoro e non l'indice, quindi ferma anche
un file non messo in stage ma non vede un file messo in stage e poi cancellato dal disco; un clone
nuovo parte disarmato finche non si lancia l'installatore.

**Cio che e stato scartato, e perche.** Far puntare il marketplace alla copia costruita dal build
renderebbe l'allowlist un filtro vero. Costringerebbe pero a un build prima di ogni ricarica del
plugin per tutte le fasi dalla 2 alla 10, dove si itera molto sulle skill, e un passaggio in piu a
ogni giro e un passaggio che qualcuno salta. La sorgente `git` resta la meta quando il repo va su
una piattaforma remota: li viaggia solo cio che e tracciato, e il pre-commit e proprio cio che
decide cosa viene tracciato.
