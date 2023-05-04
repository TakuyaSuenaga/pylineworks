#!/usr/bin/env python3

import pytest
from tests import env
import pylineworks


api = pylineworks.api(env.CLIENT_ID, env.CLIENT_SECRET, env.SERVICE_ACCOUNT,
                      env.PRIVATE_KEY, "bot")


@pytest.fixture(scope="module")
def created_bot():
    bot = api.bots.bots.create(
        botName="Test Create",
        photoUrl="https://static.worksmobile.net/static/"
                 "pwe/wm/devcenter/img_linebot.png",
        description="Test Create",
        administrators=[env.ADMINISTRATOR]
    )
    yield bot
    api.bots.bots.delete([bot.botId])


class TestBots:
    def test_create(self, created_bot):
        assert created_bot
        assert created_bot.botId

    def test_all(self):
        bots = api.bots.bots.all()
        assert bots is not None
        assert len(bots) > 0

    def test_get(self, created_bot):
        bot = api.bots.bots.get(created_bot.botId)
        assert bot is not None
        assert bot.botId == created_bot.botId

    def test_update(self, created_bot):
        created_bot.description = "updated description"
        ret = api.bots.bots.update(created_bot)
        assert ret
        bot = api.bots.bots.get(created_bot.botId)
        assert bot.description == "updated description"
