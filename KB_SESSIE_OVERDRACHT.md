# AI CAPABILITY KB — INSTRUCTIE VOLGENDE SESSIE

Plak dit aan het begin van een nieuwe chat. Dit is een instructie, geen verslag.
Twee delen: VAST (beslist — niet heroverwegen) en TE DOEN (taken). Behandel VAST als feit.

Repo: `Untamed1973/ai-capability-kb`, branch `main`. Lokaal: `~/Downloads/ai-capability-kb`.
Laatste push: `a72df2e`. Roel is niet-technisch; Claude = architect, Claude Code = executor.

Werkwijze deze sessies: Roel plakt terminal-output, Claude geeft ready-to-paste commando's.
Bestanden worden geschreven via `cat > … << 'EOF'` of via een Python-snippet met anker-check
(controleert dat de ankertekst exact 1x voorkomt vóór het schrijft — veilig, geen blind
overschrijven). Altijd back-up vóór wijzigen, JSON/inhoud valideren ná schrijven, dan pas
committen. Push doet Roel zelf.

---

## DEEL 1 — VAST (beslist, niet heroverwegen)

### KB-fundament (ongewijzigd)
- De KB is een standalone repo, project-agnostisch, staat boven elk project.
- Waarheid = platte markdown + git. Obsidian/NotebookLM alleen als lens, nooit als fundament.
- Twee databases: `01_CAPABILITIES/` en `02_KNOWLEDGE/`.
- `README.md` = voor mensen. `CONTEXT_PACK.md` = voor AI, wordt als eerste gelezen.
- `00_SYSTEM/CARD_SCHEMA.md` = enige bron van waarheid voor kaartvelden.
  `00_SYSTEM/DECISION_LOG.md` = log van elke structurele wijziging.
- `00_SYSTEM/OPERATING_PRINCIPLES.md` = de doctrine. `00_SYSTEM/CAPABILITY_ROUTER.md` = de
  router die vraag → kortste veilige route + executor-taak vertaalt.
- Autonomie-doctrine: een taak mag autonoom als hij schoon routeert naar een capability met
  status `tested`/`canonical` EN binnen de veilige grens valt. Al het andere stopt voor Roel.
