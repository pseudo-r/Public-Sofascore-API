# 🏈 American Football Endpoints

> NFL, NCAA College Football, and CFL.

**Sport slug:** `american-football`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/american-football/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/american-football/unique-tournaments` | GET | None | None |
| `/tournament/{id}/season/{seasonId}/standings/total` | GET | `{tournamentId}`, `{seasonId}` | None |

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (quarters, teams, time, status) | None |
| `/statistics` | Detailed match stats (passing yards, rushing) | None |
| `/incidents` | Match timeline (touchdowns, field goals, flags) | None |
| `/graph` | Point differential momentum graph | None |

---

## Team Endpoints

> Pattern: `https://api.sofascore.com/api/v1/team/{teamId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core team profile, colors, venue |
| `/players` | Active roster including offense/defense separation |
| `/events/next` | Upcoming scheduled matches |

---

## Athlete / Player Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core player profile, height/weight |
| `/statistics/seasons` | Historical career stats |

---

## Sport-Specific Quirks

### 1. Match Scoring (Quarters)
Similar to basketball, scoring data is explicitly split across 4 periods (quarters).

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
The standard `/event/{eventId}/incidents` primarily acts as a scoring summary (Touchdowns, Field Goals, Safeties).
*Note:* Deeper textual play-by-plays (every snap and down sequence) rely on the live statistical tracking updates.

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all NFL matches scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/american-football/scheduled-events/2026-03-26"

# Get NFL Match Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11843210"

# Get NFL Match Statistics
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11843210/statistics"
```
