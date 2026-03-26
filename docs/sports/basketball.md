# 🏀 Basketball

> NBA, WNBA, NCAA, FIBA, and international leagues.

**Sport slug:** `basketball`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/basketball/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/basketball/unique-tournaments` | GET | None | None |
| `/tournament/{id}/season/{seasonId}/standings/total` | GET | `{tournamentId}`, `{seasonId}` | None |

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (teams, time, status, scores) | None |
| `/statistics` | Detailed match stats (FG, 3PT, rebounds, TOs) | None |
| `/incidents` | Match timeline (fouls, timeouts, quarters) | None |
| `/lineups` | Starting 5 and bench | None |
| `/graph` | Point differential momentum graph | None |

---

## Team Endpoints

> Pattern: `https://api.sofascore.com/api/v1/team/{teamId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core team profile, colors, venue |
| `/players` | Active roster with player IDs |
| `/performance` | Form guide and streak data |
| `/events/next` | Upcoming scheduled matches |

---

## Athlete / Player Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core player profile, position, nationality |
| `/statistics/seasons` | Historical career stats mapped by season |

---

## Sport-Specific Quirks

### 1. Match Scoring (Quarters & Overtime)
Unlike football halves, basketball `event` responses chunk scoring dynamically into quarters inside the `homeScore` and `awayScore` objects. Overtime periods seamlessly append as `overtime1`, `overtime2`.

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

### 2. Match Statistics
The `/event/{eventId}/statistics` endpoint natively supports deep basketball metrics:
* Field Goals (Made/Attempted)
* 3 Pointers (Made/Attempted)
* Free Throws
* Rebounds (Defensive/Offensive)
* Turnovers / Steals / Blocks

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Basketball matches scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/basketball/scheduled-events/2026-03-26"

# Get NBA Match Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11550211"

# Get LA Lakers Team Profile (teamId: 3423)
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/team/3423"

# Get LeBron James Player Profile (playerId: 112341)
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/player/112341"
```
