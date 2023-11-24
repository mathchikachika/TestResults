import json
import os
import pdb
import random
import sys
import time

import requests
from assertpy import assert_that
from pytest import fixture

from tests.lib.mw_db import get_db

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger

import lib.common as common
import lib.generate_token as generate_token
import pytest
from faker import Faker

# from lib.mw_sql import execute_query
from lib.requester import Requester

fake = Faker()


@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(
        email="adminXYZ@gmail.com", password="Admin123!"
    )
    yield token
    print("\n\n---- Tear Down Test ----\n")


@pytest.mark.order(1)
def test_pending_questions(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status}
    )

    sql_pending_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_pending_questions)


@pytest.mark.order(2)
def test_approved_questions(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status}
    )

    sql_approved_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_approved_questions)


@pytest.mark.order(3)
def test_rejected_questions(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status}
    )

    sql_rejected_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_rejected_questions)


@pytest.mark.order(4)
def test_reported_questions(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status}
    )
    sql_rejected_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_rejected_questions)


@pytest.mark.order(5)
def test_staar_type_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )

    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(6)
def test_pending_status_staar_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(7)
def test_college_level_type_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(8)
def test_pending_status_college_level_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(9)
def test_pending_status_mathworld_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(10)
def test_mathworld_type_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(11)
def test_approved_status_college_level_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(12)
def test_college_level_type_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(13)
def test_approved_status_mathworld_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(14)
def test_mathworld_type_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(15)
def test_rejected_status_mathworld_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(16)
def test_mathworld_type_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(17)
def test_rejected_status_college_level_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(18)
def test_college_level_type_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(19)
def test_rejected_status_staar_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(20)
def test_staar_type_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(21)
def test_reported_status_staar_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(22)
def test_staar_type_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(23)
def test_reported_status__type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(24)
def test_college_level_type_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(25)
def test_reported_status_mathworld_type(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(26)
def test_mathworld_type_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "question_type": question_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(28)
def test_ore_response_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )

    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(29)
def test_approved_status_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(30)
def test_ore_response_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(31)
def test_rejected_status_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(32)
def test_ore_response_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(33)
def test_reported_status_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(34)
def test_ore_response_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(35)
def test_pending_status_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(36)
def test_ror_response_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {"question_status": question_status, "response_type": response_type}
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(37)
def test_pending_status_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(38)
def test_mc_response_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(39)
def test_pending_status_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(38)
def test_cb_response_pending_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


# --------
@pytest.mark.order(39)
def test_approved_status_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(40)
def test_ror_response_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(41)
def test_approved_status_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(42)
def test_mc_response_approved_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(43)
def test_rejected_status_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(44)
def test_ror_response_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(45)
def test_reported_status_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(46)
def test_ror_response_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(47)
def test_rejected_status_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(48)
def test_mc_response_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(49)
def test_reported_status_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(50)
def test_mc_response_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(51)
def test_rejected_status_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(52)
def test_cb_response_rejected_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(53)
def test_cb_response_reported_status(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(54)
def test_reported_status_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(55)
def test_pending_status_staar_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    response_type: str = "Open Response Exact"
    question_type: str = "STAAR"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(56)
def test_approved_status_staar_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    response_type: str = "Open Response Exact"
    question_type: str = "STAAR"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(57)
def test_rejected_status_staar_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(58)
def test_reported_status_staar_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(59)
def test_pending_status_college_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(60)
def test_approved_status_college_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(61)
def test_rejected_status_college_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(62)
def test_reported_status_college_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(63)
def test_pending_status_mathworld_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(64)
def test_approved_status_mathworld_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(65)
def test_rejected_status_mathworld_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(66)
def test_reported_status_mathworld_type_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(67)
def test_pending_status_college_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(68)
def test_approved_status_college_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(69)
def test_rejected_status_college_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(70)
def test_reported_status_college_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(71)
def test_pending_status_mathworld_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(72)
def test_approved_status_mathworld_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(73)
def test_rejected_status_mathworld_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(74)
def test_reported_status_mathworld_type_ror_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(75)
def test_pending_status_staar_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(76)
def test_approved_status_staar_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(77)
def test_rejected_status_staar_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(78)
def test_reported_status_staar_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(79)
def test_pending_status_college_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(80)
def test_approved_status_college_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(81)
def test_rejected_status_college_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(82)
def test_reported_status_college_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(83)
def test_pending_status_mathworld_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(84)
def test_approved_status_mathworld_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(85)
def test_rejected_status_mathworld_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(86)
def test_reported_status_mathworld_type_mc_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(87)
def test_pending_status_staar_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)

    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    print(questions)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(88)
def test_approved_status_staar_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(89)
def test_rejected_status_staar_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(90)
def test_reported_status_staar_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(91)
def test_pending_status_college_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(92)
def test_approved_status_college_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(93)
def test_rejected_status_college_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(94)
def test_reported_status_college_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(95)
def test_pending_status_mathworld_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(96)
def test_approved_status_mathworld_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(97)
def test_rejected_status_mathworld_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


@pytest.mark.order(98)
def test_reported_status_mathworld_type_cb_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported    "
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&response_type={response_type}&question_status={question_status}"
    questions_returned = get_db().question_collection.count_documents(
        {
            "question_type": question_type,
            "question_status": question_status,
            "response_type": response_type,
        }
    )
    sql_questions: int = questions_returned
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert_that(questions["total"]).is_greater_than_or_equal_to(sql_questions)


