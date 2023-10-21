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


def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_valid_login():
    req = Requester()    
    url = f"{req.base_url}/staff/login"
    payload = {
        "email": "staffABC@gmail.com",
        "password": "Staff123!"
    }    
    json_payload: str = json.dumps(payload)
    response = requests.request(
        "POST", url, headers={}, data=json_payload)
    json_response: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(json_response['access_token']).is_not_empty()

@pytest.mark.tc_002
def test_invalid_email():
    req = Requester()    
    url = f"{req.base_url}/staff/login"
    payload = {
        "email": "staff1ABC@gmail.com",
        "password": "Staff123!"
    }    
    json_payload: str = json.dumps(payload)
    response = requests.request(
        "POST", url, headers={}, data=json_payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(401)
    assert_that(json_response['detail']).is_equal_to('Username or Password is wrong.')

@pytest.mark.tc_003
def test_invalid_password():
    req = Requester()
    url = f"{req.base_url}/staff/login"
    payload = {
        "email": "staffABC@gmail.com",
        "password": "S1taff123!"
    }    
    json_payload: str = json.dumps(payload)
    response = requests.request(
        "POST", url, headers={}, data=json_payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(401)
    assert_that(json_response['detail']).is_equal_to('Username or Password is wrong.')

@pytest.mark.tc_004
def test_empty_email():
    req = Requester()    
    url = f"{req.base_url}/staff/login"
    payload = {
        "email": "",
        "password": "Staff123!"
    }    
    json_payload: str = json.dumps(payload)
    response = requests.request(
        "POST", url, headers={}, data=json_payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('email field should not be empty')


@pytest.mark.tc_005
def test_empty_password():
    req = Requester()    
    url = f"{req.base_url}/staff/login"
    payload = {
        "email": "staffABC@gmail.com",
        "password": ""
    }    
    json_payload: str = json.dumps(payload)
    response = requests.request(
        "POST", url, headers={}, data=json_payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('password field should not be empty')


@pytest.mark.tc_006
def test_empty_email_and_password():
    req = Requester()    
    url = f"{req.base_url}/staff/login"
    payload = {
        "email": "",
        "password": ""
    }    
    json_payload: str = json.dumps(payload)
    response = requests.request(
        "POST", url, headers={}, data=json_payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('email field should not be empty')
    assert_that(json_response['detail'][1]['msg']).is_equal_to('password field should not be empty')
    
    
@pytest.mark.tc_007
def test_invalid_email_and_password():
    req = Requester()    
    url = f"{req.base_url}/staff/login"
    payload = {
        "email": "staffxABC@gmail.com",
        "password": "Staffx123!"
    }    
    json_payload: str = json.dumps(payload)
    response = requests.request(
        "POST", url, headers={}, data=json_payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(401)
    assert_that(json_response['detail']).is_equal_to('Username or Password is wrong.')


@pytest.mark.tc_008
def test_admin_login():
    req = Requester()    
    url = f"{req.base_url}/staff/login"
    payload = {
        "email": "adminXYZ@gmail.com",
        "password": "Admin123!"
    }    
    json_payload: str = json.dumps(payload)
    response = requests.request(
        "POST", url, headers={}, data=json_payload)
    json_response: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(json_response['access_token']).is_not_empty()