# ⛳ Golf Endpoints

> PGA, LIV, European Tour, Majors.

**Sport slug:** `golf`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/golf/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/golf/unique-tournaments` | GET | None | None |

---

## Event (Tournament) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core tournament details (course info, par, prize) | None |
| `/standings` | Leaderboard (strokes, thru holes, to par) | None |

---

## Athlete / Golfer Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core golfer profile |
| `/statistics/seasons` | FedEx Cup rank, historical finishes |

---

## Sport-Specific Quirks

### 1. Leaderboard Centric
Single matches (individual events) replace the standard `homeTeam` vs `awayTeam` paradigm with a massive tournament leaderboard.
The `standings` block drives score tracking (tracking distinct scores per hole across 4 rounds).

### 2. Relative Par Scoring
Responses favor rendering scores relative to Par (e.g., `-12`) inside the `position` objects next to the absolute stroke total.

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Golf events scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/golf/scheduled-events/2026-03-26"

# Get PGA Tour Leaderboard block
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11995810"
```
