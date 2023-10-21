from pytest import fixture
import pdb, requests
import os, sys, json

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

@pytest.mark.tc_001
def test_question_fetch_by_uuid_pending_satus(get_staff_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_staff_token)
    question_status: str = "Pending"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    url: str = f"{req.base_url}/question/fetch/{questions_returned[0][0]}"    
    sql_pending_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['Question']['uuid'] == questions_returned[0][0]
    pass

@pytest.mark.tc_002
def test_question_fetch_by_uuid_rejected(get_staff_token):
    req: Requester = Requester()    
    headers: dict = req.create_basic_headers(token=get_staff_token)
    question_status: str = "Rejected"
    questions_returned: list = execute_query(
        f"SELECT * FROM mathworld.question WHERE status = '{question_status}' LIMIT 1")
    url: str = f"{req.base_url}/question/fetch/{questions_returned[0][0]}"    
    sql_pending_questions: int = len(questions_returned)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    question: dict = json.loads(response.text)
    assert question['Question']['uuid'] == questions_returned[0][0]
    pass