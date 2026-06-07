# Prompt — Capability-kaart aanmaken

> Doel: van een ruwe naam of URL naar een ingevulde capability-kaart in **~30 seconden**.
> Het schema is canoniek in `00_SYSTEM/CARD_SCHEMA.md` — deze prompt vult dat schema.
> Vul zoveel mogelijk; wat je niet zeker weet markeer je, je verzint niets.

## Gebruik

Plak deze prompt in je AI/executor en vul de regel `INPUT:` in. Dat is alles.

---

INPUT: <naam van de tool/dienst/agent, of een URL>
TYPE (indien bekend): <agent | skill | mcp_server | cli_tool | api_service | model | scraper | workflow | executor>

Je taak: maak een capability-kaart volgens `00_SYSTEM/CARD_SCHEMA.md`.

Regels:
- Vul elk veld dat je betrouwbaar kunt invullen.
- Wat je niet zeker weet: zet exact `— ontbreekt nog —`. Niet gissen, niet verzinnen.
- Vul de **beslisvelden** zo concreet mogelijk (kosten als prijsmodel, niet alleen "betaald";
  snelheid; gebruiksgemak als kant-en-klaar/wat config/veel werk; grens-impact ja/nee + waarom).
- Bepaal de **grens-impact**: raakt het gebruiken hiervan schema, auth, RLS, migraties,
  `.env` of keys? Zo ja → noteer dat, en weet dat gebruik voor Roel stopt.
- Zet **Status** op `unverified` tenzij expliciet anders opgegeven.
- Bepaal de **completeness-status** (`compleet`/`gedeeltelijk`/`kaal`) en sluit af met een
  `OPEN:`-regel die de lege velden opsomt.
- Zet **nooit** een sleutel/token/secret in de kaart — alleen de aard van de auth.
- Geef als laatste regel het voorgestelde bestandspad:
  `01_CAPABILITIES/<type-map>/<kebab-naam>.md`.

Output: alleen de kaart in markdown, plus de padregel. Geen uitleg eromheen.

---

### Lege kaart om te vullen

```
# <Capability-naam>

- **Type:** 
- **Wat het kan:** 
- **Wanneer te gebruiken (en wanneer niet):** 
- **Inputs nodig:** 
- **Outputs:** 
- **Beste executor:** 

**Beslisvelden**
- Toegang & vorm (API/MCP/CLI/lokaal): 
- Kosten (prijsmodel + aard): 
- Gebruiksgemak (kant-en-klaar/wat config/veel werk): 
- Kwaliteit / betrouwbaarheid: 
- Snelheid: 
- Grens-impact (raakt harde grens? waarom): 
- Afhankelijkheden & lock-in: 

- **Risico's:** 
- **Voorbeeldgebruik:** 
- **Tags:** 
- **Gerelateerde capabilities:** 
- **Gerelateerde knowledge-kaarten:** 
- **Completeness-status:** 
- **Status:** unverified

OPEN: <komma-gescheiden lijst van nog lege velden>
```
