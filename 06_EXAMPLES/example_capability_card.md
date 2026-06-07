# Voorbeeld — capability-kaart

> Een ingevulde voorbeeldkaart die het schema demonstreert. Realistisch, maar bedoeld als
> illustratie — verifieer details vóór je dit als waarheid behandelt.

```
# Claude Code

- **Type:** executor
- **Wat het kan:** Voert codeer- en bestandsbewerkingstaken autonoom uit op de lokale
  machine vanaf de command line; kan een repo lezen, wijzigen, tests draaien en committen.
- **Wanneer te gebruiken (en wanneer niet):** Gebruiken voor het daadwerkelijk uitvoeren
  van bouw-/wijzigingstaken op de MacBook. Niet gebruiken als puur strategisch klankbord
  (dat is de architect-rol in de chat).
- **Inputs nodig:** Een ready-to-paste taak/prompt, toegang tot de repo, geldige
  projectconfig.
- **Outputs:** Codewijzigingen, bestanden, commits, testresultaten.
- **Beste executor:** Zichzelf (is de executor).

**Beslisvelden**
- Toegang & vorm (API/MCP/CLI/lokaal): CLI, lokaal op de MacBook.
- Kosten (prijsmodel + aard): valt onder Anthropic-abonnement/API-gebruik; let op
  token-spend bij lange autonome runs.
- Gebruiksgemak (kant-en-klaar/wat config/veel werk): kant-en-klaar na eenmalige setup.
- Kwaliteit / betrouwbaarheid: hoog voor afgebakende taken met heldere done-criteria.
- Snelheid: snel voor kleine taken; lange autonome runs kosten meer tijd en tokens.
- Grens-impact (raakt harde grens? waarom): JA bij schema/auth/RLS/migraties/.env/keys —
  die taken stoppen voor Roel, gehandhaafd via control-files in het project.
- Afhankelijkheden & lock-in: vereist de lokale install; werkt op de echte bestanden.

- **Risico's:** Token-spend bij onbewaakte runs; kan buiten scope treden zonder strakke
  done-criteria.
- **Voorbeeldgebruik:** "Maak de mappenstructuur X aan en commit met bericht Y."
- **Tags:** executor, lokaal, cli, coding
- **Gerelateerde capabilities:** codex (executor), github-action (executor)
- **Gerelateerde knowledge-kaarten:** —
- **Completeness-status:** compleet
- **Status:** canonical

OPEN: —
```
