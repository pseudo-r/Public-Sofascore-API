# Rugby Endpoints

Rugby Union and Rugby League share the Sofascore global schema under the `rugby` slug.

## Core Navigation
* **Sport Slug:** `rugby`
* **Global Support:** Fully compatible with standard search, event, and team structures.

## Sport-Specific Quirks
* Scoring is divided into two halves (`period1`, `period2`) matching the generic `football` model.
* The `/event/{eventId}/incidents` acts as a scoring summary denoting (Tries, Conversions, Penalties, Drop Goals).
