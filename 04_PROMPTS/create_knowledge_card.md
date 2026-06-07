# Prompt — Knowledge-kaart aanmaken

> Doel: van een URL of bron naar een ingevulde knowledge-kaart in **~30 seconden**.
> Het schema is canoniek in `00_SYSTEM/CARD_SCHEMA.md`. Respecteer `INGESTION_RULES.md`:
> samenvatten in eigen woorden, geen lange letterlijke overnames, geen paywalls omzeilen.

## Gebruik

Plak deze prompt en vul `INPUT:` in.

---

INPUT: <URL of bronbeschrijving>
TYPE (indien bekend): <github_repo | doc | course | video | post | case_study | pattern>

Je taak: maak een knowledge-kaart volgens `00_SYSTEM/CARD_SCHEMA.md`.

Regels:
- Vat samen in **eigen woorden**. Kopieer geen lange passages. Prefereer structuur en
  duiding boven citaten.
- Vul elk veld dat je betrouwbaar kunt invullen; onbekend = `— ontbreekt nog —`.
- Bepaal het **trust level** (`primair`/`betrouwbaar`/`community`/`onbekend`) volgens
  `SOURCE_TRUST_LEVELS.md`.
- Noteer **source URL**, **datum toegevoegd** (vandaag) en **laatst gecheckt** (vandaag).
- Geef bij **praktisch nut** concreet aan: voor welk soort vraag/route is dit bruikbaar,
  en welke capabilities raakt het?
- Zet **Status** op `unverified` tenzij anders opgegeven.
- Bepaal **completeness-status** en sluit af met een `OPEN:`-regel.
- Geef als laatste regel het voorgestelde pad:
  `02_KNOWLEDGE/<type-map>/<kebab-naam>.md`.

Output: alleen de kaart in markdown + de padregel.

---

### Lege kaart om te vullen

```
# <Titel>

- **Type:** 
- **Source URL:** 
- **Source owner / creator:** 
- **Datum toegevoegd:** 
- **Laatst gecheckt:** 
- **Samenvatting:** 
- **Wat het doet:** 
- **Praktisch nut:** 
- **Vereisten:** 
- **Moeilijkheid:** 
- **Trust level:** 
- **Tags:** 
- **Gerelateerde capabilities:** 
- **Gerelateerde knowledge-kaarten:** 
- **Risico's / limieten:** 
- **Volgende actie:** 
- **Completeness-status:** 
- **Status:** unverified

OPEN: <komma-gescheiden lijst van nog lege velden>
```
