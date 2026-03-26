# Basketball Endpoints

Basketball matches closely follow the global Sofascore endpoints, mapped under the `basketball` slug.

## Core Navigation
* **Sport Slug:** `basketball` (used in schedules e.g., `/sport/basketball/scheduled-events/{date}`)
* **Global Support:** Full support for `_global.md` endpoints (Event Details, Team Profile, Player Profile).

## Sport-Specific Quirks

### 1. Match Scoring (Quarters)
Unlike football halves, basketball `event` responses chunk scoring dynamically into quarters inside the `homeScore` and `awayScore` objects:

```json
"homeScore": {
  "current": 115,
  "display": 115,
  "period1": 30,
  "period2": 25,
  "period3": 28,
  "period4": 32,
  "normaltime": 115
}
```
*Note: Overtime periods will append as `overtime1`, `overtime2`, etc.*

### 2. Match Statistics
The `/event/{eventId}/statistics` endpoint for basketball replaces possession/cards with basketball-specific metrics:
* Field Goals (Made/Attempted)
* 3 Pointers
* Free Throws
* Rebounds (Defensive/Offensive)
* Turnovers / Steals
