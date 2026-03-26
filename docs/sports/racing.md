# 🏎️ Motorsport / Racing Endpoints

> Formula 1, MotoGP, WRC, Nascar.

**Sport slug:** `motorsport`  
**Base URL (v1):** `https://api.sofascore.com/api/v1`

---

## Daily Schedules & Tournaments

| Endpoint | Method | Required Params | Query Params |
|----------|--------|-----------------|--------------|
| `/sport/motorsport/scheduled-events/{date}` | GET | `{date}` (YYYY-MM-DD) | None |
| `/sport/motorsport/unique-tournaments` | GET | None | None |

---

## Event (Race) Endpoints

> All endpoints below follow the pattern:  
> `https://api.sofascore.com/api/v1/event/{eventId}<sub-path>`  

| Sub-path | Description | Params |
|----------|-------------|--------|
| *(root)* | Core race details (track info, laps, status) | None |
| `/standings` | Grid standings & session times | None |

---

## Athlete / Driver Endpoints

> Pattern: `https://api.sofascore.com/api/v1/player/{playerId}<sub-path>`

| Sub-path | Description |
|----------|-------------|
| *(root)* | Core driver profile |

---

## Sport-Specific Quirks

### 1. Erasing the Head-to-Head paradigm
Motorsport largely abandons the `homeTeam / awayTeam` concept used in 95% of Sofascore endpoints.
Instead, the `/event/{eventId}` payload relies almost entirely inside an extensive `standings` or `competitors` array listing drivers in positional order alongside their delta times and lap completion metrics.

### 2. Session Scopes
Qualifying, Practice, and Race Day are often configured as discrete `eventId` payloads nested inside a master tournament `stage`.

---

## Example API Calls

*Note: You must use a WAF bypass library (`curl_cffi` in Python) or attach Chrome headers to fetch these successfully.*

```bash
# Get all Motorsport events scheduled for today
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/sport/motorsport/scheduled-events/2026-03-26"

# Get Race Details
curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/event/11995810"
```
