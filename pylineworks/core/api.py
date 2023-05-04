#!/usr/bin/env python3

import requests
import jwt
from datetime import datetime
from pylineworks.core.app import App


class Api:
    """The API object is the point of entry
    """

    def __init__(self,
                 client_id=None,
                 client_secret=None,
                 service_account=None,
                 private_key=None,
                 scope=None) -> None:
        """
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.service_account = service_account
        self.private_key = private_key
        self.scope = scope
        self.base_url = "https://www.worksapis.com/v1.0/"
        self.http_session = requests.Session()
        self.auth = self._authenticate(
            client_id, client_secret, service_account,
            private_key, scope)
        self.access_token = self.auth["access_token"]
        self.bots = App(self, "bots")
        self.users = App(self, "users")
        self.boards = App(self, "boards")
        self.calendars = App(self, "calendars")

    def _authenticate(
            self, client_id, client_secret, service_account,
            private_key, scope):
        """Service Account Authentication (JWT)
        """
        claim_set = {
            "iss": client_id,
            "sub": service_account,
            "iat": datetime.now().timestamp(),
            "exp": datetime.now().timestamp() + 60 * 60
        }

        assertion = jwt.encode(
            claim_set,
            private_key,
            algorithm="RS256"
        )

        params = {
            'assertion': assertion,
            'grant_type': "urn:ietf:params:oauth:grant-type:jwt-bearer",
            'client_id': client_id,
            'client_secret': client_secret,
            'scope': scope
        }

        response = getattr(self.http_session, "post")(
            "https://auth.worksmobile.com/oauth2/v2.0/token", params)
        if not response.json().get("access_token"):
            raise Exception("{}".format(response.json()))
        return response.json()
