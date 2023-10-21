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

# --------------------------------
# role: Staff, Admin, Contributor
# page_num:
# page_size: 
# User has to be admin to access this endpoint
# If User is Staff member, then 403 Forbidden
# --------------------------------

@pytest.mark.tc_001
def test_valid_admin_token(get_admin_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/get_people_count"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(json_response['data']['staff_total_count']).is_greater_than(1)
    assert_that(json_response['data']['admin_total_count']).is_greater_than(1)
    assert_that(json_response['data']['subscriber_total_count']).is_greater_than(1)
    assert_that(json_response['data']['total']).is_greater_than(1)

@pytest.mark.tc_002
def test_invalid_admin_token(get_admin_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_admin_token + "ds")
    url = f"{req.base_url}/staff/get_people_count"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to("Invalid token or expired token.")

@pytest.mark.tc_003
def test_invalid_staff_token(get_staff_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_staff_token + "ds")
    url = f"{req.base_url}/staff/get_people_count"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to("Invalid token or expired token.")

@pytest.mark.tc_004
def test_valid_staff_token(get_staff_token):
    req = Requester()    
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/staff/get_people_count"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to("Invalid token or expired token.")

@pytest.mark.tc_005
def test_empty_admin_token():
    req = Requester()    
    header: dict = req.create_basic_headers(token='')
    url = f"{req.base_url}/staff/get_people_count"        
    response = requests.request("GET", url, headers=header)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to("Not authenticated")