# Capability Router

De router vertaalt een vraag van Roel naar de kortste veilige route + een executeerbare
taak. Hij **matcht** niet alleen, hij **weegt**.

## Kernprincipe

> De gebruiker stelt een build-/research-/automatiserings-/media-/code-/workflow-vraag.
> Het systeem checkt capabilities, detecteert intentie, doorzoekt de kennis, matcht en
> weegt routes, stelt de kortste veilige route voor, en genereert een taak/prompt voor
> een executor (Codex, Claude Code, GitHub Action of een andere).

## De zes stappen

1. **Check beschikbare capabilities** — wat staat er in `01_CAPABILITIES/`? Welke handjes
   hebben we al?
2. **Detecteer intentie** — wat wil Roel echt? (bouwen / onderzoeken / automatiseren /
   media maken / coderen / een workflow draaien)
3. **Doorzoek de knowledge base** — wat weten we al? (`02_KNOWLEDGE/`, vooral `patterns/`
   voor bestaande bouwtekeningen en `case_studies/` voor eerdere uitkomsten)
4. **Match én weeg** — welke capabilities/agents/workflows passen, en hoe verhouden ze
   zich? Gebruik de beslisvelden (zie hieronder). Match nooit op naam alleen — namen kunnen
   botsen (zie `OPERATING_PRINCIPLES.md` §9). Lees eigenaar, URL en functie; bij twee
   gelijkende kandidaten leg je beide voor met hun verschil, in plaats van de eerste te
   kiezen.
5. **Stel de kortste veilige route voor** — inclusief het autonomie-oordeel.
6. **Genereer de taak/prompt** — ready-to-paste voor de gekozen executor.

## Het autonomie-oordeel (verplicht per verzoek)

De router spreekt zich expliciet uit:

- **AUTONOOM** — route gaat schoon naar een capability met status `tested`/`canonical`
  én blijft binnen de veilige grens. Geen goedkeuring nodig.
- **STOP — VRAAG ROEL** — onbekende/ongeteste capability, óf de route raakt schema, auth,
  RLS, migraties, `.env`, keys, of destructieve operaties.

Bij twijfel: STOP. (Zie `OPERATING_PRINCIPLES.md` §1–2.)

## Routes wegen — de beslisvelden

Wanneer meerdere wegen naar hetzelfde doel leiden, legt de router ze naast elkaar op
deze assen (bron: `CARD_SCHEMA.md`):

| As | Vraag |
|---|---|
| Toegang & vorm | API / MCP / CLI / lokaal — wat betekent dat voor sleutels en afhankelijkheid? |
| Kosten | Prijsmodel: gratis / per gebruik / abonnement / eenmalig — en de aard (per verzoek, per minuut, per maand)? |
| Gebruiksgemak | Kant-en-klaar / wat config / veel werk? |
| Kwaliteit / betrouwbaarheid | Hoe goed, en hoe zeker (gekoppeld aan status)? |
| Snelheid | Direct of traag? |
| Grens-impact | Raakt gebruik de harde grens? Bepaalt autonoom vs. stop. |
| Afhankelijkheden & lock-in | Wat is nodig vóór het werkt; hoe makkelijk stap je over? |

De router verbergt de afweging niet — hij maakt 'm zichtbaar. Voorbeeld van een
uitkomst: *"Voor dit doel zijn er drie capabilities. A is gratis maar traag en ongetest.
B kost per gebruik maar is `tested` en grens-veilig. C is het snelst maar zit aan een
sleutel (stopt voor Roel). Advies: B. Jij kiest."*

## Outputvorm van de router

1. **Intentie** (één zin)
2. **Gevonden capabilities + relevante kennis** (met status per capability)
3. **Routevergelijking** (de assen die ertoe doen voor deze vraag)
4. **Aanbevolen route + autonomie-oordeel**
5. **Executor-taak** (ready-to-paste prompt of command)
6. **Terugleg-stap** — welke nieuwe kaart/pattern leg je na afloop terug zodat de
   bibliotheek groeit?
