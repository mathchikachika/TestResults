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
def test_admin_register_staff(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(json_response['detail']).is_equal_to("Successfully Added Staff")

@pytest.mark.tc_002
def test_admin_register_staff_invalid_token(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token + "ds")
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(json_response['detail']).is_equal_to("Invalid token or expired token.")

@pytest.mark.tc_003
def test_admin_register_staff_no_fname(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("first_name field should not be empty")

@pytest.mark.tc_004
def test_admin_register_staff_no_middle_init(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(json_response['detail']).is_equal_to("Successfully Added Staff")

@pytest.mark.tc_005
def test_admin_register_staff_no_lname(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "S", "last_name": "", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("last_name field should not be empty")


@pytest.mark.tc_006
def test_admin_register_staff_no_role(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("value is not a valid enumeration member; permitted: 'staff', 'admin', 'subscriber'")

@pytest.mark.tc_007
def test_admin_register_staff_no_school(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(json_response['detail']).is_equal_to("Successfully Added Staff")

@pytest.mark.tc_008
def test_admin_register_staff_no_email(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("email field should not be empty")

@pytest.mark.tc_009
def test_admin_register_staff_no_password(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "", "repeat_password": "'+ random_data['password'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password field should not be empty")

@pytest.mark.tc_010
def test_admin_register_staff_no_password2(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("repeat_password field should not be empty")

@pytest.mark.tc_011
def test_admin_register_staff_no_matched_passwords(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "'+ random_data['password'] +'", "repeat_password": "'+ random_data['email'] +'", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password do not match")

@pytest.mark.tc_012
def test_admin_register_staff_lt_password(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "sxrQ77$", "repeat_password": "sxrQ77", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

@pytest.mark.tc_013
def test_admin_register_staff_password_no_upper(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "sxr77$$t", "repeat_password": "sxr77$$t", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

@pytest.mark.tc_014
def test_admin_register_staff_password_no_lower(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "SXRQ77$$T", "repeat_password": "SXRQ77$$T", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

@pytest.mark.tc_015
def test_admin_register_staff_password_no_special_char(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "SXRQ7TTTdxT", "repeat_password": "SXRQ7TTTdxT", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

@pytest.mark.tc_016
def test_admin_register_staff_password_no_num(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "SXRQ$TTTdxT", "repeat_password": "SXRQ$TTTdxT", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

@pytest.mark.tc_017
def test_admin_register_staff_password_max(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$T6", "repeat_password": "SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$T6", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(201)
    assert_that(json_response['detail']).is_equal_to("Successfully Added Staff")

@pytest.mark.tc_018
def test_admin_register_staff_password_max_plus(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$T632", "repeat_password": "SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$T632", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

@pytest.mark.tc_019
def test_admin_register_staff_password_space(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$ T6", "repeat_password": "SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$ T6", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

@pytest.mark.tc_020
def test_admin_register_staff_password_lead_space(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": " SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$T6", "repeat_password": " SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$T6", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

@pytest.mark.tc_021
def test_admin_register_staff_password_trail_space(get_admin_token):
    req = Requester()
    random_data: dict = json.loads(common.create_fake_register())
    payload = '{"first_name": "'+ random_data['first_name'] +'", "middle_name": "'+ random_data['middle_name'] +'", "last_name": "'+ random_data['last_name'] +'", "role": "'+ random_data['role'] +'", "school": "'+ random_data['school'] +'", "email": "'+ random_data['email'] +'", "password": "SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$T6 ", "repeat_password": "SXRQ$TTTdxTSXRQ$TTTdxTSXRQ$T6 ", "created_by": "'+ random_data['created_by'] +'"}'
    header: dict = req.create_basic_headers(token=get_admin_token)
    url = f"{req.base_url}/staff/register"    
    response = requests.request(
        "POST", url, headers=header, data=payload)
    json_response = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("password is invalid: [a-z], [A-Z], [0-9],[@$!#%*?&], min: 8, max:30")

