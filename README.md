# pylineworks
Python API client library for lineworks

> **Note:** This library only supports LINEWORKS API 2.0
> **Note:** This library is not fully comprehensive.

## Installation

To install run `pip install git+https://github.com/takuyasuenaga/pylineworks.git`.

Alternatively, you can clone the repo and run `python setup.py install`.

## Quick Start

To begin, import pylineworks and instantiate the API.

```python
import pylineworks
lw = pylineworks.api(
    "Client ID", "Client Secret", "Service Account", "Private Key", "Scope"
)
```

## Queries

The pylineworks API is setup so that LINEWORKS API are attributes of the `.api()` object. and in turn those apps have attribute representing each endpoint. Each endpoint has a handful of methods available to carry out actions on the endpoint.

```python
>>> bots = lw.bots.bot.all()
>>> print(list(bots))
['Example bot']
>>> for bot in bots:
...     print(bot.botName)
Example bot
```

```python
>>> from pprint import pprint
>>> bot = lw.bots.bot.get(2000001)
>>> pprint(dict(bot))
{
    "botId": 2000001,
    "botName": "Example bot",
    "photoUrl": "https://example.com/favicon.png",
    "description": "WorksMobile's A.I. conversation enabled bot",
    ...
}
>>> bot.description = "Update description"
>>> bot.save()
True
>>> 
```

## List of supported APIs

|App       |Endpoint  |method |HTTP Request                   |
|----------|----------|-------|-------------------------------|
|bots      |bots      |all    |GET /bots                      |
|          |          |get    |GET /bots/{botId}              |
|          |          |create |POST /bots                     |
|          |          |update |PATCH /bots/{botId}            |
|          |          |delete |DELETE /bots/{botId}           |
|users     |users     |all    |GET /users                     |
|          |          |get    |GET /users/{userId}            |
|boards    |boards    |all    |GET /boards                    |
|          |          |get    |GET /boards/{boardId}          |
|          |          |create |POST /boards                   |
|          |          |update |PUT /boards/{boardId}          |
|          |          |delete |DELETE /boards/{boardId}       |
|calendars |calendars |all    |GET /calendars                 |
|          |          |get    |GET /calendars/{calendarId}    |
|          |          |create |POST /calendars                |
|          |          |update |PATCH /calendars/{calendarId}  |
|          |          |delete |DELETE /calendars/{calendarId} |

## Build development environment

Installing rust for build cryptography

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

## Run test

Move into the `tests` directory and make a copy of `.env_example` named `.env`.
This file will hold all of your LINEWORKS parameters.

```sh
pip install dotenv
pip install pytest
pytest
```