- Harde grens (stopt altijd, ook als AI's het eens zijn): databaseschema, migraties, auth,
  RLS, `.env`, keys/secrets, destructieve operaties. Bij git: `push`, `--force`,
  `reset --hard` stoppen voor Roel.
- Bibliotheek mag royaal en groot: geen testdrempel om iets op te nemen. Status = drempel
  voor autonoom uitvoeren, niet voor bestaansrecht.
- Schema-uitbreiding gebeurt met de hand, als bewuste beslissing, gelogd in DECISION_LOG.
- `rejected` NIET gebruiken voor bronnen die om een tijdelijke reden afvielen. Die worden
  "geparkeerd, herzienbaar": status blijft `reviewed` + ingevulde herzieningsvelden.
- Cockpit-volgorde (beslist): eerst Obsidian op de vault, dan laag 1 (read-only overzicht op
  de markdown), dan laag 2 op afroep (opereren/aansturen — raakt de grens). Geen eigen
  chatvenster; cockpit = kaart + startknop naar bestaande tools.

### Globale autonomie-infrastructuur (NIEUW deze sessie — geldt voor ELK project)
- **Globale allowlist** staat in `~/.claude/settings.json`. Eén keer ingesteld, elk project
  erft 'm. Toegestaan: veilige reads (`cat`/`ls`/`grep`/`find`/`pwd`), git-reads,
  `git add`, `git commit`. Geweigerd (deny wint altijd): `git push`, `reset --hard`,
  `--force`/`-f`, `branch -d/-D`, `git rm`, `rm -rf`, `supabase db push`,
  `supabase migration`, en lezen van `.env`/secrets/credentials.
- **Codex-debugger is globaal.** Scripts staan in `~/.claude/scripts/`
  (`debug-escalate.sh` + `debug-boundary-check.sh`), de `PostToolUseFailure`-hook in
  `~/.claude/settings.json` wijst daarheen. Werking ONGEWIJZIGD t.o.v. de ALLURE-versie:
  bij de 3e dezelfde Bash-fout wordt Codex (`codex exec`, lees-sandbox) ingeroepen, die een
  fix VOORSTELT (nooit toepast) met label `BOUNDARY:SAFE`/`ARCH`; de grens-check blokkeert
  ARCH/db/auth. End-to-end getest in de KB-repo (buiten ALLURE) — werkt.
- ALLURE's lokale debugger-hook is VERWIJDERD (draaide anders dubbel). ALLURE's
  project-`settings.json` houdt zijn eigen git-deny + npm-allow + niets meer over Supabase
  (die deny staat nu globaal). ALLURE's `settings.local.json` is opgeschoond: brede
  wildcards `git *` en `curl *` vervangen door veilige varianten.
- Precedentie-feit (geverifieerd): voor permissions wint deny altijd van allow, ook over
  scopes heen; arrays mergen over scopes. `/config` toont de effectieve merged config.

### Doctrine kaart-identiteit (NIEUW deze sessie)
- **Kaart-identiteit = eigenaar + Source URL, nooit de naam alleen.** Vastgelegd als
  `OPERATING_PRINCIPLES.md` §9 + één regel in `CAPABILITY_ROUTER.md` stap 4. Namen botsen
  (twee verschillende "Graphify"-projecten bewezen dat). De lezende laag (Codex/Claude Code)
  matcht nooit op titel alleen; bij gelijkende kandidaten worden beide voorgelegd met hun
  verschil, niet samengevouwen. Bewust GEEN extra veld toegevoegd — owner+URL+functie dragen
  de identiteit al; een veld zou de meeste kaarten leeg belasten.

### Schema (NIEUW deze sessie)
- Knowledge-kaart heeft twee extra velden, direct ná "Volgende actie": **Herzien wanneer**
  (het moment/de trigger) en **Wat zou dit bruikbaar maken** (de drempel). Gelogd in
  DECISION_LOG. Scheidt bron-status (wat we ervan vinden) van herzieningssignaal (wanneer
  opnieuw kijken).

---

## DEEL 2 — STATUS (af, staat op GitHub)

- Fundament gebouwd en gepusht: volledige structuur, alle markdown gevuld, placeholders
  gelabeld (`embeddings/`, nightly, `05_SCRIPTS/`).
- Skills-map geabsorbeerd als index: `01_CAPABILITIES/skills/operator-one-skills-map.md`.
- github_repo-kaarten met geverifieerde signalen, eerder gemaakt: anthropics/skills,
  obra/superpowers, ComposioHQ/awesome-claude-skills, tinyhumansai/openhuman,
  grandamenium/dream-skill, msitarzewski/agency-agents, alirezarezvani/claude-skills,
  travisvn/awesome-claude-skills. Pattern-kaart: tokenjuice-compressie.
- **Allowlist + Codex-debugger globaal gemaakt en bewezen** (zie DEEL 1). Commits in
  allure-os: `49f153c` (allowlist), `fe6bb8f` (debugger-hook globaal, lokale verwijderd).
- **Schema uitgebreid** met twee herzieningsvelden (KB commit `1e3130e`).
- **Doctrine kaart-identiteit** vastgelegd (KB commit `cc28c39`).
- **Twee nieuwe knowledge-kaarten** (KB commit `a72df2e`):
  - `affaan-m-everything-claude-code.md` — ECC. Origineel geverifieerd via GitHub-metadata
    (geen fork, eigen network-root). MIT, ~178k sterren, Pro-tier $19/seat/mo. Status
    `reviewed`, geparkeerd. Herzien: AgentShield (`npx ecc-agentshield scan`, geen install)
    los beproeven als check op de allowlist bij de volgende settings-sessie.
  - `safishamsi-graphify.md` — Graphify, een assistant-skill (`/graphify`), NIET het oude
    pip-pakket uit de vorige overdracht (dat was een ander gelijknamig project). MIT, ~22k,
    uitgebracht apr 2026. Status `reviewed`. Te beproeven op een echte repo (ALLURE).

---

## DEEL 3 — TE DOEN (volgende sessie, in volgorde)

### Taak A — Verificatie-recept als KB-document (NIEUW, aanbevolen eerst)
Kwam sterk naar boven deze sessie: hoe scheid je origineel van kloon/malware, en hoe herken
je duplicaten. Leg dit vast als eigen document in `00_SYSTEM/` (bv. `SOURCE_VERIFICATION.md`),
gelogd in DECISION_LOG. Het recept (van sterkst naar zwakst signaal):
1. Lees de GitHub-pagina ZELF, nooit alleen een artikel erover (artikelen geven verouderde/
   opgeklopte cijfers).
2. Check `is_fork: false` en of de repo zijn eigen network-root is (repository_id ==
   network_root_id) — origineel, geen kopie.
3. De EIGENAAR is het anker, niet de reponaam (namen zijn vrij te kiezen). Verifieer de maker
   via een onafhankelijk kanaal.
4. Vergelijk moeilijk-te-vervalsen signalen: aanmaakdatum, commit-historie, contributors,
   issue/PR-activiteit. Verse kloon = lege historie.
5. Malware-rode-vlaggen: stuurt naar "download de release" i.p.v. broncode; ongezien-uit-te-
   voeren install-scripts; identieke naam onder onbekende eigenaar; nauwelijks historie.
6. Match op FUNCTIE (beschrijving + wat het doet + vorm), niet op naam — sluit aan op §9.
Sluit aan op Taak C: als Claude Code de KB gaat raadplegen, hoort hij ook te weten hóé hij
bronnen verifieert.

### Taak B — Allowlist-randpunten (los, klein)
- Claude Code vroeg in de KB-repo om toestemming voor `ls`/`cat` ondanks de globale allow.
  Vermoeden: Claude Code vraagt alsnog bij commando's met een absoluut pad buiten het project
  (veiligheidsgedrag). Niet kritiek, maar uitzoeken of dit te versoepelen is voor het normale
  werk. Eerst diagnose (waarom vraagt hij), dan pas iets aanpassen.
- AgentShield draaien als check op de globale allowlist/hooks (`npx ecc-agentshield scan`,
  geen install) — beoordeel of het waarde toevoegt. Hangt aan de ECC-kaart.

### Taak C — KB koppelen aan lopende projecten (frictieloos, automatisch)
Doel: Claude Code raadpleegt in elk project automatisch eerst de KB voordat hij iets nieuws
onderzoekt of bouwt.
- Voeg aan ALLURE's control-file (`AGENTS.md`/`CLAUDE.md`) een instructie toe: "Voordat je
  een tool/aanpak/patroon onderzoekt of bouwt: raadpleeg eerst de AI Capability KB op pad X.
  Bestaat er al een kaart/pattern/beoordeelde bron? Gebruik die. Pas als de KB niets heeft,
  onderzoek je nieuw — en leg je bevinding terug als kaart." (Terugleg-zin sluit de lus.)
- LET OP: wijzigt control-files van een draaiend project. Via Claude Code in de allure-os
  repo, review + push door Roel. Tekst voorstellen mag Claude; uitvoeren doet Roel.
- Praktisch: Claude Code moet beide repos tegelijk kunnen zien (KB + allure-os als buurmappen).
- Tot dit staat: geef bij een nieuwe Operator One-chat naast `OPERATOR_ONE_MASTER.md` ook
  `CONTEXT_PACK.md` mee.

### Taak D — Cockpit (in deze volgorde, niet eerder)
1. Obsidian op de vault (`ai-capability-kb` als vault openen). Eerst zien wat dat aan
   overzicht/graph geeft. Optioneel: `Gerelateerde`-velden → `[[wikilinks]]`.
2. Laag 1: read-only overzicht dat de markdown uitleest (kaarten, status, vullingsgraad,
   working tree per project). Veilig, raakt de grens niet.
3. Laag 2 op afroep: opereren/aansturen (projecten starten, executors). Raakt keys/auth/
   backend → grens-werk, latere bouw.

### Daarna (later)
- "Verrijk alles": marketing-skills (secties 1–17 van de skills-map) per stuk bekaarten
  wanneer ze gebruikt worden; API's/MCP's/SaaS volgen als nieuwe kaarten.
- Nachtelijk-autonoom via Codex: eerst Roels drie punten afvinken (debugger op echte bug
  testen, review-vs-autonomie, token-spend-bewaking). NB: de debugger is deze sessie
  globaal gemaakt en op een geforceerde fout getest, maar nog niet op een ECHTE bug in een
  echt project.

---

## DEEL 4 — WERKWIJZE (zo werkt Roel)
- Nederlands, direct, bondig. Eén beslissing per keer, geen gebundelde opties.
- Done-criteria vóór bouwen. Altijd ready-to-paste prompts/commands, nooit alleen beschrijving.
- Geen commentaar (`# ...`) achter een shell-commando — dat breekt de regel.
- Git-push doet Roel in de gewone terminal, niet in Claude Code.
- Beoordeel Claude Code's werk op de GECOMMITTE bestanden, niet op streaming-previews.
- Niet gokken, niet te snel oordelen. Roel let er expliciet op dat Claude in sommige chats te
  snel concludeert — eerst de bron zelf lezen/verifiëren, dan pas stellen.
- Een eerdere overdracht/notitie is GEEN onbetwistbaar feit: hij kan uit een vroegere
  denkfase stammen. Toets bron-gegevens (eigenaar, cijfers, vorm) opnieuw aan de echte bron.
