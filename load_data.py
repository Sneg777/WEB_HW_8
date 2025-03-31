import json
from models import get_authors_collection, get_quotes_collection


def load_authors():
    authors_collection = get_authors_collection()
    with open("authors.json", "r", encoding="utf-8") as f:
        authors = json.load(f)
        for author in authors:
            if not authors_collection.find_one({"fullname": author["fullname"]}):
                authors_collection.insert_one(author)


def load_quotes():
    authors_collection = get_authors_collection()
    quotes_collection = get_quotes_collection()
    with open("quotes.json", "r", encoding="utf-8") as f:
        quotes = json.load(f)
        for quote in quotes:
            author = authors_collection.find_one({"fullname": quote["author"]})
            if author and not quotes_collection.find_one({"quote": quote["quote"]}):
                quote["author"] = author["_id"]
                quotes_collection.insert_one(quote)
