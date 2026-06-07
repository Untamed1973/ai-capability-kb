# Ingestion Rules

Regels voor het binnenhalen en indexeren van bronnen. Deze gelden voor elke scraper,
prompt of executor die kennis aan dit systeem toevoegt.

## Wat mag

- **Publieke bronnen** mogen worden geïndexeerd wanneer dat is toegestaan (denk aan
  publieke documentatie, openbare repos, openbaar gepubliceerde posts/video's).
- **Eigen of gelicentieerd materiaal** mag alleen voor persoonlijk gebruik worden
  geïndexeerd wanneer de voorwaarden dat toelaten.

## Wat niet mag

- Geen omzeilen van **paywalls, logins, DRM of toegangsbeperkingen**.
- Geen reproductie van auteursrechtelijk beschermd materiaal buiten wat is toegestaan.
- Geen opslag van credentials, sleutels of persoonsgegevens van derden in kaarten.

## Hoe we opslaan

- Bewaar altijd **source URL, datum van ophalen, en trust level** (zie
  `SOURCE_TRUST_LEVELS.md`).
- **Prefereer samenvattingen en gestructureerde notities** boven ruw gekopieerde inhoud.
  De waarde zit in onze structuur en duiding, niet in een kopie van het origineel.
- Respecteer auteursrechtgrenzen: korte, eigen-woorden samenvattingen; geen lange
  letterlijke overnames.
- Leg bij twijfel over toelaatbaarheid de bron voor aan Roel in plaats van te indexeren.

## Verhouding tot de autonomie-doctrine

Indexeren van een bron (een *kaart* schrijven) is veilige markdown en mag autonoom binnen
deze regels. Het *gebruiken* van een bron of dienst die de harde grens raakt (keys, auth)
stopt voor Roel — zie `OPERATING_PRINCIPLES.md`.
