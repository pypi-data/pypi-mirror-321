import os
import re
from typing import Optional, Union, cast

from flask import Flask, g
from pymysql import Connection
from pymysql.cursors import DictCursor

_NAME_TO_ENV = re.compile(r"[^A-Z0-9_]")


def connect(name: str = "mysql"):
    """Connects to a MySQL database resource using provided environment variables
    (e.g. `MYSQL_{name}_HOST`, note that `MYSQL_MYSQL_HOST` will be abbreviated to `MYSQL_HOST`).
    """

    env_prefix = f"MYSQL_{name}" if name != "mysql" else "MYSQL"
    env_prefix = _NAME_TO_ENV.sub("", env_prefix.upper().replace("-", "_"))

    host = os.getenv(f"{env_prefix}_HOST")
    database = os.getenv(f"{env_prefix}_DB") or os.getenv(f"{env_prefix}_DATABASE")
    user = os.getenv(f"{env_prefix}_USER")
    password = os.getenv(f"{env_prefix}_PASS") or os.getenv(f"{env_prefix}_PASSWORD")

    assert (
        host is not None
        and database is not None
        and user is not None
        and password is not None
    ), (
        f"Environment variables for MySQL resource `{name}` not found (e.g. `{env_prefix}_HOST`)."
    )

    return Connection(
        host=host,
        database=database,
        user=user,
        password=password,
        cursorclass=DictCursor,
    )


def execute(
    connection: Connection[DictCursor],
    sql: str,
    values: Optional[Union[tuple, list]] = None,
):
    """Executes an SQL query against a database connection."""
    cursor = connection.cursor()
    cursor.execute(sql, values)
    return cursor


def fetch_one(connection: Connection[DictCursor], sql: str, values=None):
    """Executes an SQL query and calls `cursor.fetchone()` automatically."""
    with connection.cursor() as cursor:
        cursor.execute(sql, values)
        return cursor.fetchone()


def fetch_all(connection: Connection[DictCursor], sql: str, values=None):
    """Executes an SQL query and calls `cursor.fetchall()` automatically."""
    with connection.cursor() as cursor:
        cursor.execute(sql, values)
        return list(cursor.fetchall())


class FlaskMySQL:
    """Flask extension to add basic DB transaction usage to requests using MySQL. Each request gets a new connection
    and automatically commits or rolls back (if there is an unhandled exception) the entire transaction at
    the end of the request.
    """

    def __init__(self, name: str = "mysql", app: Optional[Flask] = None):
        self.name = name

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        app.teardown_request(self._teardown_request)

    def _get_connections_dict(self):
        # g._mysql_connections is a dictionary of database names to connections.
        try:
            assert type(g._mysql_connections) is dict
            return g._mysql_connections
        except (AttributeError, AssertionError):
            g._mysql_connections = {}
            return g._mysql_connections

    def _get_connection(self):
        connections = self._get_connections_dict()
        if self.name not in connections:
            return None
        return cast(
            Connection[DictCursor],
            connections[self.name],
        )

    def _get_or_create_connection(self):
        db = self._get_connection()
        if db is None:
            db = connect(self.name)
            self._get_connections_dict()[self.name] = db
        return db

    def _teardown_request(self, exception: Optional[BaseException]):
        db = self._get_connection()

        if db is not None:
            if exception is None:
                db.commit()
                db.close()
            else:
                db.close()

            del self._get_connections_dict()[self.name]

    def execute(
        self,
        sql: str,
        values=None,
    ):
        """Executes an SQL query."""
        cursor = self._get_or_create_connection().cursor()
        cursor.execute(sql, values)
        return cursor

    def fetch_one(self, sql: str, values=None):
        """Executes an SQL query and calls `cursor.fetchone()` automatically."""
        with self._get_or_create_connection().cursor() as cursor:
            cursor.execute(sql, values)
            return cursor.fetchone()

    def fetch_all(self, sql: str, values=None):
        """Executes an SQL query and calls `cursor.fetchall()` automatically."""
        with self._get_or_create_connection().cursor() as cursor:
            cursor.execute(sql, values)
            return list(cursor.fetchall())
