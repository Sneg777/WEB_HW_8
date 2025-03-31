from models import get_authors_collection, get_quotes_collection
from bson.objectid import ObjectId

def search_by_author(name):
    authors_collection = get_authors_collection()
    quotes_collection = get_quotes_collection()
    author = authors_collection.find_one({"fullname": name})
    if author:
        quotes = quotes_collection.find({"author": ObjectId(author["_id"])})
        for q in quotes:
            print(q["quote"].encode("utf-8").decode())
    else:
        print("Автор не найден")


def search_by_tag(tag):
    quotes_collection = get_quotes_collection()
    quotes = quotes_collection.find({"tags": tag})
    for q in quotes:
        print(q["quote"].encode("utf-8").decode())


def search_by_tags(tags):
    quotes_collection = get_quotes_collection()
    tag_list = tags.split(",")
    quotes = quotes_collection.find({"tags": {"$in": tag_list}})
    for q in quotes:
        print(q["quote"].encode("utf-8").decode())
