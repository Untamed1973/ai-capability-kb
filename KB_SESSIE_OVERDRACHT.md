# AI CAPABILITY KB — INSTRUCTIE VOLGENDE SESSIE

Plak dit aan het begin van een nieuwe chat. Dit is een instructie, geen verslag.
Twee delen: VAST (beslist — niet heroverwegen) en TE DOEN (taken). Behandel VAST als feit.

Repo: `Untamed1973/ai-capability-kb`, branch `main`. Lokaal: `~/dev/kb`.
Roel is niet-technisch; Claude = architect, Claude Code = executor.

Oproepen voor de volgende sessie: `cat ~/dev/kb/KB_SESSIE_OVERDRACHT.md` → kopiëren → plakken.

Werkwijze deze sessies: Roel plakt terminal-output, Claude geeft ready-to-paste commando's.
Voor live control-files in een draaiende repo (AGENTS.md, MASTER.md): schrijven via een
Python-snippet met anker-check (ankertekst moet exact 1x voorkomen vóór het schrijft — veilig,
geen blind overschrijven), back-up vóór, valideren ná, dan committen. Push doet Roel zelf.
Voor dit overdrachtsbestand zelf: Claude herschrijft het compleet en levert het als download;
Roel sleept het naar de juiste map. Geen anker-gedoe voor een bestand dat toch met de hand
rondgaat.

---

## DEEL 1 — VAST (beslist, niet heroverwegen)

### Mappenstructuur (geldt voor ALLES)
- Thuisbasis voor alle code-projecten: `~/dev/`. Daaronder als buurmappen:
  `~/dev/kb` (deze KB), `~/dev/allure` (ALLURE/Operator One), `~/dev/operator-one`
  (leeg, gereserveerd voor de latere standalone SaaS).
- Reden: de KB staat project-agnostisch bóven de projecten, maar moet als buurmap naast ze
  staan zodat Claude Code (gestart vanuit `~/dev`) KB + projecten tegelijk ziet. Dat lost het
  toestemming-vraaggedrag op (zie B1 hieronder).
- Naamkeuze `dev` (niet `projects`) bewust: `~/.claude/projects` bestaat al als interne map
  van Claude Code; een eigen `~/projects` zou verwarren.
- Start-conventie: gewone terminal opent in `~`, navigeer met `cd ~/dev/kb` of `cd ~/dev/allure`.
  Claude Code voor KB-werk: start vanuit `~/dev` (ziet dan beide repos). Voor puur ALLURE-werk
  mag vanuit `~/dev/allure`. De twee terminalvensters (gewone shell + Claude Code) zijn losse
  processen, weten niets van elkaar.

### KB-fundament (ongewijzigd)
- De KB is een standalone repo, project-agnostisch, staat boven elk project.
- Waarheid = platte markdown + git. Obsidian/NotebookLM alleen als lens, nooit als fundament.
- Twee databases: `01_CAPABILITIES/` en `02_KNOWLEDGE/`.
- `README.md` = voor mensen. `CONTEXT_PACK.md` = voor AI, wordt als eerste gelezen.
- `00_SYSTEM/CARD_SCHEMA.md` = enige bron van waarheid voor kaartvelden.
  `00_SYSTEM/DECISION_LOG.md` = log van elke structurele wijziging.
- `00_SYSTEM/OPERATING_PRINCIPLES.md` = de doctrine. `00_SYSTEM/CAPABILITY_ROUTER.md` = de
  router die vraag → kortste veilige route + executor-taak vertaalt.
- `00_SYSTEM/SOURCE_VERIFICATION.md` = het bron-verificatierecept.
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

### Globale autonomie-infrastructuur (geldt voor ELK project)
- Globale allowlist in `~/.claude/settings.json`. Eén keer ingesteld, elk project erft 'm.
  Toegestaan: veilige reads (`cat`/`ls`/`grep`/`find`/`pwd`), git-reads, `git add`,
  `git commit`. Geweigerd (deny wint altijd): `git push`, `reset --hard`, `--force`/`-f`,
  `branch -d/-D`, `git rm`, `rm -rf`, `supabase db push`, `supabase migration`, lezen van
  `.env`/secrets/credentials, `sudo`, `chmod 777`, `ssh`, `> /dev/`.
