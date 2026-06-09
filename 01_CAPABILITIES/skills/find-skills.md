# find-skills

- **Type:** skill
- **Wat het kan:** Meta-skill binnen de `vercel-labs/skills`-CLI. Triggert bij "is er een skill voor X", raadpleegt de skills.sh-leaderboard + `npx skills find`, stelt de beste skill voor en kan die installeren.
- **Wanneer te gebruiken (en wanneer niet):** Gebruik om te ontdekken of er al een bestaande SKILL.md-oplossing is voordat je zelf iets bouwt. **Niet** autonoom/'s nachts laten installeren — `npx skills add` hoort onder Roels hand (zie grens-impact).
- **Inputs nodig:** Een vraag/taakbeschrijving ("is er een skill voor X"). Voor installatie: een repo-URL + skill-naam.
- **Outputs:** Voorgestelde skill(s) met bron/score; optioneel een uitgevoerde installatie naar Claude Code / Codex / Cursor e.a.
- **Beste executor:** Claude Code (de skill draait in de agent-loop).

**Beslisvelden**
- Toegang & vorm (API/MCP/CLI/lokaal): CLI — `npx skills` (npm-stijl package manager), lokaal.
- Kosten (prijsmodel + aard): Gratis / open source (MIT). Telemetry standaard aan — uit via `DISABLE_TELEMETRY` of `DO_NOT_TRACK`.
- Gebruiksgemak (kant-en-klaar/wat config/veel werk): Kant-en-klaar via `npx`.
- Kwaliteit / betrouwbaarheid: Officiële vercel-labs org, ~17-21k stars, actief tot v1.5.1 (apr 2026). Ingebouwde bron-verificatie (install-count 1K+ prefereren, officiële bronnen, GitHub-stars) spiegelt OPERATING_PRINCIPLES §9 + SOURCE_VERIFICATION. Security-scan bij install (bron skills.sh): Gen = Safe, Socket = 0 alerts, Snyk = Med Risk. **Interpretatie (niet geverifieerd):** de Snyk-medium zit vrijwel zeker in een transitieve dependency van de skills-CLI, niet in de find-skills SKILL.md zelf (die is enkel tekst).
- Snelheid: Snel (npx-call + leaderboard-lookup).
- Grens-impact (raakt harde grens? waarom): **Ja.** `-g` installeert naar `~/.claude/skills/` = control-layer territory. De skill kan Claude Code aanzetten tot vervolg-`npx skills add`-calls = autonomie-vector. `add` hoort onder Roels hand, niet in autonome/nachtelijke runs.
- Afhankelijkheden & lock-in: Node/npx. Geen harde lock-in (skills zijn losse SKILL.md-bestanden). Install-methode was `copy` (geen symlink), dus updaten via `npx skills update -g` — niet automatisch via symlink-bron.

- **Risico's:** Autonome installatie-vector (zie grens-impact); telemetry standaard aan; globale install raakt control-layer.
- **Voorbeeldgebruik:**
  - Project-scope: `npx skills add https://github.com/vercel-labs/skills --skill find-skills`
  - Globaal: voeg `-g -a claude-code` toe.
- **Tags:** skills, package-manager, cli, vercel, claude-code, meta-skill, control-layer
- **Gerelateerde capabilities:** — ontbreekt nog —
- **Gerelateerde knowledge-kaarten:** — ontbreekt nog —

**Herzien wanneer:** nu globaal geïnstalleerd in `~/.claude/skills/` → allowlist-regel voor `npx skills` overwegen (en of `add` op ask/deny gaat). Of bij overstap naar multi-agent (Codex ook skills laten gebruiken). Eerste echte trigger op een taak → status naar `tested` tillen.

**Bron:** https://github.com/vercel-labs/skills · skill-pad `/skills/find-skills` · https://skills.sh/vercel-labs/skills/find-skills
**Geverifieerd:** 2026-06-09 — web-fetch repo + SKILL.md. Officiële vercel-labs org, geen malware-signaal.
**Geïnstalleerd:** 2026-06-09 — globaal via `npx skills add https://github.com/vercel-labs/skills --skill find-skills -g -a claude-code`. Pakket `skills@1.5.10`, locatie `~/.claude/skills/find-skills`, methode `copy`. Geïnstalleerd ≠ getest in actie: nog niet getriggerd op een echte taak.

- **Completeness-status:** compleet
- **Status:** reviewed
