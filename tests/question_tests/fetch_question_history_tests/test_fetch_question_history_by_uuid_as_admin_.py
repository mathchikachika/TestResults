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



@fixture(scope="module")
def get_admin_token():    
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_fetch_staar_question_history_by_id(get_admin_token):
    req: Requester = Requester()    
    sql_staar_returned: dict = get_db().question_collection.find_one({'question_type': 'STAAR'})    
    headers: dict = req.create_basic_headers(token=get_admin_token)    
    sql_id: str = sql_staar_returned['_id']
    url: str = f"{req.base_url}/v1/questions/{sql_id}"      
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(ObjectId(questions['question']['id'])).is_equal_to(ObjectId(sql_id))
    # assert_that(len(questions['history'])).is_greater_than(0)

@pytest.mark.tc_002
def test_fetch_staar_question_history_by_invalid_uuid(get_admin_token):
    req: Requester = Requester()      
    sql_staar_returned: dict = get_db().question_collection.find_one({'question_type': 'STAAR'})
            
    headers: dict = req.create_basic_headers(token=get_admin_token)    
    sql_uuid: str = str(sql_staar_returned['_id']) + "123"
    url: str = f"{req.base_url}/v1/questions/{sql_uuid}"          
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    json_response: dict = json.loads(response.text)    
    assert_that(json_response['detail']).is_equal_to("Question not found")