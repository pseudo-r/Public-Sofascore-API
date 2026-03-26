# Tennis Endpoints

Tennis relies on the core global `eventId` structure on Sofascore, but routes discovery slightly differently (using `scheduled-tournaments` instead of `scheduled-events`) and has unique incident properties like `point-by-point`.

---

## 1. Daily Scheduled Tournaments (Tennis)

Returns the root list of active tournaments containing scheduled matches.

### Endpoint
`https://api.sofascore.com/api/v1/sport/tennis/scheduled-tournaments/{date}/page/1`

### Method
`GET`

### Required Params
*   `date` (Format: `YYYY-MM-DD`, e.g., `2026-03-26`)

### Example Response (Trimmed)
```json
{
  "scheduled": [
    {
      "tournament": {
        "name": "Miami, USA",
        "slug": "miami-usa",
        "category": {
          "name": "ATP",
          "slug": "atp"
        }
      },
      "customId": "VjbsZjb",
      "status": {
        "code": 100,
        "description": "Ended",
        "type": "finished"
      },
      "winnerCode": 1,
      "homeTeam": {
        "name": "Sinner J.",
        "slug": "sinner-jannik",
        "shortName": "Sinner J.",
        "id": 268711
      },
      "awayTeam": {
        "name": "Dimitrov G.",
        "slug": "dimitrov-grigor",
        "shortName": "Dimitrov G.",
        "id": 65113
      },
      "homeScore": {
        "current": 2,
        "display": 2,
        "period1": 6,
        "period2": 6
      },
      "awayScore": {
        "current": 0,
        "display": 0,
        "period1": 3,
        "period2": 1
      },
      "id": 12154946,
      "startTimestamp": 1711910400
    }
  ]
}
```

### Verification Status
VERIFIED

---

## 2. Tennis Power Graph

Instead of the "Attack Momentum" graph used in football, tennis uses a "Tennis Power" graph to illustrate who controls the match flow.

### Endpoint
`https://api.sofascore.com/api/v1/event/{eventId}/tennis-power`

### Method
`GET`

### Verification Status
VERIFIED

---

## 3. Point-by-Point

Returns the chronological progression of the score within a game.

### Endpoint
`https://api.sofascore.com/api/v1/event/{eventId}/point-by-point`

### Method
`GET`

### Verification Status
VERIFIED
