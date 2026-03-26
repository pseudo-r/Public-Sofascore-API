# MMA / Combat Sports Endpoints

MMA on Sofascore inherits the standard `_global.md` schema under the `mma` slug, though it bypasses deep statistical integration natively (relying on incidents for outcomes like KOs/Submissions).

## Core Navigation
* **Sport Slug:** `mma` 
* **Global Support:** Full support for `_global.md` generic `event/{id}` details.

## Sport-Specific Quirks
- Fighters are mapped to `homeTeam` and `awayTeam` nodes inside the `eventId` payload.
- There is no period-by-period scoring payload; match lengths/rounds are denoted in the final status or incident summary strings.
