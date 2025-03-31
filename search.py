from models import get_authors_collection, get_quotes_collection
from bson.objectid import ObjectId
from db_connection import redis_client


def search_by_author(name):
    authors_collection = get_authors_collection()
    quotes_collection = get_quotes_collection()

    cached_result = redis_client.get(f"author:{name}")
    if cached_result:
        print(cached_result)
        return

    author = authors_collection.find_one({"fullname": {"$regex": f"^{name}", "$options": "i"}})
    if author:
        quotes = quotes_collection.find({"author": ObjectId(author["_id"])});
        result = "\n".join([q["quote"] for q in quotes])
        redis_client.setex(f"author:{name}", 3600, result)  # Кешируем на 1 час
        print(result)
    else:
        print("Автор не найден")


def search_by_tag(tag):
    quotes_collection = get_quotes_collection()

    cached_result = redis_client.get(f"tag:{tag}")
    if cached_result:
        print(cached_result)
        return

    quotes = quotes_collection.find({"tags": {"$regex": f"^{tag}", "$options": "i"}})
    result = "\n".join([q["quote"] for q in quotes])
    redis_client.setex(f"tag:{tag}", 3600, result)
    print(result)