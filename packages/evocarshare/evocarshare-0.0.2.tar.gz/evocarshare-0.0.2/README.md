# Evocarshare-py

![https://github.com/jazzz/evocarshare-py/actions/workflows/main-build.yml/badge.svg](https://github.com/jazzz/evocarshare-py/actions/workflows/main-build.yml/badge.svg)
![Status](https://img.shields.io/badge/Project_status-Alpha-orange)

Evocarshare is a module for accessing the data api of the Evo CarShare service which streamlines token management, and queries.

## Installing

```
pip install evocarshare
```

## Supported Versions

- Python 3.11+

## Usage

Fetch all vehicles with range of a location
```python
import aiohttp
import os

from evocarshare import CredentialBundle, EvoApi

API_KEY = os.environ.get("EVOAPI_KEY")
CLIENT_ID = os.environ.get("EVOAPI_CLIENTID")
CLIENT_SECRET = os.environ.get("EVOAPI_CLIENTSECRET")

async with aiohttp.ClientSession() as client_session:
    # Initialize Api
    creds = CredentialBundle(API_KEY, CLIENT_ID, CLIENT_SECRET)
    api = EvoApi(client_session, creds)

    # Query Vehicles
    steam_clock = GpsCoord(latitude=49.284407, longitude=-123.108876)
    vehicles = await api.get_vehicles_within(meters=500, of=steam_clock)

    for v in vehicles:
        print(v)
```


## Quick Start (Dev Containers)

This project supports containerized development via [devcontainers](https://code.visualstudio.com/docs/remote/containers). From Visual Studio Code select `Devcontainers: Reopen in Container` from the command palette


## Quick Start (Poetry)

Install dependencies via poetry
```
poetry install --with dev
```

Install precommit hooks
```
poetry run pre-commit install --install-hooks
```

Run tests
```
 .venv/bin/pytest
```

## Thanks
This project makes heavy use of the reverse engineering work by @jeremy21212121 and @jack-madison.

[evofinder.ca](https://github.com/jeremy21212121/evo-client-nuxt) - Unoffical web interface for Evo

[EvoAppScrape](https://github.com/jack-madison/Evo-Car-Share-App-Scrape/blob/main/evo_app_scrape.py) - Script to extract vehicle data to `csv`

## Contributing
Contributions via PR are welcome.
