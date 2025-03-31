from db_connection import db


def get_authors_collection():
    return db["authors"]


def get_quotes_collection():
    return db["quotes"]