- Codex-debugger is globaal. Scripts in `~/.claude/scripts/` (`debug-escalate.sh` +
  `debug-boundary-check.sh`), `PostToolUseFailure`-hook wijst daarheen. Bij 3e dezelfde
  Bash-fout roept Codex (`codex exec`, lees-sandbox) een fix-VOORSTEL aan met label
  `BOUNDARY:SAFE`/`ARCH`; grens-check blokkeert ARCH/db/auth.
- Precedentie-feit (geverifieerd): deny wint altijd van allow, ook over scopes heen; arrays
  mergen over scopes. `/config` toont de effectieve merged config.
- Toestemming-vraaggedrag (B1, geverifieerd): `cat`/`ls` worden NIET geblokkeerd door de
  allowlist — ze draaien stil zolang het pad BINNEN de werkmap valt. De toestemmingsprompt
  komt uitsluitend bij lezen BUITEN de werkmap (aparte, bedoelde veiligheidslaag, los van
  allow/deny). Niets aan de allowlist te versoepelen; oplossing is operationeel = beide repos
  als buurmappen onder `~/dev`.

### Doctrine kaart-identiteit
- Kaart-identiteit = eigenaar + Source URL, nooit de naam alleen. `OPERATING_PRINCIPLES.md` §9
  + `CAPABILITY_ROUTER.md` stap 4. Namen botsen. Lezende laag matcht nooit op titel alleen;
  bij gelijkende kandidaten beide voorleggen met hun verschil.

### Schema
- Knowledge-kaart heeft twee velden ná "Volgende actie": **Herzien wanneer** (trigger) en
  **Wat zou dit bruikbaar maken** (drempel). Scheidt bron-status van herzieningssignaal.

---

## DEEL 2 — AF (staat op GitHub of lokaal gecommit)

- Fundament gebouwd en gepusht: volledige structuur, alle markdown gevuld, placeholders
  gelabeld. Skills-map als index: `01_CAPABILITIES/skills/operator-one-skills-map.md`.
- github_repo-kaarten met geverifieerde signalen: anthropics/skills, obra/superpowers,
  ComposioHQ/awesome-claude-skills, tinyhumansai/openhuman, grandamenium/dream-skill,
  msitarzewski/agency-agents, alirezarezvani/claude-skills, travisvn/awesome-claude-skills.
  Pattern-kaart: tokenjuice-compressie.
- Allowlist + Codex-debugger globaal gemaakt en bewezen.
- Schema uitgebreid met twee herzieningsvelden. Doctrine kaart-identiteit vastgelegd.
- Twee knowledge-kaarten: `affaan-m-everything-claude-code.md` (ECC) en `safishamsi-graphify.md`.
- `00_SYSTEM/SOURCE_VERIFICATION.md`: bron-verificatierecept (sterkst→zwakst: bron zelf lezen,
  `is_fork`/network-root, eigenaar als anker, moeilijk-vervalsbare signalen, malware-rode-
  vlaggen, functie-match). Gekoppeld aan §9 + router stap 4; verwijzing vanuit `CONTEXT_PACK.md`
  (leesvolgorde r7). Gelogd in DECISION_LOG.
- `.gitignore` (KB): lokale backups (`.bak/`, `*.backup`) uitgesloten.
- B1 verklaard (toestemming-vraaggedrag = werkmap-gedrag, niets aan allowlist). Zie infra boven.
- B2: AgentShield beproefd (`npx ecc-agentshield scan --path ~/.claude`, read-only, geen install).
  Oordeel: bruikbaar als INCIDENTELE check, niet als vaste tool; geen `--fix`, geen Pro.
  Grade B (87/100): Secrets/Hooks/MCP 100, Permissions 50. Leidde tot vier extra denyregels.
  Oordeel gelogd op de ECC-kaart; denylist-uitbreiding in DECISION_LOG. NB: AgentShield is van
  dezelfde maker als ECC → geen onafhankelijke audit.
- Opruiming: `~/dev/` aangemaakt, KB verhuisd naar `~/dev/kb`. OpenMontage (gecloonde repo van
  calesthio, niet eigen werk, online terug te halen) naar prullenbak. Recon-rapport
  `OPEN_SOURCE_WORKFLOW_RECON_REPORT.md` veiliggesteld in `~/dev/kb/02_KNOWLEDGE/docs/` als
  oogstbare bron (11 open-source workflow-tools: OpenAI Agents SDK, LangGraph, n8n, Activepieces,
  Mautic, Dittofeed, Twenty, PostHog, GrowthBook, Robyn, e.a. — patroon-oogst, niet platform-
  adoptie). Lege `~/13_DOCS` verwijderd.

