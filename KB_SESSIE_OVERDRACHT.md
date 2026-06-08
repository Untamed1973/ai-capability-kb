# AI CAPABILITY KB — INSTRUCTIE VOLGENDE SESSIE

Plak dit aan het begin van een nieuwe chat. Dit is een instructie, geen verslag.
Twee delen: VAST (beslist — niet heroverwegen) en TE DOEN (taken). Behandel VAST als feit.

Repo: `Untamed1973/ai-capability-kb`, branch `main`. Lokaal: `~/dev/kb`.
(LET OP: pad gewijzigd — de KB is verhuisd van `~/Downloads/ai-capability-kb` naar `~/dev/kb`.)
Roel is niet-technisch; Claude = architect, Claude Code = executor.

Oproepen voor de volgende sessie: `cat ~/dev/kb/KB_SESSIE_OVERDRACHT.md` → kopiëren → plakken.

Werkwijze deze sessies: Roel plakt terminal-output, Claude geeft ready-to-paste commando's.
Bestanden worden geschreven via `cat > … << 'EOF'` of via een Python-snippet met anker-check
(controleert dat de ankertekst exact 1x voorkomt vóór het schrijft — veilig, geen blind
overschrijven). Altijd back-up vóór wijzigen, inhoud valideren ná schrijven, dan pas
committen. Push doet Roel zelf.

---

## DEEL 1 — VAST (beslist, niet heroverwegen)

### Mappenstructuur (NIEUW deze sessie — geldt voor ALLES)
- Thuisbasis voor alle code-projecten: `~/dev/`. Daaronder als buurmappen:
  `~/dev/kb` (deze KB), `~/dev/allure` (NOG TE VERHUIZEN — zie TE DOEN), `~/dev/operator-one`
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
- `00_SYSTEM/SOURCE_VERIFICATION.md` = het bron-verificatierecept (NIEUW, zie af-lijst).
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
  `.env`/secrets/credentials, EN (NIEUW deze sessie) `sudo`, `chmod 777`, `ssh`, `> /dev/`.
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
  als buurmappen onder `~/dev` (zie structuur).

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
- github_repo-kaarten met geverifieerde signalen (eerder): anthropics/skills, obra/superpowers,
  ComposioHQ/awesome-claude-skills, tinyhumansai/openhuman, grandamenium/dream-skill,
  msitarzewski/agency-agents, alirezarezvani/claude-skills, travisvn/awesome-claude-skills.
  Pattern-kaart: tokenjuice-compressie.
- Allowlist + Codex-debugger globaal gemaakt en bewezen.
- Schema uitgebreid met twee herzieningsvelden. Doctrine kaart-identiteit vastgelegd.
- Twee knowledge-kaarten: `affaan-m-everything-claude-code.md` (ECC) en `safishamsi-graphify.md`.

### NIEUW afgerond deze sessie
- **Taak A — `00_SYSTEM/SOURCE_VERIFICATION.md`**: bron-verificatierecept (sterkst→zwakst:
  bron zelf lezen, `is_fork`/network-root, eigenaar als anker, moeilijk-vervalsbare signalen,
  malware-rode-vlaggen, functie-match). Gekoppeld aan §9 + router stap 4; verwijzing vanuit
  `CONTEXT_PACK.md` (leesvolgorde r7). Gelogd in DECISION_LOG.
- **`.gitignore`**: lokale backups (`.bak/`, `*.backup`) uitgesloten.
- **Taak B — B1**: toestemming-vraaggedrag verklaard (werkmap-gedrag, niets aan allowlist).
  Zie autonomie-infra hierboven.
- **Taak B — B2**: AgentShield beproefd (`npx ecc-agentshield scan --path ~/.claude`, read-only,
  geen install). Oordeel: bruikbaar als INCIDENTELE check, niet als vaste tool; geen `--fix`,
  geen Pro. Grade B (87/100): Secrets/Hooks/MCP 100, Permissions 50. Leidde tot vier extra
  denyregels. Oordeel gelogd op de ECC-kaart; denylist-uitbreiding gelogd in DECISION_LOG.
  NB: AgentShield is van dezelfde maker als ECC → geen onafhankelijke audit.
