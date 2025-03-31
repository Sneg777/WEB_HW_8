from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://Sneg321:@clusterbes.tzjea.mongodb.net/?retryWrites=true&w=majority&appName=ClusterBes"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["HW_08"]