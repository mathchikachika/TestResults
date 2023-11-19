import re
import secrets
import string
from datetime import datetime
from typing import List, Optional

from beanie import Document, Indexed, PydanticObjectId
from pydantic import BaseModel, Field, model_validator, validator

from server.models.validators.accounts_validator import (
    password_must_be_valid,
    validate_fields,
    validate_update_fields,
)


def is_not_empty(cls, values):
    """
    The function `is_not_empty` checks if certain attributes in a dictionary are empty and raises a
    ValueError if they are.
    
    :param cls: The parameter `cls` is not used in the function and can be removed
    :param values: The `values` parameter is a dictionary that contains attribute-value pairs
    :return: the `values` dictionary.
    """
    for attr, value in values.items():
        if (
            attr == "middle_name"
            or attr == "created_by"
            or attr == "updated_by"
            or attr == "phone_number"
        ):
            continue
        else:
            if value == "":
                raise ValueError(f"{attr} field should not be empty")

    return values


# The User class represents a user with various attributes such as subscriber ID, name, role, status,
# email, password, and timestamps for creation and update.
class User(Document):
    subscriber_id: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    status: str
    email: Indexed(str, unique=True)
    password: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()

    @validator("created_at", pre=True, always=True)
    def set_created_at_now(v):
        return v or datetime.utcnow()

# The class "Settings" defines the name of a collection and its indexes.
    class Settings:
        name = "user_collection"
        indexes = [[("role", 1)]]


# The ContactPerson class represents a person's contact information including their name,
# relationship, address, and phone number.
class ContactPerson(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    relationship: str
    country: str
    state: str
    city: str
    street: str
    zip_code: str
    phone_number: Optional[str] = None


# The `OfficeDetails` class represents the details of an office, including its location, conference
# time (optional), and phone number.
class OfficeDetails(BaseModel):
    location: str
    conference_time: Optional[str] = None
    phone_number: str


# The `Education` class represents a person's educational background, including the school they
# attended, degree obtained (optional), area of study (optional), and the years they started and ended
# their education.
class Education(BaseModel):
    school: str
    degree: Optional[str] = None
    area_of_study: Optional[str] = None
    year_started: str
    year_ended: str


# The `EducationList` class is a subclass of `BaseModel` and represents a list of `Education` objects.
class EducationList(BaseModel):
    education: List[Education]


# The Student class is a subclass of the User class and has a contact_person attribute of type
# ContactPerson.
class Student(User):
    contact_person: ContactPerson


# The `Teacher` class is a subclass of `User` and includes optional attributes for office details and
# education.
class Teacher(User):
    office_details: Optional[OfficeDetails] = None
    education: Optional[List[Education]] = None


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


# The `Registration` class is a model for creating a student account with required fields such as
# first name, last name, role, school, email, password, and repeat password, along with an optional
# middle name and contact person.
class Registration(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    school: str
    email: str
    password: str
    repeat_password: str
    contact_person: Optional[ContactPerson]
    _no_empty_required_fields = model_validator(mode="before")(is_not_empty)
    _check_password = model_validator(mode="before")(password_must_be_valid)

    @validator("role")
    def check_role(cls, v):
        if v != "student":
            raise ValueError("role must be a student when creating a student account")

        return v

    @validator("email")
    def check_email(cls, v):
        if v:
            regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
            if re.fullmatch(regex, v):
                return v
            else:
                raise ValueError("email is invalid")
        else:
            raise ValueError("email field should not be empty")


# class Registration(Account):
#     school: Optional[str] = None
#     repeat_password: str

#     _validate_fields = model_validator(mode='before')(validate_fields)

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "first_name": "John",
#                 'middle_name': "David",
#                 "last_name": "Doe",
#                 "role": "staff",
#                 "school": "this is optional (subscriber only)",
#                 "email": "validemail@gmail.com",
#                 "password": "Heyy123!",
#                 "repeat_password": "Heyy123!"
#             }
#         }

# class UpdatedAccount(BaseModel):
#     first_name: str
#     middle_name: Optional[str] = None
#     last_name: str
#     role: str
#     email: str
#     updated_by: Optional[str] = None
#     updated_at: Optional[datetime] = None
#     _validate_fields = model_validator(mode='before')(validate_update_fields)

#     @validator('updated_at', pre=True, always=True)
#     def set_updated_at_now(v):
#         return v or datetime.utcnow()


# class UpdatedSubscriberAccount(UpdatedAccount):
#     school: str

# class UpdatedPassword(BaseModel):
#     old_password: str
#     new_password: str
#     repeat_new_password: str
#     updated_by: Optional[str] = None
#     updated_at: Optional[datetime] = None
#     _validate_fields = model_validator(mode='before')(password_must_be_valid)

#     @validator('updated_at', pre=True, always=True)
#     def set_updated_at_now(v):
#         return v or datetime.utcnow()

#     class Config:
#         json_schema_extra = {
#             "example": {
#                 "old_password": "Hello123!",
#                 'new_password': "HiBro567!",
#                 "repeat_new_password": "HiBro567!",
#             }
#         }


# The UserAccount class represents a user account with an email and role.
class UserAccount(BaseModel):
    email: str
    role: str


# The UserAccounts class is a subclass of BaseModel and contains a list of UserAccount objects.
class UserAccounts(BaseModel):
    accounts: List[UserAccount]


# The class `UserResponseModel` represents a user response with various attributes such as id,
# subscriber_id, first_name, last_name, role, status, email, created_by, created_at, updated_by, and
# updated_at.
class UserResponseModel(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    subscriber_id: str
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    role: str
    status: str
    email: str
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None


# The `InitialUserAccountResponseModel` class represents the response model for an initial user
# account, including attributes such as ID, subscriber ID, role, status, email, creation date, and
# update date.
class InitialUserAccountResponseModel(BaseModel):
    id: PydanticObjectId = Field(alias="_id")
    subscriber_id: str
    role: str
    status: str
    email: str
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


# The class `UpdatedUserViaSubscriber` represents a user with updated information, including their
# first name, middle name, last name, email, and details about who updated the user and when.
class UpdatedUserViaSubscriber(BaseModel):
    first_name: str
    middle_name: Optional[str] = None
    last_name: str
    email: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()

# The `Config` class contains a JSON schema with an example object.
    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Peter",
                "middle_name": "John",
                "last_name": "James",
                "email": "peterjohnj@gmail.com",
            }
        }


# The `UpdatedRole` class represents a role with optional fields for the user who updated it and the
# timestamp of the update.
class UpdatedRole(BaseModel):
    role: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()

# The `Config` class has a `json_schema_extra` attribute that contains an example JSON schema.
    class Config:
        json_schema_extra = {
            "example": {
                "role": "teacher",
            }
        }


# The class `UpdatedStatus` represents an updated status with optional fields for the updater's name
# and the update timestamp.
class UpdatedStatus(BaseModel):
    status: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()

# The class `Config` has a `json_schema_extra` attribute that contains an example JSON schema.
    class Config:
        json_schema_extra = {
            "example": {
                "status": "active",
            }
        }


# The `ResetPassword` class is a data model that represents a password reset request, including the
# new password, the user who updated it, and the timestamp of the update.
class ResetPassword(BaseModel):
    password: Optional[str] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()

    @validator("password", pre=True, always=True)
    def generate_password(v):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation.replace('"', "")
        special_chars = special_chars.replace('"', "").replace("'", "").replace(".", "")
        choices = letters + digits + special_chars
        v = ""
        for i in range(9):
            v += "".join(secrets.choice(choices))

        return v
