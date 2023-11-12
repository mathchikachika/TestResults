from bson import ObjectId
from pydantic import MongoDsn
from pytest import fixture
import pdb, requests
import os, sys, json
from faker import Faker
import random
from assertpy import assert_that
import uuid
import time
from lib.mw_db import get_db
from tests.payloads.valid_question_payloads import get_valid_successful_college_payload

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
from lib.common import get_random_question
import lib.generate_token as generate_token
from lib.requester import Requester

faker = Faker()

@fixture(scope="module")
def get_admin_token():    
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_update_college_question(get_admin_token):
    req: Requester = Requester()
    random_data: dict = common.get_random_payload_data()
    college_classic = get_db().question_collection.find_one({ "question_type": "College Level" })
    sql_classic_id: ObjectId = college_classic['_id']
    sql_classic_question_type: str = college_classic['question_type']
    sql_classic_response_type: str = college_classic['response_type']
    sql_classic_question: str = college_classic['question_content']
    sql_classic_status: str = college_classic['question_status']
    random_payload = get_valid_successful_college_payload()
    header: dict = req.create_basic_headers(token=get_admin_token) 

    url: str = f"{req.base_url}/v1/questions/update/{sql_classic_id}"
    # upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")     
    time.sleep(1)
    response = requests.request("PUT", url, headers=header, data=json.dumps(random_payload))
    updated_response: dict = json.loads(response.text)
    print(updated_response)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(updated_response['detail']).is_equal_to("Successfully updated")
    assert_that(str(updated_response['_id'])).is_equal_to(str(sql_classic_id))

    sql_college_updated = get_db().question_collection.find_one({ "_id": ObjectId(sql_classic_id) })
    sql_updated_id: str = sql_college_updated['_id']
    sql_updated_question_type: str = sql_college_updated['question_type']
    sql_updated_response_type: str = sql_college_updated['response_type']
    sql_updated_question: str = sql_college_updated['question_content']
    sql_updated_status: str = sql_college_updated['updated_status']

    assert_that(sql_updated_id).is_equal_to(sql_classic_id)
    assert_that(sql_updated_question_type).is_equal_to(sql_classic_question_type)
    assert_that(sql_updated_response_type).is_equal_to(random_data['response_type'])
    assert_that(sql_updated_question).is_not_equal_to(sql_classic_question)
    assert_that(sql_updated_status).is_equal_to(sql_classic_status)


@pytest.mark.tc_002
def test_update_college_question_invalid_id(get_admin_token):
    req: Requester = Requester()      
    random_data: dict = common.get_random_payload_data()    
    college_classic: list = get_db().question_collection.find_one({ "question_type": "College Level" })
              
    sql_classic_invalid_id: str = str(college_classic['_id']) + "123"    
    random_payload = get_valid_successful_college_payload()

    header: dict = req.create_basic_headers(token=get_admin_token) 
    
    url: str = f"{req.base_url}/v1/questions/update/{sql_classic_invalid_id}" 
    # upload_file: list = common.set_image_file(f"{CURRENT_DIR}\\tests\\images", "image_01.jpg")           
    response = requests.request("PUT", url, headers=header, data=json.dumps(random_payload))
    updated_response: dict = json.loads(response.text)  
    time.sleep(1)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(updated_response['detail']).is_equal_to("Invalid id")        