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

@pytest.mark.tc_001
def test_staff_register_staff(get_staff_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_staff_token)
    url = f"{req.base_url}/staff/register"        
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to("Invalid token or expired token.")

@pytest.mark.tc_002
def test_staff_register_invalid_tokne(get_staff_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token="")
    url = f"{req.base_url}/staff/register"        
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to("Not authenticated")
