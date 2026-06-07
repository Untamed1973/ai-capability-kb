# AI Capability KB

Een levend, doorzoekbaar brein voor AI-capabilities en kennis. Project-agnostisch:
dit systeem staat **boven** elk afzonderlijk project (zoals Operator One / ALLURE) en
helpt bij élk toekomstig project antwoord te geven op:

- Wat weten we hier al over?
- Welke tools, agents, scripts, MCP's of workflows kunnen helpen?
- Welke GitHub-repos of docs zijn relevant?
- Wat moet Codex, Claude Code of een andere executor nu doen?

## Waarheid en lenzen

De **waarheid** is platte markdown in git. Bewust gekozen: geen enkele gesloten tool
geeft een laag die tegelijk door executors (Claude Code, Codex, later Gemini) te
schrijven is, versiebeheerd is, én bovenaan elk project kan staan. Zodra kennis in een
gesloten tool zit, kan je executor er niet meer in schrijven — en dat breekt precies de
autonomie die dit systeem mogelijk moet maken.

Tools als **Obsidian** (mens-navigatie: backlinks, graph) of **NotebookLM** (latere
Q&A-leeslaag) mogen er als *lens* bovenop draaien. Nooit als fundament. Frictieloos,
selectief adopteren.

## Twee databases

Het systeem heeft twee kernen:

**1. Capability Registry — `01_CAPABILITIES/`**
Beantwoordt: *"Welke handjes/tools hebben we?"*
Agents, skills, MCP-servers, CLI-tools, API-diensten, modellen, scrapers, workflows,
executors. Dit is de gereedschapskist.

**2. Knowledge Base — `02_KNOWLEDGE/`**
Beantwoordt: *"Wat weten we?"*
GitHub-repos, docs, courses, video's, posts, case studies, en **patterns** (de
bouwtekeningen — niet alleen wélke tool, maar hóe je 'm inzet).

De gereedschapskist zegt "hier is een decoupeerzaag". De bibliotheek leert hoe je
ermee een dakkapel bouwt — en niet één, maar de varianten die we hebben verzameld.
Belangrijk: de bibliotheek is **groeiend, niet alwetend**. Wat erin staat en getest is,
kan betrouwbaar autonoom. Wat ontbreekt, is geen garantie. Daarom is het structureel
blijven verzamelen het hart van dit systeem, geen bijzaak.

## De router (de kern van het gebruik)

Zie `00_SYSTEM/CAPABILITY_ROUTER.md`. Bij elke build-/research-/automatiserings-/media-/
code-/workflow-vraag doorloopt het systeem zes stappen en geeft het bovendien een
**autonomie-oordeel**: mag dit autonoom, of stopt het voor Roel?

## MVP-flow (eerste versie)

1. Je stelt een vraag of doet een productvoorstel.
2. Het systeem leest `CONTEXT_PACK.md` (weet meteen wat er bestaat en welke regels gelden).
3. De router checkt capabilities, detecteert intentie, doorzoekt de knowledge base.
4. De router matcht en **weegt** routes (kosten, gemak, kwaliteit, snelheid, grens-impact).
5. Het systeem stelt de kortste veilige route voor + een autonomie-oordeel.
6. Het genereert een taak/prompt voor de executor (Claude Code / Codex / GitHub Action).
7. Nieuwe inzichten worden teruggelegd als kaart → de bibliotheek groeit.

## Ingangen

- **README.md** — voor mensen (dit bestand).
- **CONTEXT_PACK.md** — voor AI. Wat elke nieuwe chat als eerste leest. Heilig: kort,
  extreem helder, altijd actueel.

## Cockpit (latere horizon — nu niet gebouwd)

Een dashboard als *lens* op dezelfde markdown, in twee lagen:

- **Laag 1 — de kaart (read-only):** projectoverzicht, agents/skills per project, de
  working tree (overzicht voor het brein), beschikbare abonnementen, en de
  **verrijkingslijst** (welke kaarten half zijn, welke velden het vaakst ontbreken) en
  de **review-queue** (kaarten die menselijke check nodig hebben — als gegenereerde
  view, niet als aparte map).
- **Laag 2 — opereren:** projecten starten en executors aansturen. Raakt de harde grens
  (keys, auth, backend) → latere fase. Géén eigen chatvenster: de cockpit is kaart +
  startknop naar bestaande tools (Claude Code, Codex), niet iets dat al werkt opnieuw
  uitvindt.

## Wat hierna bouwen (implementatienoot)

Dit is het *fundament*. De zinvolle volgende stappen, in volgorde:

1. **Vul de eerste echte kaarten.** Begin met je huidige stack als capabilities
   (Claude Code, Codex, Supabase, Vercel) en je modellen (Claude, OpenAI, Gemini). Migreer
   `OPERATOR_ONE_SKILLS_MAP.md` naar `01_CAPABILITIES/skills/`.
2. **Test de router met één echte vraag** uit een lopend project en kijk of de voorgestelde
   route klopt. Stel de prompts bij op basis van wrijving.
3. **Zet Obsidian op de map** als je visueel wilt navigeren (nul migratie).
4. **Pas daarna** de cockpit (laag 1) en de index-/nightly-automatisering — die staan nu
   bewust als placeholders, omdat er nog geen executor-laag aan gekoppeld is.

Niet eerder een app bouwen dan dat de kennisstructuur klopt en gevuld raakt.
