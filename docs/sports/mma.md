# 🥊 MMA / Combat Sports Endpoints

> UFC, Bellator, PFL, ONE Championship.

**Sport slug:** `mma`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/mma/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/mma/unique-tournaments` | GET | None | None |

---

## Event (Fight) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core fight details (fighters, weight class, rounds) | None |
| `/incidents` | Fight timeline (knockdowns, submissions) | None |

---

## Athlete / Fighter Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core fighter profile (record, reach, height/weight) |
| `/events/last` | Last fought matches (fight record) |

---

## Sport-Specific Quirks

### 1. Pseudo-Teams
Fighters are mapped purely to the `homeTeam` and `awayTeam` nodes inside the `eventId` payload. The `teamId` often acts identically to the `playerId`.

### 2. Elimination of Period Scoring
There is no period-by-period scoring payload; match lengths/rounds are denoted in the final status or incident summary strings rather than a mathematical score integer (unless judging points are forced).

### 3. Stat limitations
MMA on Sofascore inherits the standard `_global.md` schema, though it bypasses deep statistical integration natively (relying strictly on incidents for outcomes like KOs/Submissions instead of tracking strikes landed/thrown).

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all MMA fights scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/mma/scheduled-events/2026-03-26"

# Get UFC Fight Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11995810"
```
