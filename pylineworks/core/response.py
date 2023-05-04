#!/usr/bin/env python3

from pylineworks.core.query import Request


class RecordSet:
    """Iterator containing Record object.
    """

    def __init__(self, endpoint, request) -> None:
        self.endpoint = endpoint
        self.request = request
        self.response = self.request.get(self.endpoint.app.name)
        self._response_cache = []

    def __iter__(self):
        return self

    def __next__(self):
        if self._response_cache:
            values = self._response_cache.pop()
        else:
            values = next(self.response)
        return self.endpoint.return_obj(
            values, self.endpoint.api, self.endpoint)

    def __len__(self):
        try:
            return self.request.count
        except AttributeError:
            try:
                self._response_cache.append(next(self.response))
            except StopIteration:
                return 0
            return self.request.count


class Record:
    """Create Python objects from LINEWORKS API responses.

    :examples:

    >>> x = lw.bots.bots.get(2000001)
    >>> x
    Example bot
    >>>

    >>> from pprint import pprint
    >>> pprint(dict(x))
    {
        "botId": 2000001,
        "botName": "Example bot",
        "photoUrl": "https://example.com/favicon.png",
        "description": "WorksMobile's A.I. conversation enabled bot",
        "administrators": [
        ...
    }
    """

    def __init__(self, values, api, endpoint) -> None:
        self._init_cache = []
        self.api = api
        self.endpoint = endpoint
        if values:
            self._parse_values(values)

    def __str__(self):
        return getattr(self, self.endpoint.app.namekey, None)

    def __repr__(self) -> str:
        return str(self)

    def __iter__(self):
        for i in dict(self._init_cache):
            yield i, getattr(self, i)

    def _add_cache(self, item):
        key, value = item
        self._init_cache.append((key, value))

    def _parse_values(self, values):
        """Parses values init arg.
        """
        for k, v in values.items():
            self._add_cache((k, v))
            setattr(self, k, v)

    def _diff(self):
        diff = {}
        for k, v in self._init_cache:
            if v != getattr(self, k):
                diff.update({k: getattr(self, k)})
        return diff

    def updates(self):
        return self._diff()

    def save(self):
        """Saves changes to an existing object.
        """
        updates = self.updates()
        if updates:
            req = Request(
                key=getattr(self, self.endpoint.app.idkey),
                base=self.endpoint.url,
                token=self.api.access_token,
                http_session=self.api.http_session,
            )
            if req.patch(updates):
                return True
        return False
