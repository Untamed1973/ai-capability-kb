# Claude Code Skills & Plugins (alirezarezvani/claude-skills)

- **Type:** github_repo
- **Source URL:** https://github.com/alirezarezvani/claude-skills
- **Source owner / creator:** alirezarezvani (Alireza Rezvani)
- **Datum toegevoegd:** 2026-06-07
- **Laatst gecheckt:** 2026-06-07
- **Samenvatting:** Grote open-source bibliotheek van ~337 Claude Code skills, plus agents, personas en slash-commands, die ook werkt met andere coding agents (Codex, Gemini CLI, Cursor, Aider, Windsurf e.a.). Skills zijn herbruikbare expertise-pakketten die een coding agent domeinkennis geven die er standaard niet is.
- **Wat het doet:** Elk skill bevat een `SKILL.md` (instructies/workflow/beslisframeworks), optionele Python-CLI-tools (stdlib-only, geen pip-installs) en referentiedocs (templates/checklists). Dekt domeinen als engineering, DevOps, security (hooks), marketing, compliance, C-level-advisory-personas, research en productiviteit. Installatie per platform via clone + setup-script; `scripts/convert.sh` genereert varianten voor meer tools.
- **Praktisch nut:** Een grote grabbelton voor de route "is er al een skill voor X?" — bruikbaar als referentie en startpunt voor eigen skills. Raakt de capability-categorie `skills`. Vooral nut als we losse skills cherry-picken; de breedte (alles-in-één) maakt blind overnemen onverstandig.
- **Vereisten:** Claude Code of een ondersteunde coding agent; git clone + install-script per platform; Python voor de meegeleverde tools (stdlib-only, dus geen extra installs). Geen API-keys nodig voor de skills zelf.
- **Moeilijkheid:** Laag tot middel — installeren is simpel; de juiste skills uit de grote set kiezen en valideren kost werk.
- **Trust level:** primair (repo van de maker zelf)
- **Tags:** claude-skills, plugins, agent-skills, multi-tool, python-tools, prompt-library
- **Gerelateerde capabilities:** — ontbreekt nog — (nog geen `skills`-capability-kaart aanwezig)
- **Gerelateerde knowledge-kaarten:** [[travisvn-awesome-claude-skills]], [[msitarzewski-agency-agents]]
- **Risico's / limieten:** Aantallen en kwaliteitsclaims (337 skills, "production-ready", "SkillCheck Validated") komen van de maker en zijn niet onafhankelijk geverifieerd; de README noemt zelf "5.200+ stars" terwijl de API ~17.385 toont — claims dus per geval checken. Zeer brede scope betekent wisselende diepte per skill. Install-scripts draaien lokaal: lees ze vóór uitvoeren.
- **Volgende actie:** Eén relevante skill installeren en in de praktijk testen vóór we naar `tested` gaan.

### Bron-signalen (GitHub, per 2026-06-07)
- **Sterren:** 17.385
- **Forks:** 2.397
- **Open issues:** 12
- **Licentie:** MIT (SPDX: MIT)
- **Hoofdtaal:** Python
- **Laatste activiteit (push):** 2026-06-07
- **Aangemaakt:** 2025-10-19
- **Gearchiveerd:** nee

- **Completeness-status:** gedeeltelijk
- **Status:** reviewed

OPEN: Gerelateerde capabilities
