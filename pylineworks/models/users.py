#!/usr/bin/env python3

from pylineworks.core.response import Record


class Users(Record):
    """User Object
    """
    def __init__(self, values, api, endpoint) -> None:
        super().__init__(values, api, endpoint)
        self.fullName = "{} {}".format(
            self.userName["lastName"], self.userName["firstName"])
