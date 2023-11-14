from tests.lib.mw_db import get_db
from pytest import fixture
import pdb, requests
import os, sys, json
from assertpy import assert_that
import re

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
import lib.generate_token as generate_token
from lib.requester import Requester

@fixture(scope="module")
def get_admin_token():
    print("\n---- Setup Test ----\n")
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

@pytest.mark.tc_001  # stats = Pending
def test_question_fetch_by_id_status_pending(get_admin_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    questions_returned: dict = get_db().question_collection.find_one({"question_status": question_status})
    sql_response_id: str = questions_returned['_id']
    url: str = f"{req.base_url}/v1/questions/{sql_response_id}"    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['question']['id'] == str(questions_returned['_id'])
    

@pytest.mark.tc_002 # status = Rejected
def test_question_fetch_by_id_status_rejected(get_admin_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    questions_returned: dict = get_db().question_collection.find_one({"question_status": question_status})
    sql_response_id: str = questions_returned['_id']
    url: str = f"{req.base_url}/v1/questions/{sql_response_id}"    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['question']['id'] == str(questions_returned['_id'])

@pytest.mark.tc_003  # status = Approved 
def test_question_fetch_by_id_status_approved(get_admin_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    questions_returned: dict = get_db().question_collection.find_one({"question_status": question_status})
    sql_response_id: str = questions_returned['_id']
    url: str = f"{req.base_url}/v1/questions/{sql_response_id}"    
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['question']['id'] == str(questions_returned['_id'])

@pytest.mark.tc_004  # status = Approved 
def test_question_fetch_by_id_status_reported(get_admin_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    questions_returned: dict = get_db().question_collection.find_one({"question_status": question_status})
    sql_response_id: str = str(questions_returned['_id'])
    url: str = f"{req.base_url}/v1/questions/{sql_response_id}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['question']['id'] == str(questions_returned['_id'])

@pytest.mark.tc_005  # invalid id format
def test_question_fetch_by_invalid_id_format(get_admin_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    questions_returned: dict = get_db().question_collection.find_one({"question_status": question_status})
    sql_response_id: str = str(questions_returned['_id']) + "dd"
    url: str = f"{req.base_url}/v1/questions/{sql_response_id}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    question_response: dict = json.loads(response.text)
    assert_that(question_response['detail']).is_equal_to('Question not found')

@pytest.mark.tc_006  # invalid id data
def test_question_fetch_by_invalid_id_data(get_admin_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    questions_returned: dict = get_db().question_collection.find_one({"question_status": question_status})
    sql_response_id: str = re.sub(r'\d+', 'z', str(questions_returned['_id']))
    url: str = f"{req.base_url}/v1/questions/{sql_response_id}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    question_response: dict = json.loads(response.text)
    assert_that(question_response['detail']).is_equal_to('Question not found')

@pytest.mark.tc_007 # invalid token 
def test_question_fetch_by_id_invalid_token(get_admin_token):
    req: Requester = Requester()    
    invalid_token: str = re.sub(r"\d+", "zz", get_admin_token)
    headers: dict = req.create_basic_headers(token=invalid_token)
    question_status: str = "Reported"
    questions_returned: dict = get_db().question_collection.find_one({"question_status": question_status})
    sql_response_id: str = str(questions_returned['_id'])
    url: str = f"{req.base_url}/v1/questions/{sql_response_id}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 403
    question_response: dict = json.loads(response.text)
    assert_that(question_response['detail']).is_equal_to('Invalid token')
    