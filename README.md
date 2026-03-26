<!-- GitAds-Verify: 44FZ4IWPYGNOY6XFRMCK946T5LOIFT23 -->

# Sofascore Public API Documentation

**Disclaimer:** This is documentation for Sofascore's undocumented internal public API. I am not affiliated with Sofascore. Use responsibly and respect rate limits.



---

## ☕ Support This Project

If this API documentation saved you hours of debugging TLS fingerprinting, please consider supporting the project:

| Platform | Link |
|----------|------|
| ☕ Buy Me a Coffee | [buymeacoffee.com/pseudo_r](https://buymeacoffee.com/pseudo_r) |
| 💖 GitHub Sponsors | [github.com/sponsors/Kloverdevs](https://github.com/sponsors/Kloverdevs) |
| 💳 PayPal Donate | [PayPal (CAD)](https://www.paypal.com/donate/?business=H5VPFZ2EHVNBU) |

## Table of Contents

- [Overview](#overview)
- [Base Domains](#base-domains)
- [Versioned Endpoints](#versioned-endpoints)
- [Search / Discovery Endpoints](#search--discovery-endpoints)
- [Event / Match Endpoints](#event--match-endpoints)
- [Player Endpoints](#player-endpoints)
- [Team Endpoints](#team-endpoints)
- [Tournament / Standings Endpoints](#tournament--standings-endpoints)
- [Sport-Specific Endpoint Notes](#sport-specific-endpoint-notes)
- [Additional Domains / Endpoint Families](#additional-domains--endpoint-families)
- [Notes / Quirks](#notes--quirks)
- [Repository Updates Made](#repository-updates-made)
- [Django API Changes Made](#django-api-changes-made)
- [Remaining Gaps / Unknowns](#remaining-gaps--unknowns)

---

## Overview

The Sofascore web platform is heavily driven by a robust, unified JSON API backend. Unlike ESPN, which historically separated core stats from frontend routing, Sofascore uses a clean REST-like `api.sofascore.com` service that scales smoothly from match discovery down to player-level granular statistics (like point-by-point graphs).

> **Important Quirks:**
> *   **WAF / TLS Fingerprinting:** Basic cURL or `requests` in Python will return a `403 Forbidden`. You **must** spoof TLS fingerprints (e.g., via `curl_cffi` in Python).
> *   **Rate Limiting:** Aggressive. Scrape responsibly.

---

## Base Domains

| Domain | Status | Purpose |
|--------|--------|---------|
| `api.sofascore.com` | **PRIMARY** | The main data driver. All modern App/Web JSON flows here. |
| `api.sofascore.app` | **MIRROR** | A secondary/alternate domain that mirrors the exact v1 API payloads of the primary domain. Used potentially as a fallback or origin bypass. Returns HTTP 200 using the same endpoints. |
| `www.sofascore.com/api` | **PROXY** | Often used interchangeably on the web app; proxies directly to `api.sofascore.com`. |

## Versioned Endpoints (v1 / v2 / v3 / legacy)

Extensive deep searches and fuzzing Python scripts reveal the following status for API routes:

| Version Route | Status | Notes |
|---------------|--------|-------|
| `/api/v1/` | **VERIFIED** | The absolute core of Sofascore data. Used for 99% of endpoints. |
| `/api/v2/` | **DEFUNCT/404** | Tested combinations. Returns 404 Not Found. Tested across 15+ core data endpoints (events, players, stats, graphs) - all return 404 globally. |
| `/api/v3/` | **DEFUNCT/404** | Tested combinations. Returns 404 Not Found. Tested across 15+ core data endpoints (events, players, stats, graphs) - all return 404 globally. |
| `/mobile/v4/` | **DEFUNCT/404** | Tested combinations. Returns 404 Not Found. |

*Conclusion:* An exhaustive test matrix against 16 core endpoints verified that Sofascore heavily protects its mobile paths or has fully unified its mobile and web data pipelines exclusively into the `v1` REST-like architecture.

---

## Search / Discovery Endpoints

### 1. Global Config & Popular Entities
* **Endpoint:** `https://api.sofascore.com/api/v1/config/popular-entities/{locale}` (e.g., `US`)
* **Method:** GET
* **Version:** v1
* **Verification Status:** VERIFIED
* **Example Request:**
  `curl -H "User-Agent: Mozilla/5.0" "https://api.sofascore.com/api/v1/config/popular-entities/US"`
* **Notes:** Used by the homepage to load local favorites (leagues/sports based on region).

---

## Event / Match Endpoints

Most match data hangs off the generic `{eventId}` model.

### 1. Event Details
* **Endpoint:** `https://api.sofascore.com/api/v1/event/{eventId}`
* **Method:** GET
* **Verification Status:** VERIFIED
* **Example Response (Trimmed):**
```json
{"event": {"tournament": {"name": "World Cup Qual. UEFA Playoffs", "slug": "world-championship-qual-uefa-playoffs"} ...}}
```

### 2. Match Statistics
* **Endpoint:** `https://api.sofascore.com/api/v1/event/{eventId}/statistics`
* **Method:** GET
* **Verification Status:** VERIFIED
* **Notes:** Returns all major stats (possession, shots, passes).

### 3. Match Incidents
* **Endpoint:** `https://api.sofascore.com/api/v1/event/{eventId}/incidents`
* **Method:** GET
* **Verification Status:** VERIFIED
* **Notes:** Timeline array of cards, goals, subs.

### 4. Match Lineups
* **Endpoint:** `https://api.sofascore.com/api/v1/event/{eventId}/lineups`
* **Method:** GET
* **Verification Status:** VERIFIED

### 5. Momentum Graph Data
* **Endpoint:** `https://api.sofascore.com/api/v1/event/{eventId}/graph`
* **Method:** GET
* **Verification Status:** VERIFIED

---

## Player Endpoints

### 1. Player Profile
* **Endpoint:** `https://api.sofascore.com/api/v1/player/{playerId}`
* **Method:** GET
* **Verification Status:** VERIFIED

### 2. Player Career Stats By Season
* **Endpoint:** `https://api.sofascore.com/api/v1/player/{playerId}/statistics/seasons`
* **Method:** GET
* **Verification Status:** VERIFIED

---

## Team Endpoints

### 1. Team Profile & Roster
* **Endpoint:** `https://api.sofascore.com/api/v1/team/{teamId}`
* **Endpoint (Squad):** `https://api.sofascore.com/api/v1/team/{teamId}/players`
* **Method:** GET
* **Verification Status:** VERIFIED
* **Example Response (Players):**
```json
{"players": [{"player": {"name": "Kenan Yıldız", "slug": "yildiz-kenan", "team": {"name": "Juventus"}}} ...]}
```

---

## Tournament / Standings Endpoints

### 1. Daily Scheduled Events (Football)
* **Endpoint:** `https://api.sofascore.com/api/v1/sport/{sport}/scheduled-events/{date}`
* **Method:** GET
* **Verification Status:** VERIFIED
* **Required Params:** `sport` (e.g. `football`), `date` (e.g. `2026-03-26`)

### 2. Unique Tournaments Configuration
* **Endpoint:** `https://api.sofascore.com/api/v1/sport/{sport}/unique-tournaments`
* **Method:** GET
* **Verification Status:** VERIFIED
* **Notes:** Lists all tournaments for a sport.

## Parameters Reference

### Path Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `{eventId}` | Integer | Unique identifier for a match/event. Look this up via the scheduled events endpoint. | `11352523` |
| `{teamId}` | Integer | Unique identifier for a team across any sport. | `4705` |
| `{playerId}` | Integer | Unique identifier for an athlete. | `814123` |
| `{sport}` | String | lowercase slug identifying the sport category. | `football` |
| `{date}` | String | ISO-8601 date format for scheduling lookups. | `2024-03-26` |
| `{page}` | Integer | Pagination parameter, commonly required for scheduled tennis tournaments and rankings. | `1` |
| `{locale}` | String | Country code for configuration fetching. | `US`, `GB` |

### Common Sport Slugs (`{sport}`)

| Sport | Slug |
|-------|------|
| Soccer / Football | `football` |
| Tennis | `tennis` |
| Basketball | `basketball` |
| Ice Hockey | `ice-hockey` |
| American Football | `american-football` |
| Baseball | `baseball` |
| Esports | `esports` |
| Table Tennis | `table-tennis` |

---

## Sport-Specific Endpoint Notes

### Tennis
* **Endpoint Variant:** Tennis uses `scheduled-tournaments` instead of `scheduled-events`.
  `https://api.sofascore.com/api/v1/sport/tennis/scheduled-tournaments/{date}/page/{page}`
* **Tennis Power:** `https://api.sofascore.com/api/v1/event/{eventId}/tennis-power` (replaces the football momentum graph).
* **Point-by-Point:** `https://api.sofascore.com/api/v1/event/{eventId}/point-by-point`

### Football / Soccer
* Contains specific subsets for Managers `.../event/{eventId}/managers` and Player characteristics.

### Esports
* Matches mostly follow the standard `{eventId}` models, though incidents translate differently (e.g., kills/towers instead of goals/cards).

---

## Additional Domains / Endpoint Families

1. **`api.sofascore.com/api/v1/config/`**
   - **Purpose:** Startup configurations, translations, and locale-based popular groupings.
   - **Status:** Current (VERIFIED).
2. **`api.sofascore.com/api/v1/sport/`**
   - **Purpose:** Broad daily schedules and routing.
   - **Status:** Current (VERIFIED).

---

## Notes / Quirks

* **WAF Enforcement:** Sofascore aggressively drops connections or sends `403 Forbidden` if your HTTP client lacks valid TLS fingerprints matching modern browsers.
* **Pagination:** Used heavily in schedules (e.g., tennis schedules explicitly require `/page/1`).
* **Image Delivery:** Typically CDN-delivered off a separate domain, not directly via API JSON payloads.

---

## Repository Updates Made

- `README.md` created matching the ESPN standard and comprehensive work log requirements.
- `CHANGELOG.md` created tracking v1.0 reverse engineering.
- `CONTRIBUTING.md` created to match organizational standards.
- Detailed endpoints added natively inside the repo.

---

## Django API Changes Made

- **`Public-Sofascore-API/sofascore_service`:** Created a dedicated standalone Django REST Framework service natively in this repository specifically to wrap and serve the endpoints through Python proxy views.
- **`clients/sofascore_client.py`:** Contains the robust Chrome-impersonated `curl_cffi` HTTP client which inherently maps and solves the TLS Fingerprinting requirements automatically for any application requesting `get_event_details()`, `get_team()`, or `get_scheduled_events()`.

### Sofascore Service (Django Proxy Implementation)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/sofascore/event/{id}/` | GET | Fetch Sofascore event details |
| `/api/v1/sofascore/team/{id}/` | GET | Fetch Sofascore team profile |
| `/api/v1/sofascore/schedule/{sport}/{date}/` | GET | Fetch Sofascore scheduled events globally |

See [`sofascore_service/README.md`](sofascore_service/README.md) for full service API documentation and running the Docker containers.

---

## Remaining Gaps / Unknowns

- **Authentication Endpoints:** User login/preferences flows are unexplored.
- **WebSocket Feeds:** Unknown if real-time game logs drop over WebSockets or rapid XHR polling. (Initial research suggests XHR polling).
- **Historical Data Limits:** How far back season logs go for minor leagues is undetermined.
