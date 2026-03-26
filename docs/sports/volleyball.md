# Volleyball Endpoints

Volleyball maps standard event and tournament data via the generic `volleyball` slug across all endpoints.

## Core Navigation
* **Sport Slug:** `volleyball`
* **Global Support:** Full generic support (`api.sofascore.com/api/v1/event/{eventId}`).

## Sport-Specific Quirks
* Scoring is formatted as sets dynamically mapped across periods (`period1`, `period2`, `period3`, `period4`, `period5`).
* Match flow graphs (`/event/{eventId}/graph`) highlight set momentum dynamically similar to the tennis point-by-point flows.
