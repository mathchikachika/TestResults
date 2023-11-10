import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()
MONGO_DETAILS = os.getenv('MONGO_DETAILS')
DB_NAME = os.getenv('DB_NAME')


def get_db():
    cluster = MongoClient(MONGO_DETAILS)
    return cluster[DB_NAME]
