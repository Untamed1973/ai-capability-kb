# CONTEXT PACK

> Dit bestand is de **AI-ingang** van dit systeem. Elke nieuwe chat of executor — Claude,
> Codex, Gemini of een ander — leest dit als **eerste**. Het vertelt wát er bestaat, welke
> regels gelden, waar je moet kijken en wanneer je moet stoppen. Houd het kort en
> extreem helder. Dit bestand is heilig: bij twijfel wint dit document.

## Wat dit systeem is

Een project-agnostische kennis- en capability-bank in platte markdown + git. Het is
geen taalmodel-uitbreiding en maakt niemand "slimmer" — het maakt je **beter uitgerust**:
je weet meteen welk gereedschap er ligt, hoe het ingezet wordt, en waar de grenzen
lopen. Het bestand vertelt wát er ligt (landkaart); het *uitvoeren* gebeurt via de
executor met toegang tot de echte bestanden.

## Lees in deze volgorde

1. `00_SYSTEM/OPERATING_PRINCIPLES.md` — de doctrine en de autonomie-regel.
2. `00_SYSTEM/CAPABILITY_ROUTER.md` — hoe je een vraag naar een route vertaalt.
3. `00_SYSTEM/CARD_SCHEMA.md` — hoe kaarten zijn opgebouwd (de velden).
4. `01_CAPABILITIES/` — wat we kunnen gebruiken (de gereedschapskist).
5. `02_KNOWLEDGE/` — wat we weten (de bibliotheek + patterns).
6. `00_SYSTEM/DECISION_LOG.md` — waarom het systeem is zoals het is.
7. `00_SYSTEM/SOURCE_VERIFICATION.md` — hoe je een bron verifieert (origineel
   vs. kloon, duplicaten herkennen). Raadpleeg dit telkens als je een bron beoordeelt.

## De gouden regels (samenvatting — bron is OPERATING_PRINCIPLES.md)

- **Autonoom mag** als een taak schoon routeert naar een capability met status
  `tested` of `canonical` **én** binnen de veilige grens valt.
- **Stop en vraag Roel** bij: onbekende/ongeteste capability, of iets dat de harde grens
  raakt — databaseschema, auth, RLS-policies, migraties, `.env`, of API-keys. Ook bij
  destructieve operaties. De grens stopt áltijd, ook als twee AI's het eens zijn dat het
  veilig is.
- **Maak de echte fout eerst zichtbaar.** Fix geen gissingen; diagnose vóór actie.
- **Eén waarheid.** Niets woont op twee plekken. Lijsten en queues zijn gegenereerde
  lenzen, geen tweede opslag.
- **Een leeg veld is een taak, geen fout.** Onvolledige kaarten mogen bestaan en zijn
  doorzoekbaar; ontbrekende velden worden expliciet gemarkeerd.
- **Schema-wijziging stopt voor Roel.** Het kaart-schema (`CARD_SCHEMA.md`) breidt met de
  hand uit, als bewuste beslissing — nooit autonoom.

## Hoe je Roel het beste helpt

- Werk in het Nederlands. Direct, bondig, geen over-uitleg.
- Eén architectuurbeslissing per keer; bundel geen opties.
- Lever altijd ready-to-paste prompts of commands wanneer Roel iets moet uitvoeren —
  nooit alleen een beschrijving.
- Spreek tegen wanneer hij iets verkeerd inschat; presenteer geen aannames als feiten.

## Waar je een nieuw project mee verbindt

Een nieuw project leent de capabilities en patterns uit deze KB. De KB *definieert* de
doctrine; het project *handhaaft* die via z'n eigen control-files (`AGENTS.md`,
`debug-boundary-check.sh`). Verwijs naar bestaande kaarten in plaats van te dupliceren.
