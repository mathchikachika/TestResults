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
from lib.fetch_statistics import get_stat_by_question
from lib.mw_db import get_db



@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(email="staffABC@gmail.com", password="Staff123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.tc_001
def test_fetch_question_total_statistics(get_staff_token):
    req: Requester = Requester()
    # num_of_staar: int = get_db().question_collection.count_documents(
    #     {'question_type': 'STAAR', 'question_status': 'Approved'})

    # num_of_colleges: int = get_db().question_collection.count_documents(
    #     {'question_type': 'College Level', 'question_status': 'Approved'})

    # num_of_mathworlds: int = get_db().question_collection.count_documents(
    #     {'question_type': 'MathWorld', 'question_status': 'Approved'})
    
    total_num_of_questions: int = get_db().question_collection.count_documents({})

    headers: dict = req.create_basic_headers(token=get_staff_token)
    url: str = f"{req.base_url}/v1/questions/statistics/all"
    response = requests.request("GET", url, headers=headers)
    json_response: dict = json.loads(response.text)
    assert response.status_code == 200
    questions_stats: dict = json.loads(response.text)
    total_stat: int = questions_stats['data'][0]['total_no_of_questions'] + \
        questions_stats['data'][1]['total_no_of_questions'] + questions_stats['data'][2]['total_no_of_questions']
    assert_that(total_stat).is_equal_to(total_num_of_questions)

@pytest.mark.tc_002
def test_fetch_question_staar_total_count(get_staff_token):
    req: Requester = Requester()
    num_of_staars: int = get_db().question_collection.count_documents(
        {'question_type': 'STAAR', 'question_status': 'Approved'})
    headers: dict = req.create_basic_headers(token=get_staff_token)
    url: str = f"{req.base_url}/v1/questions/statistics/all"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(get_stat_by_question(questions_stats['data'],'STAAR')['no_of_approved_questions']).is_equal_to(num_of_staars)

@pytest.mark.tc_003
def test_fetch_question_college_total_count(get_staff_token):
    req: Requester = Requester()
    num_of_college: int = get_db().question_collection.count_documents(
        {'question_type': 'College Level', 'question_status': 'Approved'})
    headers: dict = req.create_basic_headers(token=get_staff_token)
    url: str = f"{req.base_url}/v1/questions/statistics/all"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(get_stat_by_question(questions_stats['data'],'College Level')['no_of_approved_questions']).is_equal_to(num_of_college)

@pytest.mark.tc_004
def test_fetch_question_mathworld_total_count(get_staff_token):
    req: Requester = Requester()
    num_of_mathword: int = get_db().question_collection.count_documents(
        {'question_type': 'Mathworld', 'question_status': 'Approved'})
    headers: dict = req.create_basic_headers(token=get_staff_token)
    url: str = f"{req.base_url}/v1/questions/statistics/all"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(get_stat_by_question(questions_stats['data'],'Mathworld')['no_of_approved_questions']).is_equal_to(num_of_mathword)

@pytest.mark.tc_005
def test_fetch_question_stats_invalid_token(get_staff_token):
    req: Requester = Requester()
    # num_of_mathword: int = get_db().question_collection.count_documents(
        # {'question_type': 'Mathworld', 'question_status': 'Approved'})
    headers: dict = req.create_basic_headers(token=get_staff_token + "x")
    url: str = f"{req.base_url}/v1/questions/statistics/all"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(403)
    assert_that(questions_stats['detail']).is_equal_to('Invalid token')

@pytest.mark.tc_007
def test_fetch_question_stats_pending(get_staff_token):
    req: Requester = Requester()
    num_of_mathword: int = get_db().question_collection.count_documents(
        {'question_type': 'Mathworld', 'question_status': 'Pending'})
    headers: dict = req.create_basic_headers(token=get_staff_token)
    url: str = f"{req.base_url}/v1/questions/statistics/all"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(get_stat_by_question(questions_stats['data'],'Mathworld')['no_of_pending_questions']).is_equal_to(num_of_mathword)

# @pytest.mark.tc_008
# def test_fetch_question_stats_rejected(get_staff_token):
#     req: Requester = Requester()
#     num_of_mathword: int = get_db().question_collection.count_documents(
#         {'question_type': 'Mathworld', 'question_status': 'Rejected'})
#     headers: dict = req.create_basic_headers(token=get_staff_token)
#     url: str = f"{req.base_url}/v1/questions/statistics/all"
#     response = requests.request("GET", url, headers=headers)
#     questions_stats: dict = json.loads(response.text)
#     assert_that(response.status_code).is_equal_to(200)
#     assert_that(questions_stats['data'][1]['no_of_reported_questions']).is_not_equal_to(num_of_mathword)

@pytest.mark.tc_009
def test_fetch_question_stats_reported(get_staff_token):
    req: Requester = Requester()
    num_of_mathword: int = get_db().question_collection.count_documents(
        {'question_type': 'Mathworld', 'question_status': 'Reported'})
    headers: dict = req.create_basic_headers(token=get_staff_token)
    url: str = f"{req.base_url}/v1/questions/statistics/all"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    print(questions_stats)
    assert_that(get_stat_by_question(questions_stats['data'],'Mathworld')['no_of_reported_questions']).is_equal_to(num_of_mathword)

# @pytest.mark.tc_011
# def test_fetch_question_stats_college(get_staff_token):
#     req: Requester = Requester()
#     num_of_college: int = get_db().question_collection.count_documents(
#         {'question_type': 'College Level', 'question_status': 'Rejected'})
#     headers: dict = req.create_basic_headers(token=get_staff_token)
#     url: str = f"{req.base_url}/v1/questions/statistics/all"
#     response = requests.request("GET", url, headers=headers)
#     questions_stats: dict = json.loads(response.text)
#     assert_that(response.status_code).is_equal_to(200)
#     assert_that(questions_stats['data'][0]['no_of_reported_questions']).is_not_equal_to(num_of_college)

@pytest.mark.tc_012
def test_fetch_question_stats_mathworld(get_staff_token):
    req: Requester = Requester()
    num_of_mathword: int = get_db().question_collection.count_documents(
        {'question_type': 'Mathworld'})
    headers: dict = req.create_basic_headers(token=get_staff_token)
    url: str = f"{req.base_url}/v1/questions/statistics/all"
    response = requests.request("GET", url, headers=headers)
    questions_stats: dict = json.loads(response.text)
    assert_that(response.status_code).is_equal_to(200)
    assert_that(get_stat_by_question(questions_stats['data'],'Mathworld')['no_of_reported_questions']).is_not_equal_to(num_of_mathword)
