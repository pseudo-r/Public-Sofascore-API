# Baseball Endpoints

Baseball on Sofascore utilizes the standard `_global.md` architecture but introduces inning-by-inning scoring and highly specific match incidents.

## Core Navigation
* **Sport Slug:** `baseball` (used in schedules e.g., `/sport/baseball/scheduled-events/{date}`)
* **Global Support:** Full support for standard global Event, Team, and Player queries.

## Sport-Specific Quirks

### 1. Inning Scoring (Periods)
The Sofascore payload maps innings to `periodX` objects inside the main event payload. A standard 9-inning game will populate up to `period9`.

```json
"awayScore": {
  "current": 4,
  "display": 4,
  "period1": 0,
  "period2": 1,
  "period3": 0,
  "period4": 2,
  ...
  "period9": 0,
  "normaltime": 4
}
```

### 2. Match Incidents
The `/event/{eventId}/incidents` array tracks plays differently from traditional timed sports. Incidents are commonly logged by innings (`incidentType: "inning"`) or by runs scored (`incidentType: "run"`).
