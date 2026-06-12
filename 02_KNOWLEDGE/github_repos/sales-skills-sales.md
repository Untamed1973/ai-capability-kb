# Sales Skills — funnel & digital products (sales-skills/sales)

- **Type:** github_repo
- **Source URL:** https://github.com/sales-skills/sales
- **Source owner / creator:** sales-skills (committer "Gary")
- **Datum toegevoegd:** 2026-06-12
- **Laatst gecheckt:** 2026-06-12
- **Samenvatting:** Grote skill-bibliotheek (538 skills, SKILL.md-formaat) voor sales/marketing/GTM. Voor de operator-laag zijn twee skills inhoudelijk geverifieerd op 12 juni 2026 door ze volledig te lezen: `sales-funnel` en `sales-digital-products`. Dekking: discipline 3 (funnel) sterk, discipline 4 (upsell/OTO) sterk, discipline 1 (offer) gedeeltelijk.
- **Wat het doet:** `sales-funnel` (329 regels) is volwaardig: 8 funneltypen met stappenflows, benchmark-tabellen, salespagina-blauwdruk (11 elementen), OTO-ontwerp met prijsregel (upsell 30–60% van core offer), A/B-methodologie en troubleshooting per symptoom. `sales-digital-products` (166 regels) is gedeeltelijk: sterk validatie-playbook (pre-sell: 10+ betalers = bouwen; waitlist: 100+ signups = sterk signaal), producttype-menu en losse prijsregels; de transformatielogica expertise→product is dunner dan bij hormozi-offer. E-mailsequentie-inhoud zit bewust in de zusterskill `sales-email-marketing` (niet gelezen).
- **Praktisch nut:** Kennisbron voor de funnel-laag van de chatbot-operator (weggever → micro-product → hoofdaanbod). Beslissing (12 juni 2026, Roel): **kennis geadopteerd via destillatie** — methodiek herformuleren in eigen woorden tot eigen kennismodules (patroon: zoals coreyhaines31-skills → .ts-modules). NOOIT verbatim bestanden meeleveren in een verkocht product, vanwege de ontbrekende repo-brede licentie. De funnelmodellen zelf zijn methodes/ideeën, geen beschermde tekst (PLF is expliciet Jeff Walkers model).
- **Vereisten:** Geen voor het lezen — pure markdown. Installatie als skill kan via `npx skills add sales-skills/sales`, maar dat is voor de destillatie-route niet nodig.
- **Moeilijkheid:** Middel — de methodiek is concreet en direct bruikbaar, maar destillatie naar eigen modules is bewust handwerk.
- **Trust level:** primair (repo van de maker zelf; inhoud direct gelezen, niet alleen README)
- **Tags:** sales-funnel, digital-products, upsell-oto, tripwire, lead-magnet, validatie, skill-md, operator-laag, destillatie
- **Gerelateerde capabilities:** — ontbreekt nog —
- **Gerelateerde knowledge-kaarten:** [[alexsmedile-hormozi-skills]], [[alirezarezvani-claude-skills]]
- **Risico's / limieten:** GEEN repo-brede LICENSE-file (GitHub /license-endpoint geeft 404). Elke gelezen SKILL.md declareert wel `license: MIT` in de frontmatter (regel 5, geverifieerd in beide skills), maar references-bestanden, README en assets hebben géén licentieverklaring — status ongedefinieerd. Daarom alleen destillatie, geen verbatim hergebruik. Single maintainer ("Gary"), jong (2026-03-23). Platform-promotionele inslag: Groove.cm en Systeme.io worden herhaald aanbevolen; de methodiek zelf is daar niet van afhankelijk.
- **Volgende actie:** Destillatie-ronde: `sales-funnel` en `sales-digital-products` herformuleren tot eigen kennismodules; daarbij beoordelen of zusterskill `sales-email-marketing` ook gelezen moet worden voor de sequentie-inhoud.
- **Herzien wanneer:** bij de destillatie-ronde, of als de repo alsnog een repo-brede LICENSE krijgt (dan wordt verbatim hergebruik her-beoordeelbaar).
- **Wat zou dit bruikbaar maken:** n.v.t. voor de kennis (reeds bruikbaar via destillatie); voor verbatim hergebruik: een repo-brede LICENSE of expliciete bevestiging van de auteur.
- **Verwijzing:** volledig onderzoeksrapport in de allure-os repo, `13_DOCS/offer-layer-open-sources-research.md`

### Licentie (geverifieerd 2026-06-12)
Geen repo-brede LICENSE-file (root bevat alleen README, package.json, skills/, assets; /license-endpoint 404). Per-skill frontmatter: `license: MIT` in beide gelezen SKILL.md's. References-bestanden (`references/platforms.md`, `references/platform-guide.md`) waarop de skills leunen zijn ongelicenseerd. Conclusie: niet schoon genoeg voor verbatim meeleveren in een commercieel product; destillatie van de methodiek wel.

### Bron-signalen (GitHub, per 2026-06-12)
- **Sterren:** 46
- **Forks:** 4
- **Open issues:** 1
- **Licentie:** geen (API: None; per-skill MIT-frontmatter)
- **Hoofdtaal:** geen (API: None — pure markdown)
- **Laatste activiteit (push):** 2026-06-06
- **Aangemaakt:** 2026-03-23
- **Gearchiveerd:** nee

- **Completeness-status:** — ontbreekt nog —
- **Status:** unverified

OPEN: Gerelateerde capabilities, Completeness-status
