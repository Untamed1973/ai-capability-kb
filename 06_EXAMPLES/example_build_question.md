# Voorbeeld — een build-vraag door de router

> Laat zien hoe de router (`04_PROMPTS/build_route.md`) een vraag omzet in een route met
> autonomie-oordeel. Illustratief; capabilities zijn voorbeelden.

---

**VRAAG:** "Ik wil onder een video automatisch ondertiteling genereren."
**PROJECT:** geen — algemeen

**1. Intentie**
Spraak in een bestaande video omzetten naar tekst-ondertiteling.

**2. Beschikbare capabilities + relevante kennis**
- `whisper` (cli_tool) — status `tested`. Lokale transcriptie.
- `elevenlabs`/transcriptie-API (api_service) — status `unverified`. Externe dienst.
- Pattern `video-ondertiteling` in `02_KNOWLEDGE/patterns/` — status `reviewed`.

**3. Routevergelijking**

| As | Whisper (lokaal) | Transcriptie-API |
|---|---|---|
| Kosten | gratis | per minuut |
| Snelheid | trager op grote files | snel |
| Gebruiksgemak | wat config | kant-en-klaar |
| Kwaliteit | goed | goed–zeer goed |
| Grens-impact | nee | JA (API-key in env) |
| Status | tested | unverified |

**4. Aanbevolen route + autonomie-oordeel**
Whisper lokaal. Het routeert naar een `tested` capability én raakt de harde grens niet.
→ **AUTONOOM.** (De API-route zou STOP — VRAAG ROEL zijn: key + ongetest.)

**5. Executor-taak (ready-to-paste)**
"Claude Code: gebruik de bestaande whisper-capability om `input.mp4` te transcriberen naar
`.srt`, volgens het pattern `video-ondertiteling`. Raak geen env/keys aan. Toon het
resultaat en commit niet automatisch."

**6. Terugleg-stap**
Werkt het schoon? Promoveer het pattern `video-ondertiteling` van `reviewed` naar `tested`
(bewuste beslissing) en noteer eventuele valkuilen op de pattern-kaart.
