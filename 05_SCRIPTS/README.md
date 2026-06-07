# Scripts [PLACEHOLDER]

> **Nog geen werkende scripts.** Deze map is bewust leeg op een placeholder na. Er is nog
> geen executor-/index-laag, dus er staan hier geen scripts die doen alsof ze werken.
> Conform de doctrine: geen nepscripts.

## Wat hier later kan komen

- Een **index-generator**: leest alle kaarten en schrijft een eenvoudige index naar
  `03_INDEX/metadata/` (pad, type, status, trust level, completeness, tags).
- Een **completeness-/verrijkingsrapport**: lijst van kaarten met lege velden, gevoed door
  de `OPEN:`-regels — de bron voor de cockpit-verrijkingslijst.
- Een **working-tree-view-generator**: rendert de mappenboom van een project als overzicht.
- De **nightly-runner** (zie `04_PROMPTS/nightly_update.md`).

## Regel voor toekomstige scripts

Elk script dat hier komt, moet eerst een capability-kaart in `01_CAPABILITIES/` hebben en
de harde grens respecteren. Een script dat keys/auth/schema raakt, stopt voor Roel.
Markeer elk nog-niet-werkend script duidelijk als placeholder.
