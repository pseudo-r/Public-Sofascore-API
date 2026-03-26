# 🏒 Ice Hockey Endpoints

> NHL, KHL, SHL, and international leagues.

**Sport slug:** `ice-hockey`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/ice-hockey/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/ice-hockey/unique-tournaments` | GET | None | None |
| `/tournament/{id}/season/{seasonId}/standings/total` | GET | `{tournamentId}`, `{seasonId}` | None |

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (teams, time, status, scores) | None |
| `/statistics` | Detailed match stats (hits, shots on goal) | None |
| `/incidents` | Match timeline (goals, penalties) | None |
| `/lineups` | Lines and goaltenders | None |
| `/graph` | Point differential momentum graph | None |

---

## Team Endpoints

> Pattern: `https://api.sofascore.com/api/v1/team/{teamId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core team profile, stadium, colors |
| `/players` | Active roster |
| `/events/next` | Upcoming scheduled matches |

---

## Athlete / Player Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core player profile, position |
| `/statistics/seasons` | Historical career stats |

---

## Sport-Specific Quirks

### 1. Match Scoring (Periods)
Hockey natively divides the game into 3 periods cleanly mapped in the response.

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
If a match exceeds normal time, the payload natively conditionally injects `overtime` and `penalties` root objects alongside the standard 3 period keys.

### 3. Match Incidents
Unlike football's simple yellow/red card schema, the `/event/{eventId}/incidents` payload explicitly tracks hockey penalty minutes (2m, 5m, 10m) utilizing the `incidentClass` and `incidentType` keys in tandem.

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Hockey matches scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/ice-hockey/scheduled-events/2026-03-26"

# Get NHL Match Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11995810"

# Get NHL Match Lineups (Lines)
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11995810/lineups"
```
