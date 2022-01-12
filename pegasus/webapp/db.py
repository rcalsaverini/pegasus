import sqlite3
from sqlite3.dbapi2 import connect
from flask import g


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        conn = sqlite3.connect("database/test.db")
        conn.row_factory = sqlite3.Row
        db = g._database = conn
    return db


def query_many(query, args=()):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return rv


def query_one(query, args=()):
    cur = get_db().execute(query, args)
    rv = cur.fetchone()
    cur.close()
    return rv


def insert_one(query, args=()):
    connection = get_db()
    cur = connection.cursor()
    cur.execute(query, args)
    connection.commit()
    return cur.lastrowid
