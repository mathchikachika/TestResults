import json
import os
import sys

import requests
from assertpy import assert_that
from bson import ObjectId
from faker import Faker
from lib.mw_db import get_db
from pytest import fixture

from tests.payloads.valid_question_payloads import get_valid_successful_staar_payload

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger

import lib.common as common
import lib.generate_token as generate_token
import pytest
from lib.common import get_random_question
from lib.requester import Requester

faker = Faker()


@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(
        email="adminXYZ@gmail.com", password="Admin123!"
    )
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_update_staar_question(get_admin_token):
    req: Requester = Requester()
    staar_classic = get_db().question_collection.find_one({"question_type": "STAAR"})
    sql_classic_id: ObjectId = staar_classic["_id"]
    sql_classic_question_type: str = staar_classic["question_type"]
    sql_classic_response_type: str = staar_classic["response_type"]
    sql_classic_question: str = staar_classic["question_content"]
    sql_classic_status: str = staar_classic["question_status"]
    random_payload = get_valid_successful_staar_payload()
    random_payload["update_note"] = "Updated question"
    header: dict = req.create_basic_headers(token=get_admin_token)

    url: str = f"{req.base_url}/v1/questions/update/{sql_classic_id}"
    response = requests.request(
        "PUT", url, headers=header, data=json.dumps(random_payload)
    )
    updated_response: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(updated_response["detail"]).is_equal_to("Successfully Updated Question")
    assert_that(str(updated_response["question"]["_id"])).is_equal_to(
        str(sql_classic_id)
    )

    sql_staar_updated = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    sql_updated_id: str = sql_staar_updated["_id"]
    sql_updated_question_type: str = sql_staar_updated["question_type"]
    sql_updated_response_type: str = sql_staar_updated["response_type"]
    sql_updated_question: str = sql_staar_updated["question_content"]
    sql_updated_status: str = sql_staar_updated["question_status"]

    assert_that(sql_updated_id).is_equal_to(sql_classic_id)
    assert_that(sql_updated_question_type).is_equal_to(sql_classic_question_type)
    assert_that(sql_updated_response_type).is_equal_to(sql_classic_response_type)
    assert_that(sql_updated_question).is_not_equal_to(sql_classic_question)
    assert_that(sql_updated_status).is_equal_to(sql_classic_status)


@pytest.mark.tc_002
def test_update_staar_question_invalid_id(get_admin_token):
    req: Requester = Requester()
    staar_classic: list = get_db().question_collection.find_one(
        {"question_type": "Mathworld"}
    )

    sql_classic_invalid_id: str = str(staar_classic["_id"]) + "123"
    random_payload = get_valid_successful_staar_payload()
    random_payload["update_note"] = "Updated question"
    header: dict = req.create_basic_headers(token=get_admin_token)

    url: str = f"{req.base_url}/v1/questions/update/{sql_classic_invalid_id}"
    response = requests.request(
        "PUT", url, headers=header, data=json.dumps(random_payload)
    )
    updated_response: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(updated_response["detail"]).is_equal_to("Question not found")
