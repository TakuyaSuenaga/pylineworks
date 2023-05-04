#!/usr/bin/env python3

import json


class RequestError(Exception):
    """Basic Request Exception
    """

    def __init__(self, req) -> None:
        super().__init__(req)
        self.req = req
        self.body = self.req.request.body
        self.base = self.req.url
        self.error = self.req.text

    def __str__(self):
        return self.error


class ContentError(Exception):
    """Content Exception
    """

    def __init__(self, req) -> None:
        super().__init__(req)
        self.req = req
        self.body = self.req.request.body
        self.base = self.req.url
        self.error = (
            "The server returned invalid (non-json) data."
        )

    def __str__(self) -> str:
        return self.error


class Request:
    """Creates requests to LINEWORKS API

    :param base: (str) Base URL
    :param key: (int|str) Object ID
    :param token: (str) Access Token
    """

    def __init__(
            self,
            base,
            http_session,
            add_params=None,
            token=None,
            key=None
    ) -> None:
        self.base = base
        self.url = base if not key else f"{base}/{key}"
        self.http_session = http_session
        self.add_params = add_params
        self.token = token
        self.key = key

    def _make_call(self, verb='get', add_params=None, data=None,
                   url_override=None):
        headers = {"Authorization": f"Bearer {self.token}"}
        if verb in ("post", "put", "patch"):
            headers.update({"Content-Type": "application/json"})

        params = {}

        req = getattr(self.http_session, verb)(
            url_override or self.url, headers=headers, params=params, json=data
        )

        if verb == "delete":
            if req.ok:
                return True
            else:
                raise RequestError(req)
        elif req.ok:
            try:
                return req.json()
            except json.JSONDecodeError:
                raise ContentError(req)
        else:
            raise RequestError(req)

    def get(self, name="name", add_params=None):
        """Makes a GET request
        """
        req = self._make_call(verb='get', add_params=add_params)
        if isinstance(req, dict):
            if req.get(name):
                self.count = len(req[name])
                for i in req[name]:
                    yield i
                while req["responseMetaData"]["nextCursor"]:
                    req = self._make_call(
                        url_override=req["responseMetaData"]["nextCursor"])
                    for i in req[name]:
                        yield i
            else:
                yield req
        else:
            yield req

    def post(self, data):
        """Makes POST request.

        :param data: (dict) Contains a dict
        """
        return self._make_call("post", data=data)

    def delete(self):
        """Makes DELETE request.

        :param data: (dict) Contains a dict
        """
        return self._make_call("delete")

    def patch(self, data):
        """Makes PATCH request.

        :param data: (dict) Contains a dict
        """
        return self._make_call("patch", data=data)

    def put(self, data):
        """Makes PUT request.

        :param data: (dict) Contains a dict
        """
        return self._make_call("put", data=data)
