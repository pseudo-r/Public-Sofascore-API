# 🏉 Rugby Endpoints

> Rugby Union and Rugby League worldwide.

**Sport slug:** `rugby`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/rugby/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/rugby/unique-tournaments` | GET | None | None |
| `/tournament/{id}/season/{seasonId}/standings/total` | GET | `{tournamentId}`, `{seasonId}` | None |

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (teams, halves, points) | None |
| `/statistics` | Match stats (possession, tackles, lineouts) | None |
| `/incidents` | Match timeline (tries, conversions, penalties) | None |
| `/graph` | Point differential momentum graph | None |

---

## Team & Athlete Endpoints

> Standard `homeTeam/awayTeam` patterns (`team/{id}`) and `player/{id}` profiles strictly apply as seen in `_global.md`.

---

## Sport-Specific Quirks

### 1. Match Scoring
Scoring is divided evenly into two halves mapping onto `period1`, `period2`, mirroring the standard `football` schema.

```json
"homeScore": {
  "current": 24,
  "display": 24,
  "period1": 14,
  "period2": 10,
  "normaltime": 24
}
```

### 2. Tries vs Conversions
The `/event/{eventId}/incidents` is cleanly separated for Rugby specific logs denoting *Tries*, *Conversions*, *Penalties*, and *Drop Goals*.

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Rugby matches scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/rugby/scheduled-events/2026-03-26"

# Get Match Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11995810"
```
