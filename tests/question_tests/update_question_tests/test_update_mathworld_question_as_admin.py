from bson import ObjectId
from pytest import fixture
import pdb, requests
import os, sys, json
from faker import Faker
import random
from assertpy import assert_that
import uuid
import time

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
from lib.common import get_random_question
import lib.generate_token as generate_token
from lib.requester import Requester
from lib.mw_db import get_db
from tests.payloads.valid_question_payloads import get_valid_successful_mathworld_payload

faker = Faker()


@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_update_mathworld_question(get_admin_token):
    req: Requester = Requester()
    random_data: dict = common.get_mathworld_random_payload_data()
    mathworld_classic: dict = get_db().question_collection.find_one({'question_type': 'Mathworld'})
    sql_classic_id: str = mathworld_classic['_id']
    sql_classic_question_type: str = mathworld_classic['question_type']
    sql_classic_question: str = mathworld_classic['question_content']
    sql_classic_status: str = mathworld_classic['question_status']

    random_payload = get_valid_successful_mathworld_payload()

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/v1/questions/update/{sql_classic_id}"
    # upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")
    response = requests.request("PUT", url, headers=header, json=random_payload)
    updated_response: dict = json.loads(response.text)
    time.sleep(2)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(updated_response['detail']).is_equal_to("Successfully updated")
    assert_that(updated_response['_id']).is_equal_to(sql_classic_id)
    sql_mathworld_updated: dict = get_db().question_collection.find_one({'_id': ObjectId(sql_classic_id)})

    sql_updated_id: str = sql_mathworld_updated['_id']
    sql_updated_question_type: str = sql_mathworld_updated['question_type']
    sql_updated_response_type: str = sql_mathworld_updated['response_type']
    sql_updated_question: str = sql_mathworld_updated['question_content']
    sql_updated_status: str = sql_mathworld_updated['question_status']
    # time.sleep(1)
    assert_that(sql_updated_id).is_equal_to(sql_classic_id)
    assert_that(sql_updated_question_type).is_equal_to(sql_classic_question_type)
    assert_that(sql_updated_response_type).is_equal_to(random_data['response_type'])
    assert_that(sql_updated_question).is_not_equal_to(sql_classic_question)
    assert_that(sql_updated_status).is_equal_to(sql_classic_status)


@pytest.mark.tc_002
def test_update_mathworld_question_invalid_id(get_admin_token):
    req: Requester = Requester()
    random_data: dict = common.get_mathworld_random_payload_data()
    mathworld_classic: list = get_db().question_collection.find_one({'question_type': 'Mathworld'})
    sql_classic_invalid_id: str = str(mathworld_classic['_id']) + "333"

    random_payload = get_valid_successful_mathworld_payload()

    header: dict = req.create_basic_headers(token=get_admin_token)
    url: str = f"{req.base_url}/v1/questions/update/{sql_classic_invalid_id}"
    # upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")
    response = requests.request("PUT", url, headers=header, json=random_payload)
    updated_response: dict = json.loads(response.text)
    time.sleep(1)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(updated_response['detail']).is_equal_to("Invalid Teks Code")