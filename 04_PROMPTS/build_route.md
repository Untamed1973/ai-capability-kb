# Prompt — Build-route bepalen (de router in actie)

> Doel: een vraag van Roel omzetten in de kortste veilige route + een executor-taak,
> volgens `00_SYSTEM/CAPABILITY_ROUTER.md`. Dit is de prompt die je dagelijks gebruikt.

## Gebruik

Lees eerst `CONTEXT_PACK.md`. Vul dan `VRAAG:` in.

---

VRAAG: <wat Roel wil bouwen / onderzoeken / automatiseren / maken>
PROJECT (indien van toepassing): <projectnaam, of "geen — algemeen">

Doorloop de zes stappen uit de router en geef je antwoord in deze vorm:

**1. Intentie** — in één zin: wat wil Roel echt?

**2. Beschikbare capabilities + relevante kennis** — wat vond je in `01_CAPABILITIES/` en
`02_KNOWLEDGE/` (vooral `patterns/` en `case_studies/`)? Noteer per capability de status.

**3. Routevergelijking** — als er meerdere wegen zijn, leg ze naast elkaar op de assen die
er voor déze vraag toe doen (kosten, gemak, kwaliteit, snelheid, grens-impact, lock-in).
Verberg de afweging niet.

**4. Aanbevolen route + autonomie-oordeel** — kies de kortste veilige route en spreek je
expliciet uit:
- **AUTONOOM** als de route schoon gaat naar een `tested`/`canonical` capability én binnen
  de veilige grens blijft.
- **STOP — VRAAG ROEL** als de capability onbekend/ongetest is, of de route schema, auth,
  RLS, migraties, `.env`, keys of destructieve operaties raakt.
Bij twijfel: STOP.

**5. Executor-taak** — een ready-to-paste prompt of command voor de gekozen executor
(Claude Code / Codex / GitHub Action). Concreet genoeg om direct te plakken.

**6. Terugleg-stap** — welke nieuwe kaart of pattern leg je na afloop terug, zodat de
bibliotheek groeit en deze route de volgende keer "bekend werk" is?

Als er géén passende capability of kennis is: zeg dat eerlijk, markeer de route als
onbekend (dus STOP — VRAAG ROEL), en stel voor wat er eerst onderzocht/bekaart moet worden.
