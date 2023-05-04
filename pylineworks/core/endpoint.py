#!/usr/bin/env python3

from pylineworks.core.response import Record, RecordSet
from pylineworks.core.query import Request


class Endpoint:
    """Represent actions available on endpoints in LINEWORKS API.
    """

    def __init__(self, api, app, name, model=None) -> None:
        self.return_obj = self._lookup_ret_obj(name, model)
        self.api = api
        self.app = app
        self.name = name.replace("_", "/")
        self.model = model
        self.url = "{base_url}{app}{endpoint}".format(
            base_url=self.api.base_url,
            app=app.name,
            endpoint="/" + self.name if self.name != self.app.name else ""
        )

    def _lookup_ret_obj(self, name, model):
        """Loads unique Response objects
        """
        if model:
            name = name.title().replace("_", "").replace("-", "")
            ret = getattr(model, name, Record)
        else:
            ret = Record
        return ret

    def all(self):
        """Queries the ListView of a given endpoint.
        """
        req = Request(
            base=self.url,
            token=self.api.access_token,
            http_session=self.api.http_session,
        )
        return RecordSet(self, req)

    def get(self, *args, **kwargs):
        """Queries the DitailView of a given endpoint.
        """
        key = args[0]
        req = Request(
            key=key,
            base=self.url,
            token=self.api.access_token,
            http_session=self.api.http_session
        )
        return next(RecordSet(self, req), None)

    def create(self, *args, **kwargs):
        """Creates an object on an endpoint
        """
        req = Request(
            base=self.url,
            http_session=self.api.http_session,
            token=self.api.access_token
        ).post(args[0] if args else kwargs)

        return self.return_obj(req, self.api, self)

    def delete(self, objects):
        """Bulk deletes objects on an endpoint.

        :arg list objects: A li st of ids or Records

        :Examples:

        >>> lw.bots.bots.delete(lw.bots.bots.all())
        >>>
        >>> lw.bots.bots.delete([2, 243, 431, 700])
        >>>
        """
        cleaned_ids = []
        if not isinstance(objects, list) and \
           not isinstance(objects, RecordSet):
            raise ValueError(
                "objects must be list[str|int|Record]|RecordSet - was "
                "" + str(type(objects))
            )
        for o in objects:
            if isinstance(o, int):
                cleaned_ids.append(o)
            elif isinstance(o, str) and o.isnumeric():
                cleaned_ids.append(int(o))
            elif isinstance(o, str):
                cleaned_ids.append(o)
            elif isinstance(o, self.return_obj):
                cleaned_ids.append(hasattr(o, self.app.idkey))
            else:
                raise ValueError(
                    "invalid object in list of objects to delete: "
                    "" + str(type(o))
                )

        for id in cleaned_ids:
            ret = Request(
                key=id,
                base=self.url,
                token=self.api.access_token,
                http_session=self.api.http_session,
            ).delete()
            if ret is False:
                raise Exception("failed to delete object id: " + str(id))
        return True

    def update(self, object):
        """Updates existing object on an endpoint.
        """
        if isinstance(object, Record):
            return object.save()
        else:
            raise ValueError(
                "Object passed must be Record - was: " + str(type(object))
            )
