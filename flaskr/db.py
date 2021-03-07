"""
The Flask documentation provides this code as the suggested pattern for working with SQLite i Flask:
https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
"""
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    # the 'g' object is a piece of magic described here: https://flask.palletsprojects.com/en/1.1.x/api/#flask.g
    if 'db' not in g:
        # the sqlite3 library is a built-in Python module: https://docs.python.org/3/library/sqlite3.html#sqlite3.connect
        g.db = sqlite3.connect(
            # since Flask can specify different apps to work with, the `current_app` object
            # provides a reference to the application in current use: https://flask.palletsprojects.com/en/1.1.x/api/#flask.current_app
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()