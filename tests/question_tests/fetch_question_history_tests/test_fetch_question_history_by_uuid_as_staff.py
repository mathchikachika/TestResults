from bson import ObjectId
from pytest import fixture
import pdb, requests
import os, sys, json
from assertpy import assert_that

from tests.lib.mw_db import get_db

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
import lib.generate_token as generate_token
from lib.requester import Requester
from tests.payloads.valid_question_payloads import get_valid_successful_staar_payload


@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(
        email="staffABC@gmail.com", password="Staff123!"
    )
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_history_create(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()

    # upload_file: list = common.set_image_file(f"{CURRENT_DIR}", "image_01.jpg")
    response = requests.request("POST", url, headers=header, json=payload)
    json_response = json.loads(response.text)
    assert response.status_code == 201
    assert json_response["detail"] == "Successfully Added Question"
    global_question_uuid = json_response["question_id"]
    get_history_url: str = f"{req.base_url}/v1/questions/{json_response['question_id']}"
    response = requests.request("GET", get_history_url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    # assert_that(json_response['history'][0]['title']).is_equal_to("Create")
    # assert_that(json_response['history'][0]['details']).is_equal_to("Created a STAAR question.")
