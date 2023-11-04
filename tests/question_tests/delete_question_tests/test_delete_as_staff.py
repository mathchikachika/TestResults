from pytest import fixture
import pdb, requests
import os, sys, json

from tests.payloads.valid_question_payloads import get_valid_successful_college_payload, get_valid_successful_mathworld_payload, get_valid_successful_staar_payload

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

@pytest.mark.tc_001
def test_delete_staar(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    
    # Create Question
    
    create_response = requests.request("POST", create_url, headers=header, json=payload)
    json_create_response: dict = json.loads(create_response.text)
    print(json_create_response)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question
    question_id: str =  json_create_response['question_id']
    delete_url: str = f"{req.base_url}/v1/questions/delete/{question_id}"
    del_response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 200
    assert del_json_response['detail'] == "Successfully Deleted Question"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/v1/questions/{question_id}"
    fetch_response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 404
    assert json_fetch_response['detail'] == "Question not found"

@pytest.mark.tc_002
def test_delete_invalid_staar_uuid(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_staar_payload()
    # Create Question
    
    create_response = requests.request("POST", create_url, headers=header, json=payload)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question Attempt
    invalid_question_id: str =  common.replace_numbers_with_zero(json_create_response['question_id'])
    delete_url: str = f"{req.base_url}/v1/questions/delete/{invalid_question_id}"
    del_response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 404
    assert del_json_response['detail'] == "Question not found"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/v1/questions/{json_create_response['question_id']}"
    fetch_response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 200
    assert common.is_valid_id(json_fetch_response['question']['id']) == True

@pytest.mark.tc_003
def test_delete_mathworld(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    url: str = f"{req.base_url}/v1/questions/create"
    question1: str = common.get_random_question()
    question2: str = common.get_random_question()
    teks_code: str = common.get_random_tek_code()
    unit: str = common.get_random_unit()

    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url: str = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()

    # Create Question
    
    create_response: requests.models.Response = \
        requests.request("POST", create_url, headers=header, json=payload)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question
    question_id: str =  json_create_response['question_id']
    delete_url: str = f"{req.base_url}/v1/questions/delete/{question_id}"
    del_response: requests.models.Response = \
          requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 200
    assert del_json_response['detail'] == "Successfully Deleted Question"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/v1/questions/{question_id}"
    fetch_response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 404
    assert json_fetch_response['detail'] == "Question not found"

@pytest.mark.tc_004
def test_delete_invalid_mathworld_id(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url: str = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_mathworld_payload()

    # Create Question
    
    create_response: requests.models.Response = \
        requests.request("POST", create_url, headers=header, json=payload)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question Attempt
    invalid_question_id: str =  common.replace_numbers_with_zero(json_create_response['question_id'])
    delete_url: str = f"{req.base_url}/v1/questions/delete/{invalid_question_id}"
    del_response: requests.models.Response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 404
    assert del_json_response['detail'] == "Question not found"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/v1/questions/{json_create_response['question_id']}"
    fetch_response: requests.Response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 200
    assert common.is_valid_id(json_fetch_response['question']['id']) == True

@pytest.mark.tc_005
def test_delete_college(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url = f"{req.base_url}/v1/questions/create"
    
    payload = get_valid_successful_college_payload()

    # Create Question
    
    create_response = requests.request("POST", create_url, headers=header, json=payload)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question
    question_id: str =  json_create_response['question_id']
    delete_url: str = f"{req.base_url}/v1/questions/delete/{question_id}"
    del_response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 200
    assert del_json_response['detail'] == "Successfully Deleted Question"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/v1/questions/{question_id}"
    fetch_response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 404
    assert json_fetch_response['detail'] == "Question not found"

@pytest.mark.tc_006
def test_delete_invalid_college_uuid(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url: str = f"{req.base_url}/v1/questions/create"

    
    payload = get_valid_successful_college_payload()

    # Create Question
    
    create_response: requests.models.Response = \
        requests.request("POST", create_url, headers=header, json=payload)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question Attempt
    invalid_question_id: str =  common.replace_numbers_with_zero(json_create_response['question_id'])
    delete_url: str = f"{req.base_url}/v1/questions/delete/{invalid_question_id}"
    del_response: requests.models.Response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 404
    assert del_json_response['detail'] == "Question not found"

    # Fetch Question
    fetch_url: str = f"{req.base_url}/v1/questions/{json_create_response['question_id']}"
    fetch_response: requests.Response = requests.request("GET", fetch_url, headers=header)
    json_fetch_response: dict = json.loads(fetch_response.text)
    assert fetch_response.status_code == 200
    assert common.is_valid_id(json_fetch_response['question']['id']) == True

@pytest.mark.tc_007
def test_unauthorized_delete(get_staff_token):
    req = Requester()
    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url: str = f"{req.base_url}/v1/questions/create"

    payload = get_valid_successful_college_payload()

    # Create Question
    
    create_response: requests.models.Response = requests.request("POST", create_url, headers=header, json=payload)
    json_create_response: dict = json.loads(create_response.text)
    assert json_create_response['detail'] == "Successfully Added Question"

    # Delete Question Attempt
    invalid_question_id: str =  common.replace_numbers_with_zero(json_create_response['question_id'])
    delete_url: str = f"{req.base_url}/v1/questions/delete/{invalid_question_id}"
    header.update( {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.2yJkYXRhIjoiaEFJN3JhU0ppR2htcGFCYW5HQUd1azUxMjk1bXdMcCtaTlZuV21xb1pvbERCK1BaZXFHTFMzTEdCTWdRYVJLR3QrOE9XVS95NDREdTNBRUtKeDU0emtic0VjRzN6UFhKN2U4ZllmZi9NY0NYRFMrZGJvdjJvL1V4NWlDVm9PV2NYQWZPemNvamgrUXBPL0JXMkJYeGZLMFR5ZzR3ZE13PSo2cEorTk9Kb3NYQ2lWMFR1Q3ZpNEJ3PT0qKzR5WWJUWGVQSHRHMkpPZGVyWHJOUT09Knl2VEhycGxHRmcvUDlTenE1OWpRZHc9PSJ9.eb2Tccc-65rXGn-O4bxq2_Sbr2iVwhR3rcCxIxVvAYI'})
    del_response: requests.models.Response = requests.request("DELETE", delete_url, headers=header)
    del_json_response: dict = json.loads(del_response.text)
    assert del_response.status_code == 403
    assert del_json_response['detail'] == "Invalid token"
