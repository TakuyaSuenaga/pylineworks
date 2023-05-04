#!/usr/bin/env python3

from pylineworks.core.response import Record


class Calendars(Record):
    """Calendar Object
    """
    def __repr__(self) -> str:
        return self.calendarName
