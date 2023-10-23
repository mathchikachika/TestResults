from pytest import fixture
import pdb, requests
import os, sys, json, re
from assertpy import assert_that
from lib.common import create_a_college_question, update_question_status
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
def get_staff_token():
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001
def test_specific_by_uuid(get_staff_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_staff_token)
    response: dict = create_a_college_question("staff")
    update_response: dict = update_question_status(response['question_uuid'], "Approved")

    url = f"{req.base_url}/staff/specific/{response['question_uuid']}"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to('Invalid token or expired token.')

@pytest.mark.tc_002
def test_specific_by_uuid_admin_token(get_admin_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_admin_token)
    response: dict = create_a_college_question("staff")

    url = f"{req.base_url}/staff/specific/{response['question_uuid']}"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(404)
    assert_that(json_response['detail']).is_equal_to('Staff Not Found.')

@pytest.mark.tc_003
def test_specific_by_uuid_invalid_token(get_staff_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_staff_token + "xx")
    response: dict = create_a_college_question("staff")

    url = f"{req.base_url}/staff/specific/{response['question_uuid']}"    
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response["detail"]).is_equal_to("Invalid token or expired token.")

@pytest.mark.tc_004
def test_specific_by_uuid_remove_minus(get_staff_token):
    req = Requester()        
    header: dict = req.create_basic_headers(token=get_staff_token)    
    sql_staff_info: list = execute_query(f"SELECT * FROM mathworld.staff LIMIT 1")
    uuid_minus = sql_staff_info[0][0].replace("-", "")    
    url = f"{req.base_url}/staff/specific/{uuid_minus}"
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to('Invalid token or expired token.')
    pass
    
# '''
# @pytest.mark.tc_004
# def test_specific_by_uuid_invalid(get_staff_token):
#     req = Requester()        
#     header: dict = req.create_basic_headers(token=get_staff_token)
#     sql_staff_info: list = execute_query(f"SELECT * FROM mathworld.staff LIMIT 1")
#     sql_uuid: str = re.sub(r'\d+', 'x', sql_staff_info[0][0])
    
#     url = f"{req.base_url}/staff/specific/{sql_uuid}"        
#     response = requests.request("GET", url, headers=header)
#     json_response = json.loads(response.text)
#     assert_that(response.status_code).is_equal_to(400)
#     assert_that(json_response["detail"]).is_equal_to("invalid id")
    
# @pytest.mark.tc_005
# def test_specific_by_uuid_newly_created_staar_admin(get_staff_token):
#     req = Requester()        
#     header: dict = req.create_basic_headers(token=get_staff_token)
#     created_response: dict = common.create_a_staar_question('admin')

#     url = f"{req.base_url}/staff/specific/{created_response['question_uuid']}"        
#     response = requests.request("GET", url, headers=header)
#     json_response = json.loads(response.text)
#     assert_that(response.status_code).is_equal_to(404)
#     assert_that(json_response["detail"]).is_equal_to("Staff Not Found.")
# '''