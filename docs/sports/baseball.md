# ⚾ Baseball Endpoints

> MLB, NPB, KBO, and minor league baseball.

**Sport slug:** `baseball`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/baseball/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/baseball/unique-tournaments` | GET | None | None |
| `/tournament/{id}/season/{seasonId}/standings/total` | GET | `{tournamentId}`, `{seasonId}` | None |

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (teams, time, status, scores) | None |
| `/statistics` | Detailed match stats (hits, errors, pitches) | None |
| `/incidents` | Match timeline (hits, runs, pitching changes) | None |
| `/graph` | Point differential momentum graph | None |

---

## Team Endpoints

> Pattern: `https://api.sofascore.com/api/v1/team/{teamId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core team profile, stadium, colors |
| `/players` | Active roster |
| `/performance` | Form guide and streak data |
| `/events/next` | Upcoming scheduled games |

---

## Athlete / Player Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core player profile, position |
| `/statistics/seasons` | Historical career stats |

---

## Sport-Specific Quirks

### 1. Inning Scoring (Periods)
The Sofascore payload natively maps innings directly onto sequentially incrementing `period` properties inside `homeScore` and `awayScore`.

```json
"awayScore": {
  "current": 4,
  "display": 4,
  "period1": 0,
  "period2": 1,
  "period3": 0,
  ...
  "period9": 0,
  "normaltime": 4
}
```

### 2. Match Incidents
The `/event/{eventId}/incidents` array tracks plays differently from traditional timed sports. Incidents log strictly by innings (`incidentType: "inning"`) or by runs scored (`incidentType: "run"`).

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Baseball matches scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/baseball/scheduled-events/2026-03-26"

# Get Match Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11679234"

# Get Baseball Play-by-Play Incidents
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11679234/incidents"
```
