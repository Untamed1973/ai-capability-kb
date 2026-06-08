# Decision Log

Waarom het systeem is zoals het is. Elke structurele wijziging hoort hier: nieuwe map,
nieuw veld, gewijzigde regel, aangepaste toolstrategie, of een capability die `canonical`
wordt. Een beslissing die nergens staat, bestaat over drie maanden niet meer.

Formaat: nieuwste bovenaan.

---

## 2026-06-08 — Knowledge-kaart: twee herzieningsvelden toegevoegd

**Beslissing:** aan de knowledge-kaart in `CARD_SCHEMA.md` twee velden toegevoegd, direct
ná "Volgende actie": **Herzien wanneer** en **Wat zou dit bruikbaar maken**.

**Waarom:** bronnen die om een tijdelijke of contextafhankelijke reden afvielen (bv. een
tool die nu te groot is, maar bij groei kantelt) mogen niet als `rejected` weggeschreven
worden — dat is een definitief oordeel. Ze horen "geparkeerd, herzienbaar" te zijn. De
twee velden scheiden het bron-oordeel (status: wat we er nú van vinden) van het
herzieningssignaal (wanneer en waarom opnieuw kijken), zodat een bron `reviewed` kan
blijven mét een expliciet moment en drempel om terug te komen.

**Onderscheid tussen de twee:**
- *Herzien wanneer* = het **wanneer** (tijdstip of trigger).
- *Wat zou dit bruikbaar maken* = het **wat** (welke verandering de bron de moeite waard
  maakt).

**Scope:** alleen de knowledge-kaart. De statustabel is bewust niet gewijzigd; "geparkeerd,
herzienbaar" wordt nu gedragen door status `reviewed` + ingevulde herzieningsvelden, niet
door een nieuwe status.

## 2025 — Oprichting van de AI Capability KB

**Beslissing:** een project-agnostische kennis- en capability-bank bouwen als standalone
repo (`ai-capability-kb`), boven elk project, met platte markdown + git als waarheid.

**Waarom:** bestaande kennis (o.a. een ad-hoc skills-map) leefde verspreid en raakte
veroudert. Een levende, doorzoekbare laag laat elk project de nieuwste skills en tools
hergebruiken, en laat elke nieuwe AI-chat direct op de hoogte zijn.

**Vastgelegde keuzes in deze oprichting:**

1. **Skills-map wordt geabsorbeerd.** `01_CAPABILITIES/skills/` wordt de levende,
   canonieke thuisbasis. `OPERATOR_ONE_SKILLS_MAP.md` is gemarkeerd als "te migreren";
   nog niet verwijderd.
2. **Autonomie-doctrine.** `tested`/`canonical` + binnen de veilige grens = autonoom; al
   het andere stopt voor Roel. De bibliotheek bepaalt wat "bekend werk" is.
3. **`CONTEXT_PACK.md`** als AI-ingang naast `README.md` (mens-ingang). Lost de pijn op
   van "elke nieuwe chat alles opnieuw uitleggen".
4. **`api_services/`** toegevoegd aan capabilities — externe diensten-met-sleutel (FAL,
   ElevenLabs, Kling, model-API's, enz.) pasten nergens schoon.
5. **Beslisvelden** op elke capability-kaart (toegang, kosten, gemak, kwaliteit, snelheid,
   grens-impact, lock-in) zodat de router routes kan *wegen*, niet alleen matchen.
6. **Completeness i.p.v. verplichte velden.** Een leeg veld is een taak, geen fout.
7. **Schema-uitbreiding met de hand**, stopt voor Roel; later te herzien als er een
   betere aanpak langskomt.
8. **`CARD_SCHEMA.md`** als enige bron van waarheid voor de kaartvelden (voorkomt dat het
   schema verspreid in prompts gaat leven).
9. **Review-queue als gegenereerde view, niet als map.** Status is een eigenschap van de
   kaart; kaarten verhuizen niet tussen mappen. Idem voor de verrijkingslijst.
10. **Cockpit is een latere horizon** (laag 1 = read-only kaart; laag 2 = operate-app).
    Geen eigen chatvenster — kaart + startknop naar bestaande tools.
11. **Toolstrategie:** markdown + git = fundament; Obsidian/NotebookLM = optionele lenzen;
    Graphify blijft afgewezen.

**Status van placeholders:** `03_INDEX/embeddings/`, de nightly-update en `05_SCRIPTS/`
zijn bewust nog niet werkend — er is geen executor-laag aan gekoppeld. Duidelijk gelabeld.
