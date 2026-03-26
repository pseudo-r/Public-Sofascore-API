# 🏐 Volleyball Endpoints

> International and regional volleyball.

**Sport slug:** `volleyball`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/volleyball/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/volleyball/unique-tournaments` | GET | None | None |
| `/tournament/{id}/season/{seasonId}/standings/total` | GET | `{tournamentId}`, `{seasonId}` | None |

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (sets, teams, time, status) | None |
| `/statistics` | Detailed match stats (aces, blocks, digs) | None |
| `/incidents` | Match timeline | None |
| `/graph` | Point differential momentum graph | None |

---

## Team Endpoints

> Pattern: `https://api.sofascore.com/api/v1/team/{teamId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core team profile |
| `/players` | Active roster |
| `/events/next` | Upcoming matches |

---

## Athlete / Player Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core player profile |

---

## Sport-Specific Quirks

### 1. Set Scoring (Periods)
Volleyball scoring dynamically maps sets across sequential `period` properties. A 5-set match will push through `period5`.

```json
"homeScore": {
  "current": 3,
  "display": 3,
  "period1": 25,
  "period2": 19,
  "period3": 25,
  "period4": 25,
  "normaltime": 3
}
```

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Volleyball matches scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/volleyball/scheduled-events/2026-03-26"

# Get Volleyball Match Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11995810"
```
