#!/usr/bin/env python3

from pylineworks.core.response import Record


class Bots(Record):
    """Bot Object
    """
    def __repr__(self) -> str:
        return self.botName
