# 🎾 Tennis

> ATP, WTA, Challenger, and ITF tournaments worldwide.

**Sport slug:** `tennis`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/tennis/scheduled-tournaments/{date}/page/{page}` | GET | `{date}`, `{page}` | None |
| `/sport/tennis/unique-tournaments` | GET | None | None |
| `/tournament/{id}/season/{seasonId}/standings/total` | GET | `{tournamentId}`, `{seasonId}` | None |

> ⚠️ **Note:** Tennis scheduling uniquely groups by `scheduled-tournaments` rather than raw events natively, and it *requires* pagination (`/page/1`).

---

## Event (Match) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core event details (players, time, status, scores) | None |
| `/statistics` | Detailed match stats (aces, double faults, break pts) | None |
| `/incidents` | Match timeline (breaks, medical timeouts) | None |
| `/point-by-point` | **Unique:** Tracks every single point scored in the match | None |
| `/tennis-power` | **Unique:** Momentum graph replacing standard pressure | None |

---

## Player Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core player profile, world rank |
| `/events/next` | Upcoming tennis matches |
| `/events/last` | Last played matches |
| `/rankings` | ATP/WTA ranking history |

---

## Sport-Specific Quirks

### 1. Tennis Power vs Graph
Football uses `/graph` for momentum. Tennis uses the highly specific `/tennis-power` endpoint to track momentum swings across sets.

### 2. Set Scoring
Tennis sets are individually mapped onto the `period` arrays.

```json
"homeScore": {
  "current": 2,
  "display": 2,
  "period1": 6,
  "period2": 4,
  "period3": 7,
  "normaltime": 2
}
```

### 3. Point-by-Point
The `/point-by-point` endpoint offers unparalleled granularity, explicitly breaking down ties, aces, and faults per game per set.

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Tennis tournaments scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/tennis/scheduled-tournaments/2026-03-26/page/1"

# Get Match Details (Wimbledon Final)
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11456123"

# Get Point-by-Point Data
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11456123/point-by-point"

# Get Carlos Alcaraz Player Profile (playerId: 245123)
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/player/245123"
```
