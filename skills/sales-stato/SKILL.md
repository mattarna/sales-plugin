---
name: sales-stato
description: "Referto sullo stato di costruzione del plugin Sales Manager AI: quali strati esistono gia, quali cartelle sono ancora vuote, e cosa quindi il sistema oggi puo e non puo fare. Usala quando non sai se una cosa e gia stata costruita, prima di chiedere al plugin un lavoro che il suo contenuto non regge ancora."
when_to_use: "Frasi tipiche: 'a che punto sta il plugin?', 'cosa c'e gia dentro?', 'il metodo e gia caricato o e ancora vuoto?', 'perche questa funzione non produce niente?'."
---

# Skill · Stato di costruzione

## 0. Contratto

Il sistema **produce artefatti e non li consegna**: prepara file, non invia e non esegue azioni
verso l'esterno. Questa e la postura di oggi, perche non ci sono tool di invio collegati, non una
legge permanente del prodotto.

Tutto il sapere entra, **nessun nome esce**: si toglie l'attribuzione, non l'informazione. Fuori i
nomi di formatori terzi e di clienti, dentro il contenuto per intero.

**Formulazione piena, trigger di rifiuto e casi limite: `sales-contratto`.** Quella skill e la
fonte di verita a runtime; questa sezione e il suo promemoria, e dove le due divergono vince
`sales-contratto`.

## 1. Cosa fa questa skill

Legge l'albero del plugin installato e produce un referto onesto: cosa esiste, cosa e vuoto, cosa
non si puo ancora chiedere. Non inventa contenuto di metodo, perche in questa fase non ne esiste:
se una cartella e vuota, il referto dice vuota.

## 2. Come si legge lo stato

Guarda queste posizioni, risolte da `${CLAUDE_PLUGIN_ROOT}`. Per ognuna: esiste, e quanti file
veri contiene (i segnaposto di cartella non contano come contenuto).

| Posizione | Cosa dovrebbe contenere | Stato atteso in questa fase |
|---|---|---|
| `${CLAUDE_PLUGIN_ROOT}/.claude-plugin/` | manifest e marketplace | pieno |
| `${CLAUDE_PLUGIN_ROOT}/skills/` | le funzioni produttrici | solo segnaposto: questa skill e `sales-contratto` |
| `${CLAUDE_PLUGIN_ROOT}/catalog/` | i nodi del sapere e le funzioni, in YAML | vuoto |
| `${CLAUDE_PLUGIN_ROOT}/metodo/dottrina/` | il sapere trasferibile, de-attribuito | vuoto |
| `${CLAUDE_PLUGIN_ROOT}/metodo/forme/` | script e procedure con i segnaposto | vuoto |
| `${CLAUDE_PLUGIN_ROOT}/metodo/profilo/` | la scheda azienda astratta | vuoto |
| `${CLAUDE_PLUGIN_ROOT}/hooks/` | le difese a runtime | vuoto |
| `${CLAUDE_PLUGIN_ROOT}/scripts/` | gli script invocati dalle skill | vuoto |

Se serve un file che appartiene a questa skill, il suo posto e `${CLAUDE_SKILL_DIR}`, non un
percorso costruito a mano dalla radice del plugin: cosi il riferimento regge anche se la skill
viene rinominata.

## 3. Forma del referto

Tre righe e una tabella, in quest'ordine:

1. **Cosa il plugin puo fare oggi**, in una frase. Se la risposta e "installarsi e dire come sta",
   scrivi quella: e la verita di questa fase.
2. **La tabella** delle posizioni qui sopra, con la colonna stato compilata da cio che trovi
   davvero, non da cio che dice questo file.
3. **Cosa manca per la prossima cosa utile**, in una frase.

Se cio che trovi non corrisponde allo stato atteso della tabella, riporta cio che hai trovato e
segnala lo scarto. Il disallineamento e un'informazione, non un errore da nascondere.
