# The Agency (msitarzewski/agency-agents)

- **Type:** github_repo
- **Source URL:** https://github.com/msitarzewski/agency-agents
- **Source owner / creator:** msitarzewski (Matt Sitarzewski)
- **Datum toegevoegd:** 2026-06-07
- **Laatst gecheckt:** 2026-06-07
- **Samenvatting:** Een groeiende verzameling kant-en-klare AI-agent-personas ("een compleet AI-bureau"), elk een specialist met eigen rol, werkwijze en voorbeeld-deliverables. Geen tool of framework, maar een set markdown-agentdefinities die je in een coding agent laadt.
- **Wat het doet:** Levert per discipline (engineering, frontend, marketing/Reddit, "reality checker", enz.) een agent-bestand met identiteit, missie, workflow en code-voorbeelden. Je installeert ze via `scripts/install.sh` naar bv. `~/.claude/agents/`, of kopieert losse bestanden. Een convert-script genereert varianten voor andere tools (Copilot, Gemini CLI, Cursor, Aider, Windsurf, Codex e.a.).
- **Praktisch nut:** Bruikbaar als startpunt/inspiratie voor het opzetten van eigen sub-agents en rolprompts — route "ik wil een gespecialiseerde agent voor taak X". Raakt de capability-categorie `agents`. Niet onmisbaar (personas zijn smaakgevoelig), maar het bespaart het from-scratch schrijven van rol- en workflowdefinities.
- **Vereisten:** Claude Code of een andere ondersteunde coding agent; installatie via shell-scripts (`install.sh`/`convert.sh`) of handmatig markdown kopiëren. Geen API-keys of externe diensten nodig.
- **Moeilijkheid:** Laag — kopiëren/installeren en activeren in de sessie.
- **Trust level:** primair (repo van de maker zelf)
- **Tags:** ai-agents, personas, claude-code, sub-agents, prompt-library, multi-tool
- **Gerelateerde capabilities:** — ontbreekt nog — (nog geen `agents`-capability-kaart aanwezig)
- **Gerelateerde knowledge-kaarten:** [[alirezarezvani-claude-skills]], [[travisvn-awesome-claude-skills]]
- **Risico's / limieten:** Persona-kwaliteit is subjectief en niet onafhankelijk geverifieerd; "production-ready/battle-tested" is een claim van de maker. Het zeer hoge ster-aantal voor een jonge repo is opvallend — gebruik als signaal, niet als bewijs van kwaliteit. Installatie draait shell-scripts: lees ze vóór uitvoeren.
- **Volgende actie:** Één agent-bestand handmatig inladen en in de praktijk beoordelen vóór we de kaart naar `tested` tillen.

### Bron-signalen (GitHub, per 2026-06-07)
- **Sterren:** 108.083
- **Forks:** 17.805
- **Open issues:** 63
- **Licentie:** MIT (SPDX: MIT)
- **Hoofdtaal:** Shell
- **Laatste activiteit (push):** 2026-06-06
- **Aangemaakt:** 2025-10-13
- **Gearchiveerd:** nee

- **Completeness-status:** gedeeltelijk
- **Status:** reviewed

OPEN: Gerelateerde capabilities
