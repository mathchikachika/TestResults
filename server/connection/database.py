import os
import pdb

import motor.motor_asyncio
from beanie import init_beanie
from dotenv import load_dotenv

from server.authentication.bcrypter import Hasher
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
    try:
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
    except Exception as e:
        print(e)


async def create_initial_users():
    ADMIN_FNAME = os.getenv("ADMIN_FNAME")
    ADMIN_MNAME = os.getenv("ADMIN_MNAME")
    ADMIN_LNAME = os.getenv("ADMIN_LNAME")
    ADMIN_ROLE = os.getenv("ADMIN_ROLE")
    ADMIN_EMAIL = os.getenv("ADMIN_EMAIL")
    ADMIN_PASSWORD = os.getenv("ADMIN_PASSWORD")
    ADMIN_CREATEDBY = os.getenv("ADMIN_CREATEDBY")

    STAFF_FNAME = os.getenv("STAFF_FNAME")
    STAFF_MNAME = os.getenv("STAFF_MNAME")
    STAFF_LNAME = os.getenv("STAFF_LNAME")
    STAFF_ROLE = os.getenv("STAFF_ROLE")
    STAFF_EMAIL = os.getenv("STAFF_EMAIL")
    STAFF_PASSWORD = os.getenv("STAFF_PASSWORD")
    STAFF_CREATEDBY = os.getenv("STAFF_CREATEDBY")

    await create_user(
        email=ADMIN_EMAIL,
        first_name=ADMIN_FNAME,
        middle_name=ADMIN_MNAME,
        last_name=ADMIN_LNAME,
        role=ADMIN_ROLE,
        password=ADMIN_PASSWORD,
        created_by=ADMIN_CREATEDBY,
    )

    await create_user(
        email=STAFF_EMAIL,
        first_name=STAFF_FNAME,
        middle_name=STAFF_MNAME,
        last_name=STAFF_LNAME,
        role=STAFF_ROLE,
        password=STAFF_PASSWORD,
        created_by=STAFF_CREATEDBY,
    )


async def create_user(
    email, first_name, middle_name, last_name, role, password, created_by
):
    try:
        account = await Account.find_one({"email": email})
        if account:
            print(
                "-- INFO [Data seed - Creating initial account] - Account already exists"
            )
        else:
            user_account = Account(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
                role=role,
                email=email,
                password=Hasher().hash_password(password=password),
                created_by=created_by,
            )
            await user_account.insert()

            print(
                f"-- INFO [Data seed - Creating initial account] - Created {role} account success"
            )
    except Exception as e:
        print("An error occured while creating initial account.")
        print("Error: ", e)
