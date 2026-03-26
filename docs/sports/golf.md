# Golf Endpoints

Golf tournaments leverage the broader tournament framework on Sofascore under the `golf` slug.

## Core Navigation
* **Sport Slug:** `golf`
* **Global Support:** Event discovery matches the global model, but player payloads differ.

## Sport-Specific Quirks
* Single matches (individual events) replace the `homeTeam/awayTeam` model with a `competitors` array or full tournament leaderboard object tracking distinct scores per hole across 4 rounds.
