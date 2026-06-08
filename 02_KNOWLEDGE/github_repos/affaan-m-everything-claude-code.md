# Everything Claude Code (affaan-m/everything-claude-code)

- **Type:** github_repo
- **Source URL:** https://github.com/affaan-m/everything-claude-code
- **Source owner / creator:** affaan-m (Affaan Mustafa)
- **Datum toegevoegd:** 2026-06-08
- **Laatst gecheckt:** 2026-06-08
- **Samenvatting:** Een "agent harness performance optimization system" — een compleet, kant-en-klaar pakket van skills, agents, rules, hooks, MCP-configs en security-scanning voor coding agents, cross-harness (Claude Code, Codex, Cursor, OpenCode, Gemini e.a.). Geen losse tool maar een heel ecosysteem, met een gratis OSS-kern (MIT) en een betaalde Pro-laag.
- **Wat het doet:** Levert een grote, onderhouden verzameling agent-configuratie als installeerbare plugin of handmatig te kopiëren onderdelen: tientallen sub-agents, ~180 skills, slash-commands, hook-runtime, taalspecifieke rules, en AgentShield (security-scanner). Eén config-bron die over meerdere AI-coding-tools tegelijk werkt.
- **Praktisch nut:** Voor Operator One beperkt — de aanpak hier is met-de-hand en frictieloos (eigen allowlist, eigen Codex-debugger zijn al zo gebouwd). ECC als geheel adopteren botst met "frictieloos, selectief" (OPERATING_PRINCIPLES §7): het is groot, breed, en dupliceert wat zelf-gebouwd is. Het potentieel bruikbare losse stuk is AgentShield (zie Risico's/Volgende actie).
- **Vereisten:** Claude Code v2.1+ (of een andere ondersteunde harness). Installatie via plugin-marketplace of handmatig kopiëren van onderdelen. Geen verplichte API-keys voor de OSS-kern; Pro-laag en GitHub App vereisen account/betaling.
- **Moeilijkheid:** Midden tot hoog — niet de tool zelf, maar het selectief installeren zonder de hele context binnen te halen. README waarschuwt expliciet tegen het stapelen van install-methodes (dubbele skills/hooks).
- **Trust level:** primair (repo van de maker zelf, geverifieerd via GitHub-metadata: geen fork, eigen network-root)
- **Tags:** claude-code, agent-harness, skills, hooks, agents, cross-harness, security-scan, codex, cursor, opencode
- **Gerelateerde capabilities:** — ontbreekt nog —
- **Gerelateerde knowledge-kaarten:** [[msitarzewski-agency-agents]], [[alirezarezvani-claude-skills]], [[travisvn-awesome-claude-skills]]
- **Risico's / limieten:** Te groot/breed voor de frictieloze aanpak; adopteren-als-geheel dupliceert zelf-gebouwde laag. Pro-tier ($19/seat/mo) is een betaalde laag bovenop de OSS-kern. NAAMGEVING/VEILIGHEID: het origineel is `affaan-m/everything-claude-code` (ook bereikbaar als `affaan-m/ECC` — zelfde repo, hernoeming). De overdracht noteerde een namaak/malware-kloon `arabicapp/everything-claude-code`; NIET opnieuw geverifieerd op 2026-06-08. Regel: vertrouw op de eigenaar `affaan-m`, niet op de losse reponaam — gelijknamige repos onder andere eigenaren kunnen kwaadaardig zijn (zie OPERATING_PRINCIPLES §9).
- **Volgende actie:** geen openstaande — AgentShield is beproefd (2026-06-08). Oordeel: bruikbaar als incidentele check, niet als vaste tool. Draait read-only via `npx ecc-agentshield scan --path ~/.claude` zonder installatie. Resultaat op de eigen globale config: grade B (87/100); Secrets/Hooks/MCP 100, Permissions 50 — leidde tot vier extra denyregels (`sudo`, `chmod 777`, `ssh`, `> /dev/`). NB: AgentShield is van dezelfde maker als ECC, dus geen onafhankelijke audit. Niet adopteren: geen install, geen `--fix` (raakt config aan), geen Pro.
- **Herzien wanneer:** bij een volgende grote wijziging aan allowlist/hooks/MCP — dan de scan opnieuw draaien als verificatie.
- **Wat zou dit bruikbaar maken:** AgentShield zélf is nu bruikbaar bevonden als losse scan. De rest van ECC blijft geparkeerd; zou pas kantelen als de zelf-gebouwde laag (allowlist/debugger) tekortschiet en ECC's bredere onderdelen een gat vullen.

### Bron-signalen (GitHub, per 2026-06-08)
- **Sterren:** ~178.000 (pagina-header; README-tekst loopt achter op ~140k)
- **Forks:** ~27.500
- **Commits:** 1.553
- **Licentie:** MIT (SPDX: MIT)
- **Hoofdtaal:** Shell / TypeScript / Python (multi)
- **Laatste activiteit:** actief, wekelijkse releases (v2.0.0-rc.1, apr 2026)
- **Gearchiveerd:** nee

- **Completeness-status:** gedeeltelijk
- **Status:** reviewed

OPEN: Gerelateerde capabilities
