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
from lib.mw_sql import execute_query


@pytest.mark.skip(reason="Skipping the entire test suite")
@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001
def test_specific_by_uuid(get_staff_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_staff_token)
    sql_staff_info: list = execute_query(f"SELECT * FROM mathworld.staff LIMIT 1")
    sql_uuid: str = sql_staff_info[0][0]
    url = f"{req.base_url}/staff/specific/{sql_uuid}"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response["detail"]).is_equal_to("Invalid token or expired token.")
