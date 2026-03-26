# 🏏 Cricket Endpoints

> ICC, IPL, The Hundred, Big Bash, and Test variants.

**Sport slug:** `cricket`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/cricket/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/cricket/unique-tournaments` | GET | None | None |

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (innings, wickets, runs, status) | None |
| `/statistics` | Batting, Bowling, and Fielding metrics | None |
| `/incidents` | Match timeline (Overs, Wickets, Boundaries) | None |

---

## Team Endpoints

> Pattern: `https://api.sofascore.com/api/v1/team/{teamId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core team profile |
| `/players` | Active squad |
| `/events/next` | Upcoming matches |

---

## Athlete / Player Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core player profile, batting style, bowling style |
| `/statistics/seasons` | Historical career stats (Test, ODI, T20) |

---

## Sport-Specific Quirks

### 1. Inning Scoring (Periods & Wickets)
The `/event/{id}` payload fundamentally alters generic score tracking. It injects nested configurations for runs vs wickets fallen. `period1` typically translates to the 1st Inning block.

### 2. Overs & Targeting
Special properties like `target` runs and `overs` progress update dynamically in live payloads within the `homeScore` or `awayScore` blocks.

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Cricket matches scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/cricket/scheduled-events/2026-03-26"

# Get Cricket Match Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11995810"
```