### Afgerond — sessie 8 juni 2026 (Taak Y + Taak D laag 1)
- **Taak Y AF (op de Operator One master).** Master doc naar **v1.9**, commit `ae2046a`, gepusht.
  Drie ingrepen: (1) alle padverwijzingen `~/ALLURE` → `~/dev/allure` gecorrigeerd (incl.
  repo-root die nu vanuit `~/dev` start, en de eindesessie-checklist-commando's); (2)
  governance-blok ingekort tot verwijzing naar de config/`AGENTS.md` i.p.v. de grenzen nóg
  eens in proza te herhalen — de grenzen zélf (deny-lijst, harde stop, push-bij-founder,
  token-bewaking) blijven als feit staan; (3) zelf-geruststellende indek-toon uit de
  sessiehistorie gehaald ("geverifieerd niet aangenomen", "systeem gedroeg zich correct").
  Bewust NIET geraakt: dát commit/push bij Roel ligt — alleen de herhaling weg, de poort
  intact. Inzicht achter Taak Y: de échte begrenzing leeft in de Claude Code-config, niet in
  proza; het doc dat dezelfde grenzen herhaalt is dubbelop en is juist de bron waar een
  volgende Claude voorzichtigheid van overneemt en op doordraait.
- **Operator-One-soepelheid (Roel regelt zelf, geparkeerd):** de toestemmingsprompts tijdens
  het coderen storen omdat ze op de uitvoering zélf zitten (schrijven/wijzigen binnen de
  werkmap), niet op een echt beslismoment. Oorzaak gediagnosticeerd: de allowlist dekt alleen
  Bash; `Write`/`Edit`-tools staan er niet in, dus die vragen elke keer. Beslissing over wáár
  de poort ligt (commit vs. push) bewust NIET nu genomen — Roel verzamelt eerst screenshots
  van prompts die onzinnig voelen en komt daarmee terug. Bij vrijgeven van schrijven moet
  schrijven naar `.env`/secrets apart op deny (nu dekt deny alleen lézen).
- **Taak D stap 1 AF — Obsidian.** Geïnstalleerd via Homebrew (`brew install --cask obsidian`,
  v1.12.7), vault geopend op `~/dev/kb`. Mappenboom toont de hele structuur leesbaar; graph is
  een leeg sterrenveld (geen wikilinks) — verwacht, geen fout. Conclusie: het mappen-overzicht
  is nu het bruikbare overzicht, de graph nog niet. Obsidian maakt alleen een `.obsidian/`-map
  aan, raakt de kaarten niet.
- **Taak D laag 1 AF — read-only overzichtscript.** `05_SCRIPTS/kb-overview.py` (Python, getest
  vóór levering tegen nagebootste kaarten). Leest alle kaarten in `01_CAPABILITIES` +
  `02_KNOWLEDGE`, toont per kaart titel/`Type`/`Status`/`Completeness-status`/`Trust level`
  (lege status bovenaan zodat gaten opvallen), daarna `git status` kort per project
  (`kb`/`allure`/`operator-one`). Slaat `README.md`, `06_EXAMPLES` en `docs/` over. Veld-patroon:
  `- **Status:** <waarde>`. Read-only, raakt de grens niet. Twee commits gepusht: het script
  zelf + de `docs/`-skip-fix.
- **Bevinding (feit, geen aanname):** de KB heeft nú **5 echte kaarten**, allemaal
  `github_repo`, allemaal status `reviewed`, completeness `gedeeltelijk` (affaan-m,
  alirezarezvani, msitarzewski, safishamsi, travisvn). Géén losse placeholder-kaartbestanden
  met lege status — de "placeholders" uit eerdere taal bestaan niet als aparte bestanden. Het
  recon-rapport in `docs/` is een document, geen kaart (daarom geskipt).
- **Werkvorm-les bevestigd:** een `cp` uit Downloads zette de oude scriptversie terug ondanks
  "oude verwijderd, nieuwe gedownload". Niet gegokt — `grep` op de echte regel toonde de oude
  inhoud; daarna direct in het bestand gefixt met `sed` (binnen de werkmap, niet-destructief)
  i.p.v. opnieuw via Downloads te kopiëren. Bevestigt: toets aan de echte bron, kies de
  lichtste veilige werkvorm.
- **Taak X — ALLURE verhuisd** naar `~/dev/allure` (git intact, remote/commits behouden, oud pad
  weg). In `13_DOCS/OPERATOR_ONE_MASTER.md` 6 live padverwijzingen aangepast naar het nieuwe pad;
  regel 631 (historische key-les) bewust ongemoeid gelaten. CORRECTIE op vorige overdracht: de
  geschatte "~91 verwijzingen" waren er in werkelijkheid 22, waarvan 21 in genegeerde `.next/`
  build-cache (buiten git) — slechts EEN echt bestand was werk. Bevestigt de doctrine: een
  eerdere overdracht is geen onbetwistbaar feit, toets aan de echte bron. `.backup`/`.bak`
  toegevoegd aan ALLURE's `.gitignore`. Gepusht.
- **Taak C — KB gekoppeld aan ALLURE**: sectie "Knowledge base consultation" toegevoegd aan
  `AGENTS.md` (tussen Codex role en Supervised mode). Bevat: raadpleeg `../kb` vóór research/
  build, terugleg-lus, verwijzing naar `SOURCE_VERIFICATION.md` + identiteitsdoctrine. Engels,
  passend bij de Engelse kop-helft van het bestand. Gecommit, gepusht.

---

## DEEL 3 — TE DOEN (volgende sessie, in volgorde)

### Taak D — Cockpit, vervolg (laag 2, op afroep — niet eerder)
Stap 1 (Obsidian) en laag 1 (read-only overzichtscript) zijn AF, zie DEEL 2. Wat rest:
- **Laag 2 op afroep:** opereren/aansturen (projecten starten, executors). Raakt keys/auth/
  backend → grens-werk, bewuste latere bouw. Niet beginnen tot er een concrete behoefte is.
- **Wikilinks (uitgesteld, niet afgeschaft):** de graph is nu een leeg sterrenveld omdat de
  kaarten geen `[[wikilinks]]` gebruiken. Met 5 kaarten levert verbinden weinig op. Omzetten
  van `Gerelateerde`-velden → `[[wikilinks]]` wordt pas zinvol als de bibliotheek groeit
  ("verrijk alles"). Dan in één slag doen op een gevulde bibliotheek.
- **Laag 1 randpunt:** het script telt nu losse documenten in `02_KNOWLEDGE/docs/` NIET mee
  (opgelost deze sessie — recon-rapport was geen kaart). Mocht een ander documenttype later
  als valse "lege kaart" opduiken, dezelfde route: map toevoegen aan `SKIP_MAPPEN`.

### Losse randpunten
- AgentShield-scan periodiek herhalen bij grote wijziging aan allowlist/hooks/MCP (verificatie).
- npm-cache heeft root-eigendom-eiland (van een `sudo npm` op 26 mei): `~/.npm/_cacache/.../9f`
  is van root. Opruimen met `sudo chown -R $(whoami) ~/.npm` wanneer npm écht hindert. Niet urgent.
- OpenMontage staat in de prullenbak met datumstempel; ruimt 1 GB op bij Trash legen.

### Daarna (later)
- "Verrijk alles": marketing-skills (secties 1–17 van de skills-map) per stuk bekaarten wanneer
  ze gebruikt worden; API's/MCP's/SaaS volgen als nieuwe kaarten. Recon-rapport in
  `02_KNOWLEDGE/docs/` is een oogstbron voor workflow-tool-kaarten.
- Nachtelijk-autonoom via Codex: eerst Roels drie punten afvinken (debugger op ECHTE bug
  testen, review-vs-autonomie, token-spend-bewaking). Debugger is op een geforceerde fout
  getest, nog niet op een echte bug in een echt project.

---

## DEEL 4 — WERKWIJZE (zo werkt Roel)
- Nederlands, direct, bondig. Eén beslissing per keer, geen gebundelde opties.
- Done-criteria vóór bouwen. Altijd ready-to-paste prompts/commands, nooit alleen beschrijving.
- Geen commentaar (`# ...`) achter een shell-commando — dat breekt de regel.
- Git-push doet Roel in de gewone terminal, niet in Claude Code.
- Beoordeel Claude Code's werk op de GECOMMITTE bestanden, niet op streaming-previews.
- Niet gokken, niet te snel oordelen — eerst de bron zelf lezen/verifiëren, dan pas stellen.
- Een eerdere overdracht is GEEN onbetwistbaar feit: toets bron-gegevens opnieuw aan de echte bron.
- Kies de lichtste werkvorm die veilig is: anker-snippet voor live repo-files, complete herschrijf-
  download voor losse documenten zoals deze overdracht. Niet zwaarder maken dan nodig.