- **Opruiming/structuur**: `~/dev/` aangemaakt. KB verhuisd naar `~/dev/kb`. OpenMontage
  (gecloonde repo van calesthio, niet eigen werk, online terug te halen) naar prullenbak.
  Recon-rapport `OPEN_SOURCE_WORKFLOW_RECON_REPORT.md` veiliggesteld in
  `~/dev/kb/02_KNOWLEDGE/docs/` als oogstbare bron (11 open-source workflow-tools: OpenAI
  Agents SDK, LangGraph, n8n, Activepieces, Mautic, Dittofeed, Twenty, PostHog, GrowthBook,
  Robyn, e.a. — patroon-oogst, niet platform-adoptie). Lege `~/13_DOCS` verwijderd.
- KB-overdracht (dit bestand) woont nu in `~/dev/kb/KB_SESSIE_OVERDRACHT.md`.

---

## DEEL 3 — TE DOEN (volgende sessie, in volgorde)

### Taak X — ALLURE verhuizen naar `~/dev/allure` (EERST, eigen ALLURE-sessie)
NB: dit hoort in een Operator One/ALLURE-sessie, NIET in een KB-sessie — het raakt ALLURE's
eigen documentatie en governance.
- ALLURE staat nog op `~/ALLURE` (git-repo `allure-os`, live op Vercel, GitHub workflow
  `founder-operator-runner.yml`). Map fysiek verplaatsen naar `~/dev/allure` is veilig (git
  reist mee), MAAR: er staan ~91 verwijzingen naar het pad `~/ALLURE` / `/Users/roelvinck/ALLURE`
  in de repo, veel in `OPERATOR_ONE_MASTER.md`. Die moeten één voor één beoordeeld worden:
  welke zijn live instructies (aanpassen), welke zijn voorbeelden/changelog-historie (laten).
  NIET blind via grep ombouwen — master-doc regel voor regel met Roel erbij.
- Workflow + ask-operator.sh gebruiken relatieve paden (geverifieerd schoon). ALLURE's
  `.claude`-config schoon. Alleen de ~91 tekstuele verwijzingen zijn het werk.

### Taak C — KB koppelen aan ALLURE (in diezelfde ALLURE-sessie, ná de verhuizing)
Doel: Claude Code raadpleegt in elk project automatisch eerst de KB voordat hij iets nieuws
onderzoekt of bouwt.
- Voeg aan ALLURE's control-file (`AGENTS.md`/`CLAUDE.md`) een instructie toe: "Voordat je een
  tool/aanpak/patroon onderzoekt of bouwt: raadpleeg eerst de AI Capability KB op `../kb`.
  Bestaat er al een kaart/pattern/beoordeelde bron? Gebruik die. Pas als de KB niets heeft,
  onderzoek je nieuw — en leg je bevinding terug als kaart." (Terugleg-zin sluit de lus.)
  Verwijst ook naar `00_SYSTEM/SOURCE_VERIFICATION.md` voor hóé bronnen geverifieerd worden.
- Werkt pas schoon als ALLURE óók onder `~/dev` staat (Claude Code start vanuit `~/dev`, ziet
  `kb` + `allure` als buurmappen). Vandaar: ná Taak X.
- Wijzigt control-files van een draaiend project → via Claude Code in de repo, review + push
  door Roel. Tekst voorstellen mag Claude; uitvoeren doet Roel.

### Taak Y — Instructiebestanden losser maken (eigen sessie met het bestand erbij)
Roel is de afgelopen weken onderlegder en minder "bang" geworden. Patroon om te corrigeren:
overmatige voorzichtigheid die zichzelf voedt — als Claude voorzichtigheid deelt, draaft een
volgende Claude daar soms op door en maakt het stééds voorzichtiger. De instructie-/master-
bestanden (Operator One én deze KB-overdracht) mogen strakker: minder indekken, meer bouwen,
zonder de échte harde grenzen (schema/auth/keys/push) te verzwakken. Doen met het betreffende
bestand erbij, niet blind.

### Taak D — Cockpit (in deze volgorde, niet eerder)
1. Obsidian op de vault (`~/dev/kb` als vault openen). Eerst zien wat overzicht/graph geeft.
   Optioneel: `Gerelateerde`-velden → `[[wikilinks]]`.
2. Laag 1: read-only overzicht dat de markdown uitleest (kaarten, status, vullingsgraad,
   working tree per project). Veilig, raakt de grens niet.
3. Laag 2 op afroep: opereren/aansturen (projecten starten, executors). Raakt keys/auth/
   backend → grens-werk, latere bouw.

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
