# Sofascore Python Service

This provides the reference Python proxy service utilizing Django REST Framework to access Sofascore APIs securely by bypassing standard WAF defenses using `curl_cffi`.

## Installation

Ensure you have Python 3.12+ installed.

```bash
python -m venv venv
venv\Scripts\activate
pip install -e ".[dev]"
```

## Running the API

```bash
python manage.py runserver
```

## Available Proxy Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/sofascore/event/{id}/` | GET | Fetch Sofascore event details using Chromium TLS bypass |
| `/api/v1/sofascore/team/{id}/` | GET | Fetch Sofascore team profile |
| `/api/v1/sofascore/schedule/{sport}/{date}/` | GET | Fetch Sofascore scheduled events by sport and date |

## Client

The core request logic bypassing the API defense is contained natively within `clients/sofascore_client.py`.
