# Football (Soccer) Endpoints

These endpoints are specifically tailored for football (soccer) schedules, unique tournaments, and match granularities on `api.sofascore.com`.

---

## 1. Daily Scheduled Events (Football)

Loads all football matches scheduled for a specific date. This powers the main daily view on Sofascore.

### Endpoint
`https://api.sofascore.com/api/v1/sport/football/scheduled-events/{date}`

### Method
`GET`

### Required Params
*   `date` (Format: `YYYY-MM-DD`, e.g., `2026-03-26`)

### Example Response (Trimmed)
```json
{
  "events": [
    {
      "tournament": {
        "name": "World Cup Qual. UEFA Playoffs",
        "slug": "world-championship-qual-uefa-playoffs",
        "category": {
            "name": "Europe",
            "slug": "europe"
        }
      },
      "customId": "IUbsXVb",
      "status": {
        "code": 100,
        "description": "Ended",
        "type": "finished"
      },
      "winnerCode": 1,
      "homeTeam": {
        "name": "Türkiye",
        "slug": "turkey",
        "shortName": "Türkiye",
        "id": 4705
      },
      "awayTeam": {
        "name": "Romania",
        "slug": "romania",
        "shortName": "Romania",
        "id": 4716
      },
      "homeScore": {
        "current": 1,
        "display": 1,
        "period1": 1,
        "normaltime": 1
      },
      "awayScore": {
        "current": 0,
        "display": 0,
        "period1": 0,
        "normaltime": 0
      },
      "id": 11352523,
      "startTimestamp": 1742407200
    }
  ]
}
```

### Verification Status
VERIFIED

---

## 2. Match Statistics

Detailed match statistics including possession, shots, passing, and duels data.

### Endpoint
`https://api.sofascore.com/api/v1/event/{eventId}/statistics`

### Method
`GET`

### Example Response (Trimmed)
```json
{
  "statistics": [
    {
      "period": "ALL",
      "groups": [
        {
          "groupName": "Match overview",
          "statisticsItems": [
            {
              "name": "Ball possession",
              "home": "68%",
              "away": "32%",
              "compareCode": 1,
              "statisticsType": "positive",
              "valueType": "event",
              "homeValue": 68,
              "awayValue": 32,
              "renderType": 2,
              "key": "ballPossession"
            }
          ]
        }
      ]
    }
  ]
}
```

### Verification Status
VERIFIED

---

## 3. Match Momentum Graph

Sofascore's famous "Attack Momentum" graph. The `value` generally spans between -100 to 100 based on the attacking pressure of home vs away teams.

### Endpoint
`https://api.sofascore.com/api/v1/event/{eventId}/graph`

### Method
`GET`

### Example Response (Trimmed)
```json
{
  "graphPoints": [
    {"minute": 1, "value": 5},
    {"minute": 2, "value": 24},
    {"minute": 3, "value": 19},
    {"minute": 4, "value": 54},
    {"minute": 5, "value": 38},
    {"minute": 6, "value": 20}
  ]
}
```

### Verification Status
VERIFIED

---

## 4. Match Lineups

Starting XI and substitutions for both teams, including player ratings if available.

### Endpoint
`https://api.sofascore.com/api/v1/event/{eventId}/lineups`

### Method
`GET`

### Verification Status
VERIFIED

---

## 5. Match Managers

Returns the data for the team managers.

### Endpoint
`https://api.sofascore.com/api/v1/event/{eventId}/managers`

### Method
`GET`

### Verification Status
VERIFIED
