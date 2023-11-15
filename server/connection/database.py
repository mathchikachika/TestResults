import os
import pdb

import motor.motor_asyncio
from beanie import init_beanie
from dotenv import load_dotenv

from server.models.account import Account, SubscriberAccount
from server.models.question import (
    Activity,
    CollegeQuestion,
    MathworldQuestion,
    Question,
    StaarQuestion,
)
from server.models.users import User

# The code snippet is loading environment variables from a `.env` file using the `load_dotenv()`
# function.
load_dotenv()
MONGO_DETAILS = os.getenv("MONGO_DETAILS")
DB_NAME = os.getenv("DB_NAME")
client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)
db = client[DB_NAME]


async def init_db():
    """
    The `init_db` function initializes the database and sets up the document models for various question
    types, accounts, activities, and users.
    """
    await init_beanie(
        database=client[DB_NAME],
        document_models=[
            Question,
            StaarQuestion,
            MathworldQuestion,
            CollegeQuestion,
            Account,
            SubscriberAccount,
            Activity,
            User,
        ],
    )
