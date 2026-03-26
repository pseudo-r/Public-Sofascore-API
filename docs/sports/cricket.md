# Cricket Endpoints

Cricket on Sofascore follows the standard `_global.md` schema but injects complex scoring payloads to track innings, wickets, and runs.

## Core Navigation
* **Sport Slug:** `cricket`
* **Global Support:** Full support for standard global Event, Team, and Player queries.

## Sport-Specific Quirks
* The `/event/{id}` payload includes specific nested arrays tracking runs per over, total wickets fallen, and target scores.
* Depending on the format (T20, ODI, Test), the `"period1"` and `"period2"` representations map directly to the corresponding innings.
