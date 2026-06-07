# Prompt — Nightly update [PLACEHOLDER — CONCEPT, nog niet geautomatiseerd]

> **Status: concept.** Er is nog geen draaiende automatisering of executor-laag die dit
> uitvoert. Dit bestand legt vast wát een nachtelijke run moet doen, zodat het later
> ingeschakeld kan worden. Draai het voorlopig hooguit handmatig en gecontroleerd.

## Wat een nightly run moet doen

Een AI-/code-agent krijgt de opdracht om, binnen `INGESTION_RULES.md`:

1. **Ververs gevolgde GitHub-repo-metadata** — check op nieuwe releases, recente commits
   en activiteit van de repos die als knowledge-kaart bestaan.
2. **Detecteer README-/release-/activiteitswijzigingen** — is een tool van richting
   veranderd, gearchiveerd, of fors geüpdatet?
3. **Spot nieuwe relevante docs/video's/posts** waar toegestaan — kandidaten voor nieuwe
   kaarten, niet automatisch ingelijfd.
4. **Werk metadata bij** in `03_INDEX/metadata/`.
5. **Schrijf een changelog** in `03_INDEX/changelogs/` met wat er feitelijk veranderde.

## Harde regels voor de run

- **Overschrijf nooit door mensen gereviewde notities zonder de wijziging te markeren.**
  Bij conflict: laat het origineel staan, voeg een gemarkeerd voorstel toe, en zet de
  kaart in de review-queue (statusveld), zodat Roel het ziet.
- Raak **nooit** de harde grens (keys, auth, schema, `.env`) — een nightly run is per
  definitie autonoom en mag dus alleen veilig, read-only verzamelwerk doen.
- Promoot **nooit** zelf een kaart naar `tested`/`canonical` — dat is een menselijke,
  bewuste beslissing.
- Verzin niets. Onbekend blijft `— ontbreekt nog —`.

## Wat nog nodig is vóór dit kan draaien

Een executor met repo-leestoegang en een schema-bewuste schrijflaag, plus een veilige
trigger (bv. een GitHub Action). Zie de implementatienoot in de root-`README.md`.