# --------------------------------------------page 1--------------------------------------------------------------------


@pytest.mark.order(99)
def test_pending_questions_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(100)
def test_approved_questions_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(101)
def test_rejected_questions_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(102)
def test_reported_questions_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    # assert questions['data'] != []


@pytest.mark.order(103)
def test_staar_type_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(104)
def test_pending_status_staar_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(105)
def test_college_level_type_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(106)
def test_pending_status_college_level_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(107)
def test_pending_status_mathworld_type_Page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(108)
def test_mathworld_type_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}&question_type={question_type}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(109)
def test_approved_status_college_level_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(110)
def test_college_level_type_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(111)
def test_approved_status_mathworld_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(112)
def test_mathworld_type_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(113)
def test_rejected_status_mathworld_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(114)
def test_mathworld_type_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(115)
def test_rejected_status_college_level_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(116)
def test_college_level_type_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(117)
def test_rejected_status_staar_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(118)
def test_staar_type_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(119)
def test_reported_status_staar_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(120)
def test_staar_type_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(121)
def test_reported_status__type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(122)
def test_college_level_type_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(123)
def test_reported_status_mathworld_type_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 1
    create_response: dict = common.create_a_mathworld_question("admin")
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(124)
def test_mathworld_type_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 1
    create_response: dict = common.create_a_mathworld_question("admin")
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(125)
def test_pending_status_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(126)
def test_ore_response_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(127)
def test_approved_status_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(128)
def test_ore_response_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(129)
def test_rejected_status_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(130)
def test_ore_response_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(131)
def test_reported_status_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(132)
def test_ore_response_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(133)
def test_pending_status_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(134)
def test_ror_response_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(135)
def test_pending_status_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(136)
def test_mc_response_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(137)
def test_pending_status_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(138)
def test_cb_response_pending_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


