# Motorsport / Racing Endpoints

Sofascore racing utilizes the `motorsport` routing slug.

## Core Navigation
* **Sport Slug:** `motorsport`
* **Global Support:** Reduced support. While events load properly, many team/driver specific lookups differ strictly depending on the Formula/Series (F1, MotoGP, WRC).

## Sport-Specific Quirks
* The `/event/{eventId}` payload replaces generic `homeTeam/awayTeam` scores with an array of competitors (drivers and constructors) finishing times, points, and laps completed mapped inside the `standings` arrays.
