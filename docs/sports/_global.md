# Global Endpoints

These endpoints apply generally across all sports on Sofascore (Football, Tennis, Basketball, Esports, etc.) because Sofascore primarily revolves around a universal ID system for `events`, `teams`, and `players`.

> **Note on WAF/TLS Fingerprinting:**
> You must spoof your TLS fingerprint to access these endpoints directly over HTTP. Standard cURL or requests libraries will return `403 Forbidden`. Use a library like `curl_cffi` in Python (impersonating modern Chrome) and set valid `Origin`, `Referer`, and `User-Agent` headers.

---

## 1. Event Details

Returns core metadata about a match, including the tournament, start timestamp, and current state.

### Endpoint
`https://api.sofascore.com/api/v1/event/{eventId}`

### Method
`GET`

### Required Params
*   `eventId` (e.g., `11352523`)

### Example Response (Trimmed)
```json
{
  "event": {
    "tournament": {
      "name": "World Cup Qual. UEFA Playoffs",
      "slug": "world-championship-qual-uefa-playoffs",
      "category": {
        "name": "Europe",
        "slug": "europe",
        "sport": {
          "name": "Football",
          "slug": "football",
          "id": 1
        }
      }
    },
    "homeTeam": {
      "name": "Türkiye",
      "slug": "turkey",
      "shortName": "Türkiye"
    },
    "awayTeam": {
      "name": "Romania",
      "slug": "romania",
      "shortName": "Romania"
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
    "startTimestamp": 1742407200,
    "status": {
      "code": 100,
      "description": "Ended",
      "type": "finished"
    }
  }
}
```

### Verification Status
VERIFIED

---

## 2. Event Incidents

Returns a timeline array of match events (e.g. goals, cards, substitutions in football; breaks/sets in tennis).

### Endpoint
`https://api.sofascore.com/api/v1/event/{eventId}/incidents`

### Method
`GET`

### Example Response (Trimmed)
```json
{
  "incidents": [
    {
      "text": "FT",
      "homeScore": 1,
      "awayScore": 0,
      "isLive": false,
      "time": 90,
      "addedTime": 999,
      "incidentType": "period"
    },
    {
      "player": {
        "name": "Kerem Aktürkoğlu",
        "slug": "akturkoglu-kerem"
      },
      "incidentClass": "yellow",
      "incidentType": "card",
      "time": 78
    }
  ]
}
```

### Verification Status
VERIFIED

---

## 3. Team Profile

Returns core team details and team colors.

### Endpoint
`https://api.sofascore.com/api/v1/team/{teamId}`

### Method
`GET`

### Example Response (Trimmed)
```json
{
  "team": {
    "name": "Türkiye",
    "slug": "turkey",
    "shortName": "Türkiye",
    "gender": "M",
    "sport": {
      "name": "Football",
      "slug": "football",
      "id": 1
    },
    "national": true,
    "type": 0,
    "id": 4705,
    "teamColors": {
      "primary": "#e30a17",
      "secondary": "#ffffff",
      "text": "#ffffff"
    }
  }
}
```

### Verification Status
VERIFIED

---

## 4. Team Roster (Players)

### Endpoint
`https://api.sofascore.com/api/v1/team/{teamId}/players`

### Method
`GET`

### Verification Status
VERIFIED

---

## 5. Player Profile

### Endpoint
`https://api.sofascore.com/api/v1/player/{playerId}`

### Method
`GET`

### Verification Status
VERIFIED
