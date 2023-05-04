#!/usr/bin/env python3

import pytest
from tests import env
import pylineworks

api = pylineworks.api(env.CLIENT_ID, env.CLIENT_SECRET, env.SERVICE_ACCOUNT,
                      env.PRIVATE_KEY, "user.read")


@pytest.fixture(scope="module")
def created_user():
    # TODO: Now I don't have authority for user
    # user = api.users.users.create(
    #     domainId=env.DOMAIN_ID,
    #     email="test_users@test.com",
    #     userName={"userName": {
    #         "lastName": "ワークス",
    #         "firstName": "太郎"
    #     }},
    # )
    # yield user
    # api.users.users.delete([user.userId])
    return


class TestUsers:
    # def test_create(self, created_user):
    #     assert created_user
    #     assert created_user.userId

    def test_all(self):
        users = api.users.users.all()
        assert users is not None
        assert len(users) > 0

    # def test_get(self, created_user):
    #     user = api.users.users.get(created_user.userId)
    #     assert user is not None
    #     assert user.userId == created_user.userId

    # def test_update(self, created_user):
    #     created_user.email = "test_user_update@test.com"
    #     ret = api.users.users.update(created_user)
    #     assert ret
    #     user = api.users.users.get(created_user.userId)
    #     assert user.email == "test_user_update@test.com"
