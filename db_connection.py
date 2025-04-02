from pymongo import MongoClient
from pymongo.server_api import ServerApi
import redis

uri = "mongodb+srv://Sneg321:****@clusterbes.tzjea.mongodb.net/?retryWrites=true&w=majority&appName=ClusterBes"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["HW_08"]

redis_client = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
