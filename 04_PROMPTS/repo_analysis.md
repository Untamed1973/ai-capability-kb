# Prompt — Repo-analyse → knowledge-kaart

> Doel: een GitHub-repo beoordelen en omzetten naar een knowledge-kaart (type
> `github_repo`), met een eerlijk oordeel over bruikbaarheid en risico's.

## Gebruik

Geef de repo-URL. Laat de executor de README, releases en recente activiteit lezen
(binnen `INGESTION_RULES.md`).

---

INPUT: <repo-URL>

Analyseer de repo en beantwoord, in eigen woorden:

1. **Wat doet het** — in twee zinnen.
2. **Praktisch nut voor ons** — voor welk doel/route zou dit bruikbaar zijn? Raakt het een
   bestaande capability of pattern?
3. **Volwassenheid & activiteit** — laatste release, recente commits, open issues-indruk,
   onderhouden of stil?
4. **Vereisten & afhankelijkheden** — taal, runtime, externe diensten/keys nodig?
5. **Licentie** — en de implicatie. Let op copyleft (bv. AGPL): privégebruik kan prima
   zijn, maar incorporeren in een te verkopen product kan het hele product open dwingen.
   Maak dit expliciet.
6. **Grens-impact** — vereist gebruik keys/auth/schema? → relevant voor autonoom vs. stop.
7. **Risico's / limieten** — eerlijk, ook schaalbaarheid (denk aan context-/tijdskosten).
8. **Oordeel** — adopteren / gedeeltelijk lenen (welk idee) / afwijzen, met reden.

Schrijf het resultaat als knowledge-kaart volgens `00_SYSTEM/CARD_SCHEMA.md`. Trust level
meestal `primair` (de repo van de maker). Status `unverified` tot we het draaiend zagen.
Sluit af met het voorgestelde pad `02_KNOWLEDGE/github_repos/<kebab-naam>.md` en een
`OPEN:`-regel.

Als de repo wordt afgewezen: maak alsnog een kaart met status `rejected` en leg de reden
vast — een afwijzing is een waardevolle les die we niet willen herhalen.
