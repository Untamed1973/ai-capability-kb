# Graphify (safishamsi/graphify)

- **Type:** github_repo
- **Source URL:** https://github.com/safishamsi/graphify
- **Source owner / creator:** safishamsi (Safi Shamsi)
- **Datum toegevoegd:** 2026-06-08
- **Laatst gecheckt:** 2026-06-08
- **Samenvatting:** Een AI-coding-assistant skill (slash-command `/graphify`) die een map met code, docs, schema's, papers of media omzet in één querybare knowledge graph. De assistent navigeert daarna die graph in plaats van bestanden één voor één te herlezen. Code blijft lokaal.
- **Wat het doet:** Bouwt via statische analyse + LLM-extractie een expliciete graph van entiteiten (functies, classes, concepten) en hun relaties (calls, imports, verwijzingen, afgeleide afhankelijkheden). De assistent beantwoordt vragen door de graph te doorlopen — dichter bij hoe een engineer een onbekende codebase navigeert dan bij fuzzy full-text zoeken. Output: interactieve HTML-graph, optioneel Obsidian-vault, Neo4j, GraphML, of een MCP-server die de graph als tools blootstelt.
- **Praktisch nut:** Voor het werken in een groeiende codebase (bv. ALLURE): de assistent hoeft niet elk bestand te herlezen om een vraag te beantwoorden, wat tokens en tijd bespaart. Onderscheidt zich van Obsidian: Obsidian visualiseert de links die jij met de hand legt tussen je KB-kaarten; Graphify ontdekt zélf de structuur ín de code die je niet handmatig hebt vastgelegd. Andere doelen, geen overlap.
- **Vereisten:** Een ondersteunde AI-coding-assistent (Claude Code: `/graphify`; Codex: `$graphify`; ook Cursor, Gemini CLI, OpenCode e.a.). Voor de volledige semantische graph is een LLM-laag nodig; een kalere AST-only graph kan zonder LLM. Code blijft lokaal — niets wordt verstuurd.
- **Moeilijkheid:** Laag tot midden — installeren per assistent met één commando, dan `/graphify` op een map draaien.
- **Trust level:** primair (repo van de maker zelf, geverifieerd via GitHub)
- **Tags:** knowledge-graph, codebase-navigatie, token-besparing, claude-code, codex, mcp, ast, skill
- **Gerelateerde capabilities:** — ontbreekt nog —
- **Gerelateerde knowledge-kaarten:** — ontbreekt nog —
- **Risico's / limieten:** Token-winst hangt sterk af van corpus-omvang en query-type: schaarse, structurele vragen winnen veel, brede conceptuele vragen weinig. Bij kleine of niet-code-mappen (zoals de platte-markdown KB) is de winst gering. De "71,5×"-claim komt uit de eigen voorbeelddata van het project — architectonisch plausibel, niet onafhankelijk geverifieerd. NAAMGEVING: de overdracht noteerde eerder een gelijknamig pip-pakket "Graphify" (`drcintas`, dubbele-y PyPI-naam) — dat is een ANDER project (andere eigenaar, andere vorm, pip i.p.v. assistant-skill), niet deze. Niet verwarren (OPERATING_PRINCIPLES §9); status van die andere tool niet geverifieerd.
- **Volgende actie:** Op één echte repo (ALLURE) draaien en de praktische token-/tijdwinst beoordelen vóór promotie naar `tested`.
- **Herzien wanneer:** zodra ALLURE merkbaar groeit of er token-druk ontstaat bij het werken in een project.
- **Wat zou dit bruikbaar maken:** bij grotere codebase-omvang kantelt de token-winst van structurele queries naar duidelijk voordeel; dan een echte run doen en meten.

### Bron-signalen (GitHub, per 2026-06-08)
- **Sterren:** ~22.000 (uitgebracht 3 april 2026, snel gegroeid)
- **Forks:** — ontbreekt nog —
- **Licentie:** MIT (SPDX: MIT)
- **Hoofdtaal:** — ontbreekt nog —
- **Laatste activiteit:** actief (recente commits per 2026-06-08)
- **Gearchiveerd:** nee

- **Completeness-status:** gedeeltelijk
- **Status:** reviewed

OPEN: Gerelateerde capabilities, Gerelateerde knowledge-kaarten, Forks, Hoofdtaal
