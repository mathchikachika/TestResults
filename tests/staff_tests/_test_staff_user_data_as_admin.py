from pytest import fixture
import pdb, requests
import os, sys, json
from assertpy import assert_that

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
import lib.generate_token as generate_token
from lib.requester import Requester


@pytest.mark.skip(reason="Skipping the entire test suite")
@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_staff_user_data(get_staff_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/staff/user_data"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
