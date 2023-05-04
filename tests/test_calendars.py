#!/usr/bin/env python3

import pytest
from tests import env
import pylineworks


api = pylineworks.api(env.CLIENT_ID, env.CLIENT_SECRET, env.SERVICE_ACCOUNT,
                      env.PRIVATE_KEY, "calendar")


@pytest.fixture(scope="module")
def created_calendar():
    calendar = api.calendars.calendars.create(
        calendarName="Test Create Calendar",
        description="Test Create Calendar",
        members=[{"id": env.CALENDAR_MEMBER_ID,
                  "type": "USER",
                  "role": "CALENDAR_EVENT_READ_WRITE"}]
    )
    yield calendar
    api.calendars.calendars.delete([calendar.calendarId])


class TestCalendars:
    def test_create(self, created_calendar):
        assert created_calendar
        assert created_calendar.calendarId

    def test_get(self, created_calendar):
        calendar = api.calendars.calendars.get(created_calendar.calendarId)
        assert calendar is not None
        assert calendar.calendarId == created_calendar.calendarId

    def test_update(self, created_calendar):
        created_calendar.description = "updated description"
        ret = api.calendars.calendars.update(created_calendar)
        assert ret
        calendar = api.calendars.calendars.get(created_calendar.calendarId)
        assert calendar.description == "updated description"
