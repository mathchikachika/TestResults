from datetime import datetime
from typing import List, Optional

import pymongo
from beanie import Document, Indexed
from pydantic import BaseModel, Field, model_validator, validator

from server.models.validators.question_request_root_validators import (
    validate_college_fields,
    validate_mathworld_fields,
    validate_option_fields,
    validate_staar_fields,
    validate_updated_question_fields,
    validate_updated_status_fields,
)

# The `Activity` class is a document that represents an activity with a title, details, staff
# involved, question ID, staff ID, and creation timestamp.

class Activity(Document):
    title: str
    details: str
    staff_involved: str
    question_id: str
    staff_id: str
    created_at: Optional[datetime] = None

    @validator("created_at", pre=True, always=True)
    def set_created_at_now(v):
        return v or datetime.utcnow()

  # The class "Settings" defines the name and indexes for an activity collection.
    class Settings:
        name = "acitivity_collection"
        indexes = [[("question_id", 1)], [("staff_id", 1)]]


# The `Option` class represents an option in a multiple-choice question, with properties for the
# letter, content, image, unit, and whether it is the correct answer.
class Option(BaseModel):
    letter: str
    content: str
    image: Optional[str]
    unit: Optional[str]
    is_answer: bool
    _validate_fields = model_validator(mode="before")(validate_option_fields)


# The `Question` class represents a document with various attributes such as response type, question
# content, image, status, options, and timestamps for creation, update, and review.
class Question(Document):
    response_type: str
    question_content: str
    question_img: Optional[str]
    question_status: str = "Pending"
    options: List[Option]
    created_by: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()

    @validator("created_at", pre=True, always=True)
    def set_created_at_now(v):
        return v or datetime.utcnow()

    class Settings:
        name = "question_collection"
        indexes = [[("response_type", 1)], [("question_status", 1)]]


# The `StaarQuestion` class is a subclass of `Question` that represents a STAAR (State of Texas
# Assessments of Academic Readiness) question and includes additional fields specific to STAAR
# questions.
class StaarQuestion(Question):
    question_type: str
    grade_level: int
    release_date: str
    category: str
    student_expectations: List[str]
    keywords: List[str]
    _validate_fields = model_validator(mode="before")(validate_staar_fields)

# The class "Settings" defines a collection named "question_collection" with multiple indexes.
    class Settings:
        name = "question_collection"
        indexes = [
            [("question_type", 1)],
            [("grade_level", 1)],
            [("release_date", 1)],
            [("category", 1)],
            [("student_expectations", 1)],
            [("keywords", 1)],
        ]


# The above class represents a college question with specific fields and validation.
class CollegeQuestion(Question):
    question_type: str
    classification: str
    test_code: str
    keywords: List[str]
    _validate_fields = model_validator(mode="before")(validate_college_fields)

# The class "Settings" defines the name and indexes for a question collection.
    class Settings:
        name = "question_collection"
        indexes = [
            [("classification", 1)],
            [("test_code", 1)],
        ]


# The class MathworldQuestion represents a question in the Mathworld system and includes various
# properties and methods for managing question data.
class MathworldQuestion(Question):
    question_type: str
    grade_level: int
    teks_code: str
    subject: str
    topic: str
    category: str
    student_expectations: List[str]
    keywords: List[str]
    difficulty: str
    points: int
    _validate_fields = model_validator(mode="before")(validate_mathworld_fields)

# The class "Settings" defines the name of a collection and the indexes for that collection in a
# MongoDB database.
    class Settings:
        name = "question_collection"
        indexes = [
            [("teks_code", 1)],
            [("subject", 1)],
            [("topic", 1)],
            [("difficulty", 1)],
        ]


# The `UpdatedStaarQuestion` class is a subclass of `StaarQuestion` that adds additional fields for
# update notes, the user who updated the question, the timestamp of the update, and a list of options.
class UpdatedStaarQuestion(StaarQuestion):
    update_note: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    options: List[Option]
    _no_missing_update_fields = model_validator(mode="before")(
        validate_updated_question_fields
    )

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()


# The class `UpdatedCollegeQuestion` is an updated version of the `CollegeQuestion` class, with
# additional fields for tracking updates and a validator for ensuring all required fields are present
# when updating a question.
class UpdatedCollegeQuestion(CollegeQuestion):
    update_note: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    options: List[Option]
    _no_missing_update_fields = model_validator(mode="before")(
        validate_updated_question_fields
    )

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()


# The class `UpdatedMathworldQuestion` is an updated version of the `MathworldQuestion` class, with
# additional fields for update note, updated by, updated at, and options. It also includes a validator
# for ensuring that all required update fields are present.
class UpdatedMathworldQuestion(MathworldQuestion):
    update_note: str
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    options: List[Option]
    _no_missing_update_fields = model_validator(mode="before")(
        validate_updated_question_fields
    )

    @validator("updated_at", pre=True, always=True)
    def set_updated_at_now(v):
        return v or datetime.utcnow()


# The class `UpdateQuestionStatus` is a BaseModel that represents the status update of a question,
# including the status, update note, reviewer, and review timestamp.
class UpdateQuestionStatus(BaseModel):
    status: str
    update_note: Optional[str] = None
    reviewed_by: Optional[str] = None
    reviewed_at: Optional[datetime] = None
    _validate_fields = model_validator(mode="before")(validate_updated_status_fields)

    @validator("reviewed_at", pre=True, always=True)
    def set_updated_at_now(cls, v):
        return v or datetime.utcnow()

# The class `Config` has a `json_schema_extra` attribute with an example JSON schema.
    class Config:
        json_schema_extra = {
            "example": {"status": "Approved", "update_note": "Update message"}
        }


def ErrorResponseModel(error, code, message):
    """
    The function ErrorResponseModel returns a dictionary containing error, code, and message.
    
    :param error: The error parameter is a string that represents the type or category of the error that
    occurred. It can be used to provide more specific information about the nature of the error
    :param code: The code parameter is used to represent the error code or status code of the response.
    It is typically a numerical value that indicates the specific error or status of the response
    :param message: The message parameter is a string that represents the error message or description.
    It provides additional information about the error that occurred
    :return: a dictionary with three keys: "error", "code", and "message". The values for these keys are
    provided as arguments to the function.
    """
    return {"error": error, "code": code, "message": message}
