# Bron-verificatie

> Instructie aan de lezende laag (Codex, Claude Code, of welke executor dan ook). Raadpleeg
> dit telkens als je een nieuwe bron beoordeelt vóór je er een kaart van maakt of erop
> handelt. Doel: origineel scheiden van kloon/malware, en duplicaten herkennen. Dit document
> dient §9 van `OPERATING_PRINCIPLES.md` (identiteit = eigenaar + Source URL) en stap 4 van
> `CAPABILITY_ROUTER.md` (match op functie, nooit op naam alleen).

## Kernregel

Een naam bewijst niets. De identiteit van een bron is **eigenaar + Source URL + functie**,
niet de kop. Verifieer elke bron aan de bron zélf voordat je hem opneemt of inzet. Een
eerdere notitie of overdracht is géén bewijs — toets de gegevens opnieuw aan het origineel.

## Het recept (sterkst → zwakst signaal)

1. **Lees de GitHub-pagina (of officiële bron) zélf.** Nooit alleen een artikel erover.
   Artikelen geven verouderde of opgeklopte cijfers; de bron geeft de actuele waarheid.

2. **Check `is_fork: false` en de network-root.** Is de repo zijn eigen network-root
   (repository_id == network_root_id), dan is het een origineel en geen kopie. Een fork die
   zich als origineel voordoet is een rode vlag.

3. **De eigenaar is het anker, niet de reponaam.** Reponamen zijn vrij te kiezen en botsen.
   Verifieer de maker via een onafhankelijk kanaal (profiel, andere projecten, externe
   vermelding) voordat je de bron vertrouwt.

4. **Vergelijk moeilijk-te-vervalsen signalen.** Aanmaakdatum, commit-historie, contributors,
   issue- en PR-activiteit. Een verse kloon heeft een lege of te gladde historie; een echt
   project draagt sporen van tijd en meerdere handen.

5. **Let op malware-rode-vlaggen.** Stuurt de bron je naar "download de release" in plaats
   van naar broncode? Vraagt hij om ongezien uit te voeren install-scripts? Draagt hij een
   identieke naam onder een onbekende eigenaar? Heeft hij nauwelijks historie? Elk van deze
   is reden om te stoppen en Roel te raadplegen.

6. **Match op functie, niet op naam.** Bij twee gelijkende kandidaten: vergelijk wat ze doen,
   waarvoor ze geschikt zijn, en hun vorm — niet hun titel. Leg beide naast elkaar met hun
   verschil; vouw ze nooit samen tot één. (Zie §9 + router stap 4.)

## Uitkomst

- Geverifieerd origineel → opnemen als kaart met eigenaar + Source URL + geverifieerde
  signalen.
- Twijfel of rode vlag → niet autonoom opnemen of uitvoeren; leg voor aan Roel.
- Tijdelijk afgevallen (niet onveilig, wel nu ongeschikt) → status `reviewed` + de
  herzieningsvelden invullen ("geparkeerd, herzienbaar"), nooit `rejected`.
