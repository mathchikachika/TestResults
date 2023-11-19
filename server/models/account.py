import re
from datetime import datetime
from enum import Enum
from typing import Optional

from beanie import Document, Indexed, PydanticObjectId
from pydantic import BaseModel, Field, model_validator, validator

from server.models.validators.accounts_validator import (
    password_must_be_valid,
    validate_fields,
    validate_update_fields,
)


# The below class represents an account with various attributes such as first name, last name, role,
# email, password, and timestamps for creation and update.
class Account(Document):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    email: Indexed(str, unique=True)
    password: str
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()

    @validator("created_at", pre=True, always=True)
    def set_created_at_now(v):
        return v or datetime.utcnow()

    class Settings:
        name = "account_collection"
        indexes = [[("role", 1)]]


# The `SubscriberAccount` class is a subclass of the `Account` class and includes an additional
# attribute `school` of type string.
class SubscriberAccount(Account):
    school: str


# The `LogIn` class is a data model for validating and storing user login information, specifically
# the email and password.
class LogIn(BaseModel):
    email: str
    password: str

    @validator("email", pre=True, always=True)
    def check_email(cls, v):
        if v:
            regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            if re.fullmatch(regex, v):
                return v
            else:
                raise ValueError("email is invalid")
        else:
            raise ValueError("email field should not be empty")

# The `Config` class has a `json_schema_extra` attribute that contains an example JSON schema.
    class Config:
        json_schema_extra = {
            "example": {
                "email": "validemail@gmail.com",
                "password": "password",
            }
        }


# The `Registration` class represents a user registration form with optional school field and password
# validation.
class Registration(Account):
    school: Optional[str] = None
    repeat_password: str

    _validate_fields = model_validator(mode="before")(validate_fields)

# The `Config` class contains a JSON schema with an example of a user's information.
    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "John",
                "middle_name": "David",
                "last_name": "Doe",
                "role": "staff",
                "school": "this is optional (subscriber only)",
                "email": "validemail@gmail.com",
                "password": "Heyy123!",
                "repeat_password": "Heyy123!",
            }
        }


# The `UpdatedAccount` class is a model that represents an updated account with fields such as first
# name, middle name, last name, role, email, and information about the update.
class UpdatedAccount(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    email: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    _validate_fields = model_validator(mode="before")(validate_update_fields)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()


# The class `UpdatedSubscriberAccount` is a subclass of `UpdatedAccount` that includes an additional
# attribute `school` of type `str`.
class UpdatedSubscriberAccount(UpdatedAccount):
    school: str


# The `UpdatedPassword` class represents a model for updating a password, including fields for the old
# password, new password, repeat new password, and optional fields for the user who updated the
# password and the timestamp of the update.
class UpdatedPassword(BaseModel):
    old_password: str
    new_password: str
    repeat_new_password: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    _validate_fields = model_validator(mode="before")(password_must_be_valid)

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()

# The `Config` class contains a JSON schema example for password change.
    class Config:
        json_schema_extra = {
            "example": {
                "old_password": "Hello123!",
                "new_password": "HiBro567!",
                "repeat_new_password": "HiBro567!",
            }
        }


# The `AccountResponseModel` class represents a response model for an account, with various attributes
# such as id, name, role, email, and timestamps for creation and update.
class AccountResponseModel(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    email: str
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None


# The class `SubscriberAccountResponseModel` is a subclass of `AccountResponseModel` and includes an
# additional attribute `school` of type `str`.
class SubscriberAccountResponseModel(AccountResponseModel):
    school: str
