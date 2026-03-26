# ⚽ Football / Soccer

> Football (Soccer) including the World Cup, Champions League, Premier League, LaLiga, Serie A, and minor regional leagues worldwide.

**Sport slug:** `football`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/football/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/football/unique-tournaments` | GET | None | None |
| `/unique-tournament/{id}/seasons` | GET | `{uniqueTournamentId}` | None |
| `/tournament/{id}/season/{seasonId}/standings/total` | GET | `{tournamentId}`, `{seasonId}` | None |

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (teams, time, status, scores) | None |
| `/statistics` | Detailed match stats (possession, shots, passes, corners) | None |
| `/incidents` | Match timeline (goals, cards, VAR, substitutions) | None |
| `/lineups` | Starting XI and bench players | None |
| `/graph` | Momentum graph (pressure over time) | None |
| `/player/{playerId}/statistics` | Specific player event ratings/heatmaps | `{playerId}` |
| `/managers` | Coaches for both teams | None |

---

## Team Endpoints

> Pattern: `https://api.sofascore.com/api/v1/team/{teamId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core team profile, colors, venue |
| `/players` | Active squad roster with player IDs |
| `/performance` | Form guide and streak data |
| `/events/next` | Upcoming scheduled matches |
| `/events/last` | Last played matches |

---

## Athlete / Player Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core player profile, position, nationality |
| `/statistics/seasons` | Historical career stats mapped by season |
| `/characteristics` | Player traits (strengths/weaknesses) |
| `/national-team-statistics` | International duty statistics |

---

## Sport-Specific Quirks

### 1. Match Scoring
Soccer halves are explicitly tracked inside the `homeScore` and `awayScore` keys in event payloads:

```json
"homeScore": {
  "current": 2,
  "display": 2,
  "period1": 1,
  "period2": 1,
  "normaltime": 2
}
```

### 2. Incidents (Cards & Goals)
The `/incidents` array explicitly distinguishes between Yellow/Red cards, Goals, and Subs. `incidentType` dictates the event, while `incidentClass` outlines the specifics (e.g., `incidentClass: "yellow"`).

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all football matches scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/football/scheduled-events/2026-03-26"

# Get Match Details (Champions League Final)
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11352523"

# Get Real Madrid Team Profile (teamId: 2829)
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/team/2829"

# Get Real Madrid Roster
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/team/2829/players"

# Get Jude Bellingham Player Profile (playerId: 991011)
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/player/991011"
```
