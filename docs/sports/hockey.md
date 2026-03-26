# Ice Hockey Endpoints

Ice Hockey is natively supported by the generic Sofascore `_global.md` schemas with a slug modification.

## Core Navigation
* **Sport Slug:** `ice-hockey` (used in schedules e.g., `/sport/ice-hockey/scheduled-events/{date}`)
* **Global Support:** Full support for `_global.md` generic `event/{id}` details.

## Sport-Specific Quirks

### 1. Match Scoring (Periods)
Hockey events map the traditional 3-period structure precisely:

```json
"awayScore": {
  "current": 4,
  "display": 4,
  "period1": 1,
  "period2": 2,
  "period3": 1,
  "normaltime": 4
}
```

### 2. Overtime and Shootouts
If a match exceeds normal time, the payload conditionally injects `overtime` and `penalties` root objects alongside the period keys.

### 3. Match Incidents
Unlike football, incidents in the timeline (`/event/{eventId}/incidents`) track hockey-specific penalty minutes (2m, 5m, 10m) using the `incidentClass` modifier. 
