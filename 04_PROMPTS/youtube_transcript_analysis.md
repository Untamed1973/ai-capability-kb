# Prompt — Video/transcript-analyse → knowledge-kaart

> Doel: uit een video (via transcript) de bruikbare kern halen en als knowledge-kaart
> (type `video`) vastleggen. We bewaren inzicht en werkwijze, niet een kopie.

## Gebruik

Geef de video-URL of plak het transcript. Respecteer `INGESTION_RULES.md`: samenvatten in
eigen woorden, geen lange letterlijke overname van het transcript.

---

INPUT: <video-URL of geplakt transcript>

Haal uit de video, in eigen woorden:

1. **Kernboodschap** — waar gaat het echt over (2–3 zinnen).
2. **Bruikbare technieken/stappen** — concreet, als lijst. Dit is de waarde.
3. **Voor welke route bruikbaar** — welk soort vraag helpt dit? Raakt het een capability
   of bestaand pattern?
4. **Vereisten** — wat heb je nodig om dit toe te passen?
5. **Risico's / kanttekeningen** — claims die je nog moet verifiëren, of beperkingen.
6. **Mogelijk nieuw pattern?** — als de video een herhaalbare werkwijze beschrijft,
   stel voor om ook een `pattern`-kaart in `02_KNOWLEDGE/patterns/` aan te maken.

Schrijf het resultaat als knowledge-kaart volgens `00_SYSTEM/CARD_SCHEMA.md`. Bepaal het
trust level eerlijk (een willekeurige tutorial is meestal `community`). Noteer source URL
en datums. Status `unverified`. Sluit af met pad `02_KNOWLEDGE/videos/<kebab-naam>.md` en
een `OPEN:`-regel.
