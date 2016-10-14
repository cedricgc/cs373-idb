# -*- coding: utf-8 -*-
"""Routing and request handler for REST API

The flask app object provides the route decorator to dispatch requests
to the function as described in the decorator argument as well as controlling
the valid HTTP verbs that can be requested to that endpoint. The decorated
handler expects a flask.Response object as the return value.

See http://flask.pocoo.org/docs/latest/quickstart/#about-responses for how
flask converts return values to Response objects.
"""


import flask
import sqlalchemy

from website import api, app, db, ma

app.url_map.strict_slashes = False
"""Disables Werkzeug's strict route interpretation

There are good reasons for enforcing strict slashes for form posts and
indexability, but it is inconvienent when interacting with an API so
it is disabled.

See: http://flask.pocoo.org/docs/latest/quickstart/#variable-rules
"""


@api.route('/hello/', methods=['GET'])
def hello():
    return "Hello!"
