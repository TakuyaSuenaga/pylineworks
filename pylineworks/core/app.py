#!/usr/bin/env python3

from typing import Any
from pylineworks.core.endpoint import Endpoint
from pylineworks.models import (
    bots,
    users,
    boards,
    calendars,
)


class App:
    """Represents apps in Lineworks
    """

    def __init__(self, api, name) -> None:
        self.api = api
        self.name = name
        self._setmodel()

    models = {
        "bots": {"model": bots, "namekey": "botName", "idkey": "botId"},
        "users": {"model": users, "namekey": "fullName", "idkey": "userId"},
        "boards": {"model": boards, "namekey": "boardName",
                   "idkey": "boardId"},
        "calendars": {"model": calendars, "namekey": "calendarName",
                      "idkey": "calendarId"},
    }

    def _setmodel(self):
        if self.name in App.models:
            self.model = App.models[self.name]["model"]
            self.namekey = App.models[self.name]["namekey"]
            self.idkey = App.models[self.name]["idkey"]
        else:
            self.model = None

    def __getattr__(self, name: str) -> Any:
        return Endpoint(self.api, self, name, model=self.model)
