# American Football Endpoints

American Football scores and timelines inherit the Sofascore global schema via the explicit `american-football` routing slug.

## Core Navigation
* **Sport Slug:** `american-football`
* **Global Support:** Fully compatible with standard search, event, and team structures.

## Sport-Specific Quirks

### 1. Match Scoring (Quarters)
Similar to basketball, scoring data is split strictly across 4 periods (quarters).

```json
"awayScore": {
  "current": 24,
  "display": 24,
  "period1": 7,
  "period2": 3,
  "period3": 0,
  "period4": 14,
  "normaltime": 24
}
```

### 2. Play-by-Play & Incidents
The standard `/event/{eventId}/incidents` acts as a scoring summary (Touchdowns, Field Goals, Safeties, Extra Points).
*Note:* A true textual play-by-play (every snap and down) may require parsing deeper sub-feeds (e.g. `play-by-play` if active, depending on the NFL vs College coverage).
