#!/usr/bin/env python3

from pylineworks.core.response import Record
from pylineworks.core.response import Request


class Boards(Record):
    """Board Object
    """
    def __repr__(self) -> str:
        return self.boardName

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
            if req.put({
                "boardName": self.boardName,
                "description": self.description
            }):
                return True
        return False
