# Sofascore API Response Schemas

This document provides extensive examples of the core data models returned by the Sofascore `api.sofascore.com/api/v1` endpoints. Use these references to build your deserialization models.

## 1. Global Event Model

This model is the primary object returned under the `"event"` key by `/event/{eventId}`.

```json
{
  "event": {
    "tournament": {
      "name": "LaLiga",
      "slug": "laliga",
      "category": {
        "name": "Spain",
        "slug": "spain",
        "sport": {
          "name": "Football",
          "slug": "football",
          "id": 1
        },
        "id": 32,
        "flag": "spain"
      },
      "uniqueTournament": {
        "name": "LaLiga",
        "slug": "laliga",
        "id": 8
      },
      "priority": 1,
      "id": 169
    },
    "customId": "wWscac",
    "status": {
      "code": 100,
      "description": "Ended",
      "type": "finished"
    },
    "winnerCode": 1,
    "homeTeam": {
      "name": "Real Madrid",
      "slug": "real-madrid",
      "shortName": "Real Madrid",
      "userCount": 2187321,
      "nameCode": "RMA",
      "national": false,
      "type": 0,
      "id": 2829,
      "teamColors": {
        "primary": "#ffffff",
        "secondary": "#ffffff",
        "text": "#ffffff"
      }
    },
    "awayTeam": {
      "name": "Barcelona",
      "slug": "barcelona",
      "shortName": "Barcelona",
      "userCount": 2512934,
      "nameCode": "BAR",
      "national": false,
      "type": 0,
      "id": 2817,
      "teamColors": {
        "primary": "#004d98",
        "secondary": "#a50044",
        "text": "#004d98"
      }
    },
    "homeScore": {
      "current": 3,
      "display": 3,
      "period1": 1,
      "period2": 2,
      "normaltime": 3
    },
    "awayScore": {
      "current": 2,
      "display": 2,
      "period1": 1,
      "period2": 1,
      "normaltime": 2
    },
    "time": {
      "injuryTime1": 2,
      "injuryTime2": 5,
      "currentPeriodStartTimestamp": 1713732644
    },
    "changes": {
      "changes": [
        "status.code",
        "status.description",
        "status.type"
      ],
      "changeTimestamp": 1713735750
    },
    "hasGlobalHighlights": true,
    "hasXg": true,
    "hasEventPlayerStatistics": true,
    "hasEventPlayerHeatMap": true,
    "detailId": 1
  }
}
```

## 2. Match Incident Model

Returned within the `"incidents"` array via `/event/{eventId}/incidents`.

```json
{
  "text": "GOAL",
  "homeScore": 3,
  "awayScore": 2,
  "isLive": false,
  "time": 90,
  "addedTime": 1,
  "timeSeconds": 5412,
  "reversedPeriodTime": 1,
  "reversedPeriodTimeSeconds": 588,
  "incidentType": "goal",
  "incidentClass": "regular",
  "player": {
    "name": "Jude Bellingham",
    "slug": "jude-bellingham",
    "shortName": "J. Bellingham",
    "position": "M",
    "userCount": 164500,
    "id": 991011
  },
  "assist1": {
    "name": "Lucas Vázquez",
    "slug": "lucas-vazquez",
    "shortName": "L. Vázquez",
    "position": "D",
    "userCount": 10567,
    "id": 142171
  }
}
```

## 3. Player Stats Model

Returned via `/event/{eventId}/managers` or player profiles.

```json
{
  "player": {
    "name": "Luka Modrić",
    "slug": "luka-modric",
    "shortName": "L. Modrić",
    "position": "M",
    "jerseyNumber": "10",
    "height": 172,
    "preferredFoot": "Right",
    "userCount": 101235,
    "id": 15993,
    "country": {
      "alpha2": "HR",
      "name": "Croatia"
    }
  },
  "statistics": {
    "rating": 7.4,
    "totalPass": 52,
    "accuratePass": 48,
    "totalLongBalls": 6,
    "accurateLongBalls": 5,
    "totalCross": 2,
    "accurateCross": 1,
    "aerialWon": 1,
    "aerialLost": 0,
    "duelWon": 4,
    "duelLost": 3,
    "challengeSuccessful": 2,
    "dispossessed": 1,
    "touches": 64,
    "wasFouled": 1,
    "fouls": 0,
    "minutesPlayed": 90
  }
}
```
