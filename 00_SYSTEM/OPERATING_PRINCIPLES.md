# Operating Principles

De doctrine van dit systeem. Bij twijfel winnen deze principes van gemak of snelheid.

## 1. De harde grens (stopt altijd voor Roel)

Een taak **stopt en vraagt Roel** zodra hij raakt aan:

- databaseschema of migraties
- authenticatie of autorisatie
- RLS-policies
- `.env`-bestanden of omgevingsvariabelen
- API-keys of secrets
- destructieve operaties (verwijderen, overschrijven, force-push)

Deze grens stopt **altijd** — ook wanneer twee AI's het eens zijn dat het veilig is. Een
"BOUNDARY:SAFE"-label van een ander systeem heft de grens niet op. In projecten wordt dit
onafhankelijk gehandhaafd (bv. `debug-boundary-check.sh`).

## 2. Autonomie-doctrine

De bibliotheek bepaalt wat "bekend werk" is.

- **Autonoom toegestaan:** de taak routeert schoon naar een capability met status
  `tested` of `canonical`, én valt volledig binnen de veilige grens.
- **Stop, vraag Roel:** onbekende capability, status `unverified`/`reviewed`, óf de taak
  raakt de harde grens (zie §1).

Zo hoeft Roel alleen het onbekende goed te keuren, en wordt bekend werk frictieloos.

## 3. Maak de echte fout eerst zichtbaar

Niet fixen op een gok. Eerst diagnose, dan actie. Toon de werkelijke error vóór je iets
verandert.

## 4. Eén waarheid

`OPERATING_PRINCIPLES.md` en `CARD_SCHEMA.md` zijn canoniek. Niets woont op twee plekken.
Overzichten, lijsten en queues (verrijkingslijst, review-queue, working tree) zijn
**gegenereerde lenzen** op de markdown — geen tweede opslagplaats. Status is een
*eigenschap* van een kaart; een kaart verhuist niet tussen mappen om een status te tonen.

## 5. Een leeg veld is een taak, geen fout

Onvolledige kaarten mogen bestaan, zijn doorzoekbaar, en krijgen een completeness-status.
Ontbrekende velden worden expliciet gemarkeerd ("ontbreekt nog: …"). Bij het vergaren
wordt zoveel mogelijk gevuld; gaten blijven zichtbaar in plaats van stil te verdwijnen.

## 6. Schema-wijziging stopt voor Roel

Het kaart-schema breidt **met de hand** uit, als bewuste architectuurbeslissing. Een
prompt mag *voorstellen* "deze bron bevat info die in geen veld past — overweeg veld X",
maar verandert het schema nooit autonoom. Elke schema-wijziging komt in
`DECISION_LOG.md`.

## 7. Frictieloos, selectief adopteren

Bouw niet wat bestaande tools al beter doen (graph, search, Q&A). Adopteer alleen wat
duidelijk waarde toevoegt. Het hart (schema, vulprompts, router) bouwen we zelf, omdat
het van Roel moet zijn en door elke executor leesbaar moet blijven.

## 8. Statussen (kort — definitie staat in CARD_SCHEMA.md)

`unverified` → `reviewed` → `tested` → `canonical`, met `rejected` als zijspoor.
Alleen `tested` en `canonical` tellen mee voor autonomie.

## 9. Kaart-identiteit = bron, niet naam

De identiteit van een kaart is de **eigenaar + Source URL**, nooit de naam alleen. Namen
botsen — twee verschillende tools kunnen dezelfde naam dragen (zie de twee "Graphify"-
projecten: `safishamsi/graphify`, een assistant-skill, vs. een eerder genoteerd
gelijknamig pip-pakket). Een lezende laag (Codex, Claude Code, of welke laag dan ook) mag
een kaart daarom nooit op titel alleen matchen. Het onderscheid zit in eigenaar, URL, en
vooral in *wat het doet en waarvoor het geschikt is* — de volledige kaart, niet de kop.
Bij gelijkende kandidaten worden ze naast elkaar gelegd en op functie onderscheiden, niet
samengevouwen tot één.
