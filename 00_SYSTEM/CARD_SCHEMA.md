# Card Schema (canoniek)

De **enige** bron van waarheid voor hoe kaarten zijn opgebouwd. Vulprompts in
`04_PROMPTS/` verwijzen naar dit bestand; ze kopiëren het schema niet. Wijzigingen aan
dit schema zijn een bewuste beslissing en gaan via `DECISION_LOG.md` (zie
`OPERATING_PRINCIPLES.md` §6).

## Statussen (voor beide kaarttypen)

| Status | Betekenis | Telt mee voor autonomie? |
|---|---|---|
| `unverified` | Net toegevoegd, niet gecontroleerd | Nee |
| `reviewed` | Door een mens gelezen en plausibel bevonden | Nee |
| `tested` | In de praktijk werkend gezien | **Ja** |
| `canonical` | Bewezen, vaste keuze voor dit type werk | **Ja** |
| `rejected` | Geprobeerd/beoordeeld en afgewezen (blijft staan als les) | Nee |

Een kaart wordt pas `canonical` na een bewuste beslissing (genoteerd in `DECISION_LOG.md`).

## Completeness

- Geen veld is verplicht-op-straffe-van-error.
- Elke kaart heeft een **completeness-status**: `compleet` / `gedeeltelijk` / `kaal`.
- Lege velden worden gemarkeerd met `— ontbreekt nog —`.
- Onderaan elke half-gevulde kaart staat een regel: `OPEN: <veld1>, <veld2>`.
- Incomplete kaarten zijn geldig en doorzoekbaar. De cockpit-verrijkingslijst leest deze
  markeringen later uit.

## Capability-kaart (`01_CAPABILITIES/`)

Beantwoordt: "welk handje is dit en wanneer pak ik het?"

- **Capability-naam**
- **Type** — agent / skill / mcp_server / cli_tool / api_service / model / scraper /
  workflow / executor
- **Wat het kan** — in één of twee zinnen
- **Wanneer te gebruiken** — en wanneer juist niet
- **Inputs nodig**
- **Outputs**
- **Beste executor** — wie draait dit het beste (Claude Code / Codex / GitHub Action / …)
- **Beslisvelden** (voor het wegen van routes):
  - Toegang & vorm — API / MCP / CLI / lokaal
  - Kosten — prijsmodel + aard
  - Gebruiksgemak — kant-en-klaar / wat config / veel werk
  - Kwaliteit / betrouwbaarheid
  - Snelheid
  - Grens-impact — raakt het de harde grens?
  - Afhankelijkheden & lock-in
- **Risico's**
- **Voorbeeldgebruik**
- **Tags**
- **Gerelateerde capabilities** / **Gerelateerde knowledge-kaarten**
- **Completeness-status** + `OPEN:`-regel
- **Status** — unverified / reviewed / tested / rejected / canonical

> Sleutels, tokens of secrets staan **nooit** in een kaart. Wel de *aard* van de auth
> ("vereist API-key in env"), nooit de waarde.

## Knowledge-kaart (`02_KNOWLEDGE/`)

Beantwoordt: "wat weten we over deze bron, en hoe helpt het ons?"

- **Titel**
- **Type** — github_repo / doc / course / video / post / case_study / pattern
- **Source URL**
- **Source owner / creator**
- **Datum toegevoegd**
- **Laatst gecheckt**
- **Samenvatting**
- **Wat het doet**
- **Praktisch nut**
- **Vereisten**
- **Moeilijkheid**
- **Trust level** — zie `SOURCE_TRUST_LEVELS.md`
- **Tags**
- **Gerelateerde capabilities** / **Gerelateerde knowledge-kaarten**
- **Risico's / limieten**
- **Volgende actie**
- **Completeness-status** + `OPEN:`-regel
- **Status** — unverified / reviewed / tested / rejected / canonical

## Naamgeving van kaartbestanden

`kebab-case.md`, beschrijvend, zonder datum in de naam (datum staat in de kaart).
Voorbeeld: `claude-code.md`, `elevenlabs-tts.md`, `dakkapel-pattern-organic-posts.md`.