# --------
@pytest.mark.order(139)
def test_approved_status_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    question_classic: dict = get_db().question_collection.find_one(
        {"response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(140)
def test_ror_response_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    question_classic: dict = get_db().question_collection.find_one(
        {"response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(141)
def test_approved_status_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(142)
def test_mc_response_approved_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(143)
def test_rejected_status_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(144)
def test_ror_response_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(145)
def test_reported_status_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(146)
def test_ror_response_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(147)
def test_rejected_status_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(148)
def test_mc_response_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(149)
def test_reported_status_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(150)
def test_mc_response_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(151)
def test_rejected_status_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(152)
def test_cb_response_rejected_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(153)
def test_cb_response_reported_status_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(154)
def test_reported_status_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(155)
def test_pending_status_staar_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(156)
def test_approved_status_staar_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(157)
def test_rejected_status_staar_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(158)
def test_reported_status_staar_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(159)
def test_pending_status_college_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(160)
def test_approved_status_college_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(161)
def test_rejected_status_college_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(162)
def test_reported_status_college_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(163)
def test_pending_status_mathworld_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(164)
def test_approved_status_mathworld_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(165)
def test_rejected_status_mathworld_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(166)
def test_reported_status_mathworld_type_ore_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = 1
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(167)
def test_pending_status_college_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(168)
def test_approved_status_college_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"

    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)

    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    print(questions)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(169)
def test_rejected_status_college_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(170)
def test_reported_status_college_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(171)
def test_pending_status_mathworld_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(172)
def test_approved_status_mathworld_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)

    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(173)
def test_rejected_status_mathworld_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(174)
def test_reported_status_mathworld_type_ror_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_new_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    mathworld_response: dict = common.create_a_mathworld_question(
        "admin", response_type
    )
    qustion_uuid: str = mathworld_response["question_id"]
    mathworld_status = common.update_question_status(qustion_uuid, question_new_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_new_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(175)
def test_pending_status_staar_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(176)
def test_approved_status_staar_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(177)
def test_rejected_status_staar_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(178)
def test_reported_status_staar_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(179)
def test_pending_status_college_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


def test_approved_status_college_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    mathworld_response: dict = common.create_a_mathworld_question(
        "admin", response_type
    )
    qustion_uuid: str = mathworld_response["question_id"]
    mathworld_status = common.update_question_status(qustion_uuid, response_type)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(181)
def test_rejected_status_college_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(182)
def test_reported_status_college_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(183)
def test_pending_status_mathworld_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["data"] != []
    assert questions["page"] == page_num


@pytest.mark.order(184)
def test_approved_status_mathworld_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(185)
def test_rejected_status_mathworld_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(186)
def test_reported_status_mathworld_type_mc_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    mathworld_response = common.create_a_mathworld_question("admin", response_type)
    time.sleep(1)
    mathworld_status = common.update_question_status(
        mathworld_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(187)
def test_pending_status_staar_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(188)
def test_approved_status_staar_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(189)
def test_rejected_status_staar_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.key
@pytest.mark.order(190)
def test_reported_status_staar_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num


@pytest.mark.order(191)
def test_pending_status_college_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(192)
def test_approved_status_college_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(193)
def test_rejected_status_college_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    create_response = common.create_a_college_question("admin", response_type)
    assert_that(create_response["detail"]).is_equal_to("Successfully Added Question")
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(194)
def test_reported_status_college_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(195)
def test_pending_status_mathworld_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(196)
def test_approved_status_mathworld_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(197)
def test_rejected_status_mathworld_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.key
@pytest.mark.order(198)
def test_reported_status_mathworld_type_cb_response_page_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    mathworld_response = common.create_a_mathworld_question("admin", response_type)
    mathworld_status = common.update_question_status(
        mathworld_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


# ------------------------ page_num = 100 ------------------------


@pytest.mark.order(199)
def test_pending_questions_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(200)
def test_approved_questions_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = 100
    mathworld_response = common.create_a_mathworld_question("admin")
    mathworld_status = common.update_question_status(
        mathworld_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(201)
def test_rejected_questions_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question("admin")
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status='{question_status}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num


@pytest.mark.order(202)
def test_reported_questions_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(203)
def test_staar_type_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(204)
def test_pending_status_staar_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(205)
def test_college_level_type_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(206)
def test_pending_status_college_level_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(207)
def test_pending_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question("admin")
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_type='{question_type}'&question_status='{question_status}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(208)
def test_mathworld_type_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status='{question_status}'&page_num={page_num}&question_type='{question_type}'"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(209)
def test_approved_status_college_level_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(210)
def test_college_level_type_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(211)
def test_approved_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question("admin")
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_type='{question_type}'&question_status='{question_status}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(212)
def test_mathworld_type_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    create_response: dict = common.create_a_mathworld_question("admin")
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(213)
def test_rejected_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(214)
def test_mathworld_type_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(215)
def test_rejected_status_college_level_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == 100
    assert questions["data"] == []


@pytest.mark.order(216)
def test_college_level_type_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(217)
def test_rejected_status_staar_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(218)
def test_staar_type_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(219)
def test_reported_status_staar_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?uestion_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(220)
def test_staar_type_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(221)
def test_reported_status__type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(222)
def test_college_level_type_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(223)
def test_reported_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(224)
def test_mathworld_type_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status='{question_status}'&question_type='{question_type}'&page_num={page_num}"
    create_response: dict = common.create_a_mathworld_question("admin")
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(225)
def test_pending_status_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(226)
def test_ore_response_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(227)
def test_approved_status_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(228)
def test_ore_response_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(229)
def test_rejected_status_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(230)
def test_ore_response_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(231)
def test_reported_status_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(232)
def test_ore_response_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(233)
def test_pending_status_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(235)
def test_pending_status_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(236)
def test_mc_response_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(237)
def test_pending_status_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(238)
def test_cb_response_pending_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


# --------
@pytest.mark.order(239)
def test_approved_status_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(240)
def test_ror_response_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(241)
def test_approved_status_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(242)
def test_mc_response_approved_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(243)
def test_rejected_status_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(244)
def test_ror_response_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(245)
def test_reported_status_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(246)
def test_ror_response_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(247)
def test_rejected_status_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(248)
def test_mc_response_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(249)
def test_reported_status_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(250)
def test_mc_response_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(251)
def test_rejected_status_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(252)
def test_cb_response_rejected_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(253)
def test_cb_response_reported_status_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num


@pytest.mark.order(254)
def test_reported_status_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num


@pytest.mark.order(255)
def test_pending_status_staar_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(256)
def test_approved_status_staar_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(257)
def test_rejected_status_staar_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(258)
def test_reported_status_staar_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(259)
def test_pending_status_college_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    common.create_a_college_question("admin", response_type)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(260)
def test_approved_status_college_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(261)
def test_rejected_status_college_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(262)
def test_reported_status_college_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(263)
def test_pending_status_mathworld_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status='{question_status}'&question_type='{question_type}'&response_type='{response_type}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(264)
def test_approved_status_mathworld_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(265)
def test_rejected_status_mathworld_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(266)
def test_reported_status_mathworld_type_ore_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = 100
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(267)
def test_pending_status_college_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(268)
def test_approved_status_college_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(269)
def test_rejected_status_college_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(270)
def test_reported_status_college_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(271)
def test_pending_status_mathworld_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(272)
def test_approved_status_mathworld_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(273)
def test_rejected_status_mathworld_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.key
@pytest.mark.order(274)
def test_reported_status_mathworld_type_ror_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 100
    mathworld_response: dict = common.create_a_mathworld_question(
        "admin", response_type
    )
    mathworld_status = common.update_question_status(
        mathworld_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(275)
def test_pending_status_staar_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(276)
def test_approved_status_staar_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(277)
def test_rejected_status_staar_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(278)
def test_reported_status_staar_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(279)
def test_pending_status_college_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(280)
def test_approved_status_college_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(281)
def test_rejected_status_college_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(282)
def test_reported_status_college_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(283)
def test_pending_status_mathworld_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(284)
def test_approved_status_mathworld_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(285)
def test_rejected_status_mathworld_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(286)
def test_reported_status_mathworld_type_mc_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(287)
def test_pending_status_staar_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    print(questions)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(288)
def test_approved_status_staar_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(289)
def test_rejected_status_staar_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(290)
def test_reported_status_staar_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(291)
def test_pending_status_college_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status='{question_status}'&question_type='{question_type}'&response_type='{response_type}'&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(292)
def test_approved_status_college_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    # json_patch_response = json.loads(patch_response.text)
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(293)
def test_rejected_status_college_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(294)
def test_reported_status_college_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(295)
def test_pending_status_mathworld_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(296)
def test_approved_status_mathworld_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


@pytest.mark.order(297)
def test_rejected_status_mathworld_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 100
    create_response: dict = common.create_a_mathworld_question("admin")
    time.sleep(2)
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(298)
def test_reported_status_mathworld_type_cb_response_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] == []


# ------------- page_num = 0 ---------------------------------------------------------------------------------------------------------


@pytest.mark.order(299)
def test_pending_questions_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(300)
def test_approved_questions_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(301)
def test_rejected_questions_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(302)
def test_reported_questions_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(303)
def test_staar_type_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(304)
def test_pending_status_staar_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(305)
def test_college_level_type_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(306)
def test_pending_status_college_level_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(307)
def test_pending_status_mathworld_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(308)
def test_mathworld_type_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}&question_type={question_type}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(309)
def test_approved_status_college_level_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(310)
def test_college_level_type_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(311)
def test_approved_status_mathworld_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(312)
def test_mathworld_type_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(313)
def test_rejected_status_mathworld_type_page_100(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 100
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == 100
    assert questions["data"] != []


@pytest.mark.order(314)
def test_mathworld_type_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(315)
def test_rejected_status_college_level_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(316)
def test_college_level_type_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(317)
def test_rejected_status_staar_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(318)
def test_staar_type_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(319)
def test_reported_status_staar_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(320)
def test_staar_type_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(321)
def test_reported_status__type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(322)
def test_college_level_type_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(323)
def test_reported_status_mathworld_type_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(324)
def test_mathworld_type_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(325)
def test_pending_status_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(326)
def test_ore_response_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(327)
def test_approved_status_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(328)
def test_ore_response_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(329)
def test_rejected_status_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(330)
def test_ore_response_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(331)
def test_reported_status_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(332)
def test_ore_response_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(333)
def test_pending_status_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(334)
def test_ror_response_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(335)
def test_pending_status_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(336)
def test_mc_response_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(337)
def test_pending_status_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(338)
def test_cb_response_pending_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


# --------
@pytest.mark.order(339)
def test_approved_status_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(340)
def test_ror_response_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(341)
def test_approved_status_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(342)
def test_mc_response_approved_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(343)
def test_rejected_status_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(344)
def test_ror_response_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(345)
def test_reported_status_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(346)
def test_ror_response_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(347)
def test_rejected_status_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(348)
def test_mc_response_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(349)
def test_reported_status_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(350)
def test_mc_response_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(351)
def test_rejected_status_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(352)
def test_cb_response_rejected_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(353)
def test_cb_response_reported_status_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(354)
def test_reported_status_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(355)
def test_pending_status_staar_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(356)
def test_approved_status_staar_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(357)
def test_rejected_status_staar_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(358)
def test_reported_status_staar_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(359)
def test_pending_status_college_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(360)
def test_approved_status_college_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(361)
def test_rejected_status_college_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(362)
def test_reported_status_college_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(363)
def test_pending_status_mathworld_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(364)
def test_approved_status_mathworld_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(365)
def test_rejected_status_mathworld_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(366)
def test_reported_status_mathworld_type_ore_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = 0
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(367)
def test_pending_status_college_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(368)
def test_approved_status_college_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(369)
def test_rejected_status_college_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(370)
def test_reported_status_college_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(371)
def test_pending_status_mathworld_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(372)
def test_approved_status_mathworld_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(373)
def test_rejected_status_mathworld_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(374)
def test_reported_status_mathworld_type_ror_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(375)
def test_pending_status_staar_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(376)
def test_approved_status_staar_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(377)
def test_rejected_status_staar_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(378)
def test_reported_status_staar_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(379)
def test_pending_status_college_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(380)
def test_approved_status_college_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(381)
def test_rejected_status_college_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(382)
def test_reported_status_college_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(383)
def test_pending_status_mathworld_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(384)
def test_approved_status_mathworld_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(385)
def test_rejected_status_mathworld_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(386)
def test_reported_status_mathworld_type_mc_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(387)
def test_pending_status_staar_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(388)
def test_approved_status_staar_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(389)
def test_rejected_status_staar_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(390)
def test_reported_status_staar_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(391)
def test_pending_status_college_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(392)
def test_approved_status_college_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(393)
def test_rejected_status_college_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(394)
def test_reported_status_college_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(395)
def test_pending_status_mathworld_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(396)
def test_approved_status_mathworld_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(397)
def test_rejected_status_mathworld_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(398)
def test_reported_status_mathworld_type_cb_response_page_0(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


# -------------------------------------------- page_num = empty -------------------------------------------------------


@pytest.mark.order(399)
def test_pending_questions_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(400)
def test_approved_questions_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(401)
def test_rejected_questions_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(402)
def test_reported_questions_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(403)
def test_staar_type_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(404)
def test_pending_status_staar_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(405)
def test_college_level_type_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(406)
def test_pending_status_college_level_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(407)
def test_pending_status_mathworld_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(408)
def test_mathworld_type_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}&question_type={question_type}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(409)
def test_approved_status_college_level_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(410)
def test_college_level_type_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(411)
def test_approved_status_mathworld_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(412)
def test_mathworld_type_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(413)
def test_rejected_status_mathworld_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(414)
def test_mathworld_type_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(415)
def test_rejected_status_college_level_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(416)
def test_college_level_type_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(417)
def test_rejected_status_staar_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(418)
def test_staar_type_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(419)
def test_reported_status_staar_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(420)
def test_staar_type_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(421)
def test_reported_status__type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(422)
def test_college_level_type_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(423)
def test_reported_status_mathworld_type_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(424)
def test_mathworld_type_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(425)
def test_pending_status_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(426)
def test_ore_response_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(427)
def test_approved_status_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(428)
def test_ore_response_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(429)
def test_rejected_status_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(430)
def test_ore_response_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(431)
def test_reported_status_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(432)
def test_ore_response_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(433)
def test_pending_status_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(434)
def test_ror_response_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(435)
def test_pending_status_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(436)
def test_mc_response_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(437)
def test_pending_status_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(438)
def test_cb_response_pending_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


# --------
@pytest.mark.order(439)
def test_approved_status_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(440)
def test_ror_response_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(441)
def test_approved_status_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(442)
def test_mc_response_approved_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(443)
def test_rejected_status_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(444)
def test_ror_response_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(445)
def test_reported_status_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(446)
def test_ror_response_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(447)
def test_rejected_status_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(448)
def test_mc_response_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(449)
def test_reported_status_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(450)
def test_mc_response_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(451)
def test_rejected_status_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(452)
def test_cb_response_rejected_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(453)
def test_cb_response_reported_status_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(454)
def test_reported_status_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(455)
def test_pending_status_staar_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(456)
def test_approved_status_staar_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(457)
def test_rejected_status_staar_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(458)
def test_reported_status_staar_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(459)
def test_pending_status_college_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(460)
def test_approved_status_college_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(461)
def test_rejected_status_college_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(462)
def test_reported_status_college_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(463)
def test_pending_status_mathworld_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(464)
def test_approved_status_mathworld_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(465)
def test_rejected_status_mathworld_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(466)
def test_reported_status_mathworld_type_ore_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: str = ""
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(467)
def test_pending_status_college_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(468)
def test_approved_status_college_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(469)
def test_rejected_status_college_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(470)
def test_reported_status_college_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(471)
def test_pending_status_mathworld_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(472)
def test_approved_status_mathworld_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(473)
def test_rejected_status_mathworld_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(474)
def test_reported_status_mathworld_type_ror_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(475)
def test_pending_status_staar_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(476)
def test_approved_status_staar_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(477)
def test_rejected_status_staar_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(478)
def test_reported_status_staar_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(479)
def test_pending_status_college_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(480)
def test_approved_status_college_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(481)
def test_rejected_status_college_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(482)
def test_reported_status_college_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(483)
def test_pending_status_mathworld_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(484)
def test_approved_status_mathworld_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(485)
def test_rejected_status_mathworld_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(486)
def test_reported_status_mathworld_type_mc_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(487)
def test_pending_status_staar_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(488)
def test_approved_status_staar_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(489)
def test_rejected_status_staar_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(490)
def test_reported_status_mathworld_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(491)
def test_pending_status_college_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(492)
def test_approved_status_college_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(493)
def test_rejected_status_college_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(494)
def test_reported_status_college_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(495)
def test_pending_status_mathworld_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(496)
def test_approved_status_mathworld_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(497)
def test_rejected_status_mathworld_type_cb_response_page_empty(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


@pytest.mark.order(498)
def test_reported_status_mathworld_type_cb_response_page_empyt(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: str = ""
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 422
    questions: dict = json.loads(response.text)
    assert (
        questions["detail"][0]["msg"]
        == "Input should be a valid integer, unable to parse string as an integer"
    )


# ------------------------------ page_num = negative ---------------------------------


@pytest.mark.order(499)
def test_pending_questions_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(500)
def test_approved_questions_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(501)
def test_rejected_questions_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(502)
def test_reported_questions_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(503)
def test_staar_type_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(504)
def test_pending_status_staar_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(505)
def test_college_level_type_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(506)
def test_pending_status_college_level_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(507)
def test_pending_status_mathworld_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(508)
def test_mathworld_type_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}&question_type={question_type}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(509)
def test_approved_status_college_level_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&page_num={page_num}&question_status={question_status}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(510)
def test_college_level_type_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    time.sleep(1)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(511)
def test_approved_status_mathworld_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(512)
def test_mathworld_type_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(513)
def test_rejected_status_mathworld_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(514)
def test_mathworld_type_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(515)
def test_rejected_status_college_level_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(516)
def test_college_level_type_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(517)
def test_rejected_status_staar_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(518)
def test_staar_type_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(519)
def test_reported_status_staar_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(520)
def test_staar_type_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(521)
def test_reported_status__type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(522)
def test_college_level_type_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(523)
def test_reported_status_mathworld_type_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "mathworld"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(524)
def test_mathworld_type_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(525)
def test_pending_status_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(526)
def test_ore_response_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(527)
def test_approved_status_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(528)
def test_ore_response_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(529)
def test_rejected_status_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(530)
def test_ore_response_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(531)
def test_reported_status_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(532)
def test_ore_response_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(533)
def test_pending_status_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(534)
def test_ror_response_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(535)
def test_pending_status_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(536)
def test_mc_response_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(537)
def test_pending_status_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(538)
def test_cb_response_pending_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


# --------
@pytest.mark.order(539)
def test_approved_status_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(540)
def test_ror_response_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(541)
def test_approved_status_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(542)
def test_mc_response_approved_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(543)
def test_rejected_status_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(544)
def test_ror_response_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(545)
def test_reported_status_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(546)
def test_ror_response_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(547)
def test_rejected_status_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(548)
def test_mc_response_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(549)
def test_reported_status_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(550)
def test_mc_response_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(551)
def test_rejected_status_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(552)
def test_cb_response_rejected_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(553)
def test_cb_response_reported_status_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(554)
def test_reported_status_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(555)
def test_pending_status_staar_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(556)
def test_approved_status_staar_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(557)
def test_rejected_status_staar_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(558)
def test_reported_status_staar_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(559)
def test_pending_status_college_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(560)
def test_approved_status_college_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(561)
def test_rejected_status_college_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(562)
def test_reported_status_college_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(563)
def test_pending_status_mathworld_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(564)
def test_approved_status_mathworld_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(565)
def test_rejected_status_mathworld_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(566)
def test_reported_status_mathworld_type_ore_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = -1
    response_type: str = "Open Response Exact"
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(567)
def test_pending_status_college_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(568)
def test_approved_status_college_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(569)
def test_rejected_status_college_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(570)
def test_reported_status_college_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(571)
def test_pending_status_mathworld_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(572)
def test_approved_status_mathworld_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(573)
def test_rejected_status_mathworld_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(574)
def test_reported_status_mathworld_type_ror_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(575)
def test_pending_status_staar_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(576)
def test_approved_status_staar_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(577)
def test_rejected_status_staar_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(578)
def test_reported_status_staar_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(579)
def test_pending_status_college_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(580)
def test_approved_status_college_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(581)
def test_rejected_status_college_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(582)
def test_reported_status_college_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(583)
def test_pending_status_mathworld_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(584)
def test_approved_status_mathworld_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(585)
def test_rejected_status_mathworld_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(586)
def test_reported_status_mathworld_type_mc_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(587)
def test_pending_status_staar_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(588)
def test_approved_status_staar_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(589)
def test_rejected_status_staar_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(590)
def test_reported_status_staar_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(591)
def test_pending_status_college_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(592)
def test_approved_status_college_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(593)
def test_rejected_status_college_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(594)
def test_reported_status_college_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(595)
def test_pending_status_mathworld_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(596)
def test_approved_status_mathworld_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(597)
def test_rejected_status_mathworld_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


@pytest.mark.order(598)
def test_reported_status_mathworld_type_cb_response_page_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page number should not be equal or less than to 0"


# ----------------------------------page size = 1 --------------------------------------------


@pytest.mark.order(600)
def test_pending_question_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(602)
def test_approved_questions_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(603)
def test_rejected_question_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(604)
def test_reported_questions_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(605)
def test_staar_type_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_size = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(606)
def test_pending_status_staar_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(607)
def test_college_level_type_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(608)
def test_pending_status_college_level_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(609)
def test_pending_status_mathworld_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(610)
def test_mathworld_type_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(611)
def test_approved_status_college_level_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(612)
def test_college_level_type_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(613)
def test_approved_status_mathworld_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(614)
def test_mathworld_type_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(615)
def test_rejected_status_mathworld_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(616)
def test_mathworld_type_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(617)
def test_rejected_status_college_level_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(618)
def test_college_level_type_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(619)
def test_rejected_status_staar_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(620)
def test_staar_type_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(621)
def test_reported_status_staar_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(622)
def test_staar_type_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(623)
def test_reported_status__type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(624)
def test_college_level_type_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(625)
def test_reported_status_mathworld_type_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_size: int = 1
    create_response: dict = common.create_a_mathworld_question("admin")
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size
    assert questions["data"] != []


@pytest.mark.order(626)
def test_mathworld_type_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_size: int = 1
    create_response: dict = common.create_a_mathworld_question("admin")
    time.sleep(1)
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(628)
def test_ore_response_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(629)
def test_approved_status_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(630)
def test_ore_response_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(631)
def test_rejected_status_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(632)
def test_ore_response_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(633)
def test_reported_status_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(634)
def test_ore_response_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(635)
def test_pending_status_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(636)
def test_ror_response_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(637)
def test_pending_status_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(638)
def test_mc_response_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(639)
def test_pending_status_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(638)
def test_cb_response_pending_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


# --------
@pytest.mark.order(639)
def test_approved_status_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    question_classic: dict = get_db().question_collection.find_one(
        {"response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(640)
def test_ror_response_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    question_classic: dict = get_db().question_collection.find_one(
        {"response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(641)
def test_approved_status_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(642)
def test_mc_response_approved_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(643)
def test_rejected_status_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(644)
def test_ror_response_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(645)
def test_reported_status_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(646)
def test_ror_response_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(647)
def test_rejected_status_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(648)
def test_mc_response_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(649)
def test_reported_status_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(650)
def test_mc_response_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(651)
def test_rejected_status_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(652)
def test_cb_response_rejected_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(653)
def test_cb_response_reported_status_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(654)
def test_reported_status_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(655)
def test_pending_status_staar_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(656)
def test_approved_status_staar_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(657)
def test_rejected_status_staar_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(658)
def test_reported_status_staar_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(659)
def test_pending_status_college_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(660)
def test_approved_status_college_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(661)
def test_rejected_status_college_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(662)
def test_reported_status_college_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(663)
def test_pending_status_mathworld_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(664)
def test_approved_status_mathworld_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(665)
def test_rejected_status_mathworld_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(666)
def test_reported_status_mathworld_type_ore_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    common.create_a_mathworld_question("admin", response_type)
    common.update_question_status("admin", question_status)
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(667)
def test_pending_status_college_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(668)
def test_approved_status_college_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(669)
def test_rejected_status_college_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(670)
def test_reported_status_college_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(671)
def test_pending_status_mathworld_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(672)
def test_approved_status_mathworld_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(673)
def test_rejected_status_mathworld_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(674)
def test_reported_status_mathworld_type_ror_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_size: int = 1
    mathworld_response: dict = common.create_a_mathworld_question(
        "admin", response_type
    )
    mathworld_status = common.update_question_status(
        mathworld_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(675)
def test_pending_status_staar_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(676)
def test_approved_status_staar_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(677)
def test_rejected_status_staar_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(678)
def test_reported_status_staar_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(679)
def test_pending_status_college_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(680)
def test_approved_status_college_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_size


@pytest.mark.order(681)
def test_rejected_status_college_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(682)
def test_reported_status_college_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(683)
def test_pending_status_mathworld_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(684)
def test_approved_status_mathworld_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(685)
def test_rejected_status_mathworld_type_mc_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(687)
def test_pending_status_staar_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(688)
def test_approved_status_staar_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(689)
def test_rejected_status_staar_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.key
@pytest.mark.order(690)
def test_reported_status_staar_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_size


@pytest.mark.order(691)
def test_pending_status_college_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_size: int = 1
    create_response: dict = common.create_a_college_question("admin", response_type)
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(692)
def test_approved_status_college_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(693)
def test_rejected_status_college_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(694)
def test_reported_status_college_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(695)
def test_pending_status_mathworld_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(696)
def test_approved_status_mathworld_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(697)
def test_rejected_status_mathworld_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size


@pytest.mark.order(698)
def test_reported_status_mathworld_type_cb_response_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    print(questions)
    assert questions["count"] == page_size


# --------------------------------------------page 1--------------------------------------------------------------------


@pytest.mark.order(699)
def test_pending_questions_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_num = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(700)
def test_approved_questions_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(701)
def test_rejected_questions_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(702)
def test_reported_questions_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_num={page_num}&page_size=1"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(703)
def test_staar_type_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_size: int = 1
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(704)
def test_pending_status_staar_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(705)
def test_college_level_type_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(706)
def test_pending_status_college_level_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(707)
def test_pending_status_mathworld_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(708)
def test_mathworld_type_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(709)
def test_approved_status_college_level_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&page_num={page_num}&question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(710)
def test_college_level_type_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(711)
def test_approved_status_mathworld_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(712)
def test_mathworld_type_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(713)
def test_rejected_status_mathworld_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 1
    create_response: dict = common.create_a_mathworld_question("admin")
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(714)
def test_mathworld_type_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []


@pytest.mark.order(715)
def test_rejected_status_college_level_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(716)
def test_college_level_type_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(717)
def test_rejected_status_staar_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(718)
def test_staar_type_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Rejected"
    page_size: int = 1
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["page"] == page_size


@pytest.mark.order(719)
def test_reported_status_staar_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(720)
def test_staar_type_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "STAAR"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(721)
def test_reported_status__type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(722)
def test_college_level_type_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "College Level"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(723)
def test_reported_status_mathworld_type_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    mathworld_response: dict = common.create_a_mathworld_question("admin")
    question_id: str = mathworld_response["question_id"]
    mathworld_status = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_type={question_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["count"] == page_size
    assert questions["data"] != []


@pytest.mark.key
@pytest.mark.order(724)
def test_mathworld_type_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_type: str = "Mathworld"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    mathworld_response: dict = common.create_a_mathworld_question("admin")
    question_id = mathworld_response["question_id"]
    mathworld_status = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(725)
def test_pending_status_ore_response(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(726)
def test_ore_response_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(727)
def test_approved_status_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(728)
def test_ore_response_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(729)
def test_rejected_status_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(730)
def test_ore_response_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(731)
def test_reported_status_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(732)
def test_ore_response_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Open Response Exact"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(733)
def test_pending_status_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(734)
def test_ror_response_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(735)
def test_pending_status_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(736)
def test_mc_response_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(737)
def test_pending_status_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(738)
def test_cb_response_pending_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Pending"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


# --------
@pytest.mark.order(739)
def test_approved_status_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    question_classic: dict = get_db().question_collection.find_one(
        {"response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(740)
def test_ror_response_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Approved"
    question_classic: dict = get_db().question_collection.find_one(
        {"response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(741)
def test_approved_status_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(742)
def test_mc_response_approved_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Approved"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(743)
def test_rejected_status_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_size: int = 1
    page_num: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(744)
def test_ror_response_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(745)
def test_reported_status_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(746)
def test_ror_response_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Range Open Response"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(747)
def test_rejected_status_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(748)
def test_mc_response_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(749)
def test_reported_status_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(750)
def test_mc_response_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Multiple Choice"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(751)
def test_rejected_status_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(752)
def test_cb_response_rejected_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Rejected"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(753)
def test_cb_response_reported_status_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?response_type={response_type}&question_status={question_status}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(754)
def test_reported_status_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    response_type: str = "Checkbox"
    question_status: str = "Reported"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(755)
def test_pending_status_staar_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(756)
def test_approved_status_staar_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(757)
def test_rejected_status_staar_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(758)
def test_reported_status_staar_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(759)
def test_pending_status_college_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(760)
def test_approved_status_college_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(761)
def test_rejected_status_college_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(762)
def test_reported_status_college_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(763)
def test_pending_status_mathworld_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(764)
def test_approved_status_mathworld_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(765)
def test_rejected_status_mathworld_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Open Response Exact"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(766)
def test_reported_status_mathworld_type_ore_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    page_num: int = 1
    response_type: str = "Open Response Exact"
    page_size: int = 1
    count: int = 1
    create_response: dict = common.create_a_mathworld_question("staff", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == count


@pytest.mark.order(767)
def test_pending_status_college_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(768)
def test_approved_status_college_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(769)
def test_rejected_status_college_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(770)
def test_reported_status_college_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(771)
def test_pending_status_mathworld_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(772)
def test_approved_status_mathworld_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(773)
def test_rejected_status_mathworld_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(774)
def test_reported_status_mathworld_type_ror_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Range Open Response"
    page_num: int = 1
    page_size: int = 1
    time.sleep(1)
    mathworld_response: dict = common.create_a_mathworld_question(
        "admin", response_type
    )
    question_id = mathworld_response["question_id"]
    mathworld_status = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(775)
def test_pending_status_staar_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(776)
def test_approved_status_staar_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(777)
def test_rejected_status_staar_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(778)
def test_reported_status_staar_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(779)
def test_pending_status_college_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(780)
def test_approved_status_college_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    time.sleep(1)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["count"] == 0


@pytest.mark.order(781)
def test_rejected_status_college_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(782)
def test_reported_status_college_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Multiple Choice"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(783)
def test_pending_status_mathworld_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    page_count: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    # assert questions['count'] == page_count
    assert questions["data"] != []


@pytest.mark.order(784)
def test_approved_status_mathworld_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(785)
def test_rejected_status_mathworld_type_mc_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Multiple Choice"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(787)
def test_pending_status_staar_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["page"] == page_size


@pytest.mark.order(788)
def test_approved_status_staar_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(789)
def test_rejected_status_staar_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.key
@pytest.mark.order(790)
def test_reported_status_staar_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "STAAR"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    create_response: dict = common.create_a_staar_question("admin", response_type)
    question_id: str = create_response["question_id"]
    update_response = common.update_question_status(question_id, question_status)
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(791)
def test_pending_status_college_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(792)
def test_approved_status_college_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(793)
def test_rejected_status_college_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(794)
def test_reported_status_college_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "College Level"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    create_response: dict = common.create_a_college_question("admin", response_type)
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(795)
def test_pending_status_mathworld_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(796)
def test_approved_status_mathworld_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Approved"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    question_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "response_type": response_type}
    )
    sql_classic_id: str = question_classic["_id"]
    patch_payload = json.dumps(
        {
            "status": f"{question_status}",
            "update_note": "Updated status",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=headers, data=patch_payload
    )
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(797)
def test_rejected_status_mathworld_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Rejected"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size


@pytest.mark.order(798)
def test_reported_status_mathworld_type_cb_response_page_1_size_1(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Reported"
    question_type: str = "Mathworld"
    response_type: str = "Checkbox"
    page_num: int = 1
    page_size: int = 1
    create_response: dict = common.create_a_mathworld_question("admin", response_type)
    update_response = common.update_question_status(
        create_response["question_id"], question_status
    )
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&question_type={question_type}&response_type={response_type}&page_num={page_num}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["page"] == page_num
    assert questions["data"] != []
    assert questions["count"] == page_size

    # ----------------------------------- page_size max -----------------------------------


@pytest.mark.order(799)
def test_pending_question_size_2(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = 2
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size
    assert len(questions["data"]) == page_size


@pytest.mark.order(800)
def test_pending_question_size_large(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = 500
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 200
    questions: dict = json.loads(response.text)
    assert questions["count"] == page_size
    assert len(questions["data"]) == page_size


@pytest.mark.order(801)
def test_pending_question_size_zero(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = 0
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page size should not be equal or less than to 0"


@pytest.mark.order(802)
def test_pending_question_size_negative(get_admin_token):
    req: Requester = Requester()
    headers: dict = req.create_basic_headers(token=get_admin_token)
    question_status: str = "Pending"
    page_size: int = -1
    url: str = f"{req.base_url}/v1/questions?question_status={question_status}&page_size={page_size}"
    response = requests.request("GET", url, headers=headers)
    assert response.status_code == 400
    questions: dict = json.loads(response.text)
    assert questions["detail"] == "Page size should not be equal or less than to 0"
