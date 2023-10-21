from pytest import fixture
import pdb, requests
import os, sys, json, re
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

@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001
def test_specific_by_uuid(get_admin_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_admin_token)
    sql_staff_info: list = execute_query(f"SELECT * FROM mathworld.staff LIMIT 1")
    sql_uuid: str = sql_staff_info[0][0]
    sql_email: str = sql_staff_info[0][1]
    sql_first_name: str = sql_staff_info[0][5]
    sql_middle_init: str = sql_staff_info[0][6]
    sql_last_name: str = sql_staff_info[0][7]

    url = f"{req.base_url}/staff/specific/{sql_uuid}"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)

    assert_that(json_response["user"]['uuid']).is_equal_to(sql_uuid)
    assert_that(json_response["user"]['first_name']).is_equal_to(sql_first_name)
    assert_that(json_response["user"]['middle_name']).is_equal_to(sql_middle_init)
    assert_that(json_response["user"]['last_name']).is_equal_to(sql_last_name)
    assert_that(json_response["user"]['email']).is_equal_to(sql_email)

@pytest.mark.tc_002
def test_specific_by_uuid_invalid_token(get_admin_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_admin_token + "xx")
    sql_staff_info: list = execute_query(f"SELECT * FROM mathworld.staff LIMIT 1")
    sql_uuid: str = sql_staff_info[0][0]

    url = f"{req.base_url}/staff/specific/{sql_uuid}"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response["detail"]).is_equal_to("Invalid token or expired token.")

@pytest.mark.tc_003
def test_specific_by_uuid_remove_minus(get_admin_token):
    req = Requester()        
    header: dict = req.create_basic_headers(token=get_admin_token)
    sql_staff_info: list = execute_query(f"SELECT * FROM mathworld.staff LIMIT 1")
    sql_uuid: str = sql_staff_info[0][0].replace("-", "")
    sql_email: str = sql_staff_info[0][1]
    sql_first_name: str = sql_staff_info[0][5]
    sql_middle_init: str = sql_staff_info[0][6]
    sql_last_name: str = sql_staff_info[0][7]

    url = f"{req.base_url}/staff/specific/{sql_uuid}"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)

    assert_that(str(json_response["user"]['uuid']).replace("-", "")).is_equal_to(sql_uuid)
    assert_that(json_response["user"]['first_name']).is_equal_to(sql_first_name)
    assert_that(json_response["user"]['middle_name']).is_equal_to(sql_middle_init)
    assert_that(json_response["user"]['last_name']).is_equal_to(sql_last_name)
    assert_that(json_response["user"]['email']).is_equal_to(sql_email)

@pytest.mark.tc_004
def test_specific_by_uuid_invalid(get_admin_token):
    req = Requester()        
    header: dict = req.create_basic_headers(token=get_admin_token)
    sql_staff_info: list = execute_query(f"SELECT * FROM mathworld.staff LIMIT 1")
    sql_uuid: str = re.sub(r'\d+', 'x', sql_staff_info[0][0])
    
    url = f"{req.base_url}/staff/specific/{sql_uuid}"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(400)
    assert_that(json_response["detail"]).is_equal_to("invalid id")
    
@pytest.mark.tc_005
def test_specific_by_uuid_newly_created_staar_admin(get_admin_token):
    req = Requester()        
    header: dict = req.create_basic_headers(token=get_admin_token)
    created_response: dict = common.create_a_staar_question('admin')

    url = f"{req.base_url}/staff/specific/{created_response['question_uuid']}"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(json_response["detail"]).is_equal_to("Staff Not Found.")
    