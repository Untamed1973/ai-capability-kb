# API Services

Externe diensten die je via een API aanroept — geen gewone tool, maar een dienst met een
sleutel, kosten, limieten, kwaliteitsverschil, lock-in en privacy/security-impact.

**Kaarttype:** `api_service` — zie `00_SYSTEM/CARD_SCHEMA.md` en
`04_PROMPTS/create_capability_card.md`.

**Voorbeelden:** FAL/FLUX (beeld), ElevenLabs (stem), Kling/Veo (video), en de model-API's
van providers wanneer je ze puur als dienst aanroept.

> **Grens-implicatie:** elke dienst hier draagt een sleutel. De *kaart* schrijven (wat het
> doet, kost, riskeert) is veilige markdown en mag autonoom. Het *aanroepen* van de dienst
> raakt de harde grens (keys, `.env`) en **stopt voor Roel**. Zet nooit een sleutel in een
> kaart — alleen de aard van de auth ("vereist API-key in env").
