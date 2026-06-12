# Decision Log

Waarom het systeem is zoals het is. Elke structurele wijziging hoort hier: nieuwe map,
nieuw veld, gewijzigde regel, aangepaste toolstrategie, of een capability die `canonical`
wordt. Een beslissing die nergens staat, bestaat over drie maanden niet meer.

Formaat: nieuwste bovenaan.

---

## 2026-06-12 — hormozi-skills geadopteerd als bevroren kopie

**Beslissing (Roel):** `alexsmedile/hormozi-skills` geadopteerd als **bevroren kopie** —
een eigen kopie in het project, geen levende dependency, geen updates verwacht. Doel:
fundament voor de offer-architectuurlaag (gratis weggever → Operator One).

**Voorwaarde:** de namen "Hormozi" en "Grand Slam Offer" zijn merk-/persoonsnamen — in
het eigen product hernoemen naar eigen taal. De methodiek is vrij, de naam niet.

**Licentie:** MIT repo-breed, geverifieerd (LICENSE-file integraal gelezen, inclusief
het recht op verkoop). Juridisch schoon voor commercieel hergebruik mits de
copyright-notice behouden blijft.

**Waarom bevroren en geen levende dependency:** de repo is zeer jong, heeft één
maintainer en de laatste push dateert van 2026-04-27 — er is geen onderhoud te
verwachten.

**Kaart:** `02_KNOWLEDGE/github_repos/alexsmedile-hormozi-skills.md`

## 2026-06-12 — sales-skills/sales geadopteerd via destillatie

**Beslissing (Roel):** de kennis uit `sales-skills/sales` (m.n. `sales-funnel` en
`sales-digital-products`) geadopteerd via **destillatie** — de methodiek herformuleren
in eigen woorden tot eigen kennismodules (patroon: zoals coreyhaines31 → .ts-modules).
**Nooit** verbatim bestanden meeleveren in een verkocht product.

**Waarom destillatie en niet kopiëren:** de repo heeft géén repo-brede LICENSE-file;
alleen de SKILL.md's declareren MIT in hun frontmatter, terwijl references-bestanden,
README en assets ongelicenseerd zijn. Te onduidelijk voor verbatim hergebruik in een
commercieel product. De funnelmodellen zelf zijn methodes/ideeën, geen beschermde tekst.

**Herzienbaar:** krijgt de repo alsnog een repo-brede LICENSE, dan wordt verbatim
hergebruik her-beoordeelbaar (zo ook vastgelegd op de kaart).

**Kaart:** `02_KNOWLEDGE/github_repos/sales-skills-sales.md`

---

## 2026-06-08 — Globale denylist uitgebreid met vier regels

**Beslissing:** aan de globale `~/.claude/settings.json` deny-array vier regels toegevoegd: `Bash(sudo:*)`, `Bash(chmod 777:*)`, `Bash(ssh:*)`, `Bash(*> /dev/*)`. Claude Code kan deze commando's nu in geen enkel project autonoom draaien.

**Aanleiding:** AgentShield-scan (zie ECC-kaart) gaf de eigen config grade B; de enige zwakke categorie was Permissions (50/100), met als bevinding dat deze vier gangbare gevaarlijke commando's niet geblokkeerd waren. De `sudo`-regel is direct relevant: een `sudo npm` had eerder de npm-cache vervuild (root-eigendom).

**Kanttekening:** de drie commando-prefixes (`sudo`, `chmod 777`, `ssh`) matchen hard; `*> /dev/*` (redirect) is zwakker omdat Claude Code's matching op commando-prefix werkt, niet op shell-redirects. De winst zit in de eerste drie.

**Scope:** alleen de globale autonomie-grens. Geldt voor elk project dat de globale config erft. Sluit aan op de bestaande deny-doctrine (deny wint altijd van allow).

## 2026-06-08 — Nieuw document: SOURCE_VERIFICATION.md

**Beslissing:** een bron-verificatierecept vastgelegd als eigen document in `00_SYSTEM/SOURCE_VERIFICATION.md`, met een verwijzing vanuit `CONTEXT_PACK.md` (leesvolgorde, regel 7). Het recept ordent de signalen van sterkst naar zwakst: bron zelf lezen, `is_fork`/network-root, eigenaar als anker, moeilijk-vervalsbare signalen, malware-rode-vlaggen, functie-match.

**Waarom:** het scheiden van origineel en kloon/malware en het herkennen van duplicaten kwam herhaaldelijk terug (de twee "Graphify"-projecten). De doctrine (§9) zegt dát identiteit = eigenaar + Source URL; dit document zegt hóé je dat verifieert. Als de lezende laag straks de KB raadpleegt vóór ze iets nieuws onderzoekt, hoort ze ook het verificatierecept te kennen.

**Scope:** puur instructie-document. Geen schema-wijziging, geen nieuwe status.

---

## 2026-06-08 — Doctrine: kaart-identiteit = bron, niet naam

**Beslissing:** vastgelegd als principe (`OPERATING_PRINCIPLES.md` §9) dat de identiteit
van een kaart de **eigenaar + Source URL** is, nooit de naam alleen. De router
(`CAPABILITY_ROUTER.md`, stap 4) is aangevuld: match nooit op naam alleen, en leg bij
gelijkende kandidaten beide voor met hun verschil.

**Aanleiding:** bij het aanmaken van een Graphify-kaart bleken er twee verschillende
projecten met de naam "Graphify" te bestaan — `safishamsi/graphify` (een assistant-skill,
uitgebracht april 2026) en een eerder in de overdracht genoteerd gelijknamig pip-pakket.
Verschillende eigenaar, verschillende vorm, verschillende functie. Een systeem dat op naam
matcht zou deze verwarren. Naarmate de bibliotheek groeit, nemen zulke botsingen toe.

**Bewust géén nieuw veld.** Overwogen is een `Verwar niet met`-veld. Afgewezen omdat
eigenaar en Source URL de identiteit al dragen; een extra veld zou de meeste kaarten leeg
belasten (tegen §5/§7). De doctrine stuurt de lezende laag; dat is voldoende. De
onderscheidende informatie staat al in de bestaande velden (owner, URL, "wat het doet") —
de doctrine zorgt dat de lezer ernaar kijkt in plaats van op de titel af te gaan.

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
