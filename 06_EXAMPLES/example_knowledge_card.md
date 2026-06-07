# Voorbeeld — knowledge-kaart

> Een ingevulde voorbeeldkaart, gebaseerd op een eerdere echte evaluatie, die laat zien
> hoe een afwijzing óók waardevolle kennis is. Illustratie — verifieer vóór gebruik.

```
# OpenMontage — geautomatiseerde videomontage

- **Type:** github_repo
- **Source URL:** <repo-URL — ontbreekt nog —>
- **Source owner / creator:** OpenMontage-project
- **Datum toegevoegd:** 2025-..-..
- **Laatst gecheckt:** 2025-..-..
- **Samenvatting:** Open-source pijplijn voor geautomatiseerde videomontage (o.a. via
  transcript en FFmpeg-achtige bewerking).
- **Wat het doet:** Zet ruwe input om naar gemonteerde video met scènedetectie en
  transcript-gestuurde knipbeslissingen.
- **Praktisch nut:** Onderzocht als patroon voor de video-laag (Phase 2). Bruikbaar voor
  het begrijpen van de aanpak; niet als basis voor een schaalbaar product.
- **Vereisten:** FFmpeg, Whisper, zware lokale verwerking.
- **Moeilijkheid:** Hoog.
- **Trust level:** primair (repo van de maker)
- **Tags:** video, montage, ffmpeg, whisper, phase2
- **Gerelateerde capabilities:** ffmpeg (cli_tool), whisper (cli_tool/api_service)
- **Gerelateerde knowledge-kaarten:** openmontage-inzichten (pattern/case_study)
- **Risico's / limieten:** Zware contextlast en ~10 min per video → niet schaalbaar voor
  ons gebruik. Licentie AGPL-3.0: privégebruik kan, maar incorporeren in een te verkopen
  SaaS dwingt het hele product open — daarom niet als productbasis bruikbaar.
- **Volgende actie:** Architecturale inzichten bewaren als pattern; voor productie-kwaliteit
  betaalde API's overwegen (beeld/stem/video) i.p.v. deze gratis stack.
- **Completeness-status:** gedeeltelijk
- **Status:** rejected

OPEN: Source URL, exacte datums
```
