import json
import os
import pdb
import sys

import requests
from pytest import fixture

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger
import random

import lib.common as common
import lib.generate_token as generate_token
import pytest
from assertpy import assert_that
from bson import ObjectId
from lib.common import get_current_yyyy_mm, get_random_payload_data, get_random_question
from lib.mw_db import get_db
from lib.requester import Requester

from tests.payloads.valid_question_payloads import get_valid_successful_staar_payload


@fixture(scope="module")
def get_staff_token():
    token = generate_token.generate_token(
        email="staffABC@gmail.com", password="Staff123!"
    )
    yield token
    print("\n\n---- Tear Down Test ----\n")


# ---------------------------------------
# Test Cases: STAAR Status Update as Admin
# Author: Yshmael Ammonraheem
# Status: Approved, Pending, Rejected, Reported
# Question Type: STAAR, College Level, Mathworld
# ----------------------------------------
# Pending -> Approved
# Pending -> Rejected
# Pending -> Reported
# ----------------------------------------
@pytest.mark.order(1)
def test_status_pending_to_approved(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    update_status: str = "Approved"
    question_type: str = "STAAR"
    header: dict = req.create_basic_headers(token=get_staff_token)
    create_url = f"{req.base_url}/v1/questions/create"
    question1 = common.get_random_question()
    question2 = common.get_random_question()

    payload = get_valid_successful_staar_payload()

    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    classic_response = requests.request(
        "POST", create_url, headers=header, json=payload
    )
    json_classic_response = json.loads(classic_response.text)
    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(json_classic_response["question_id"])}
    )
    classic_status: str = questions_returned["question_status"]
    assert_that(classic_status).is_equal_to("Pending")
    patch_url: str = f"{req.base_url}/v1/questions/update/question_status/{json_classic_response['question_id']}"
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to("Approved")
    assert_that(json_patch_response["data"]["question_type"]).is_equal_to(question_type)


# ---------------------------------------------------------------------------------


@pytest.mark.order(2)
def test_status_pending_to_reported(get_staff_token):
    req = Requester()
    create_url = f"{req.base_url}/v1/questions/create"
    random_data: dict = common.get_random_payload_data()
    update_status: str = "Reported"
    question_type: str = "STAAR"
    header: dict = req.create_basic_headers(token=get_staff_token)

    payload = get_valid_successful_staar_payload()

    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    classic_response = requests.request(
        "POST", create_url, headers=header, json=payload
    )
    json_classic_response = json.loads(classic_response.text)
    questions_returned: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": "Pending"}
    )
    classic_status: str = questions_returned["question_status"]
    assert_that(classic_status).is_equal_to("Pending")
    patch_url: str = f"{req.base_url}/v1/questions/update/question_status/{json_classic_response['question_id']}"
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to("Reported")
    assert_that(json_patch_response["data"]["question_type"]).is_equal_to(question_type)


@pytest.mark.order(3)
def test_status_pending_to_rejected_by_payload(get_staff_token):
    req = Requester()
    create_url = f"{req.base_url}/v1/questions/create"
    random_data: dict = common.get_random_payload_data()
    update_status: str = "Rejected"
    question_type: str = "STAAR"
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    questions_returned: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": "Rejected"}
    )
    classic_id: str = questions_returned["_id"]
    classic_status: str = questions_returned["question_status"]
    assert_that(classic_status).is_equal_to("Rejected")
    patch_url: str = f"{req.base_url}/v1/questions/update/question_status/{classic_id}"
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to("Rejected")
    assert_that(json_patch_response["data"]["question_type"]).is_equal_to(question_type)


# ---------------------------------------------------------------------------------
# Approved -> Pending
# Rejected -> Pending
# Reported -> Pending
# Pending -> Pending
# ---------------------------------------------------------------------------------


@pytest.mark.order(4)
def test_status_approved_to_pending(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Approved"
    update_status: str = "Pending"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(5)
def test_status_rejected_to_pending(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Rejected"
    update_status: str = "Pending"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(6)
def test_status_reported_to_pending(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Reported"
    update_status: str = "Pending"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


# ---------------------------------------------------------------------------------
# Approved -> Approved
# Rejected -> Approved
# Reported -> Approved
# Pending -> Approved
# ---------------------------------------------------------------------------------


@pytest.mark.order(7)
def test_status_approved_to_approved(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Approved"
    update_status: str = "Approved"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(8)
def test_status_rejected_to_approved(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Rejected"
    update_status: str = "Approved"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    updated_status: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(updated_status)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


# ---------------------------------------------------------------------------------
# Approved -> Reported
# Rejected -> Reported
# Reported -> Reported
# Pending -> Reported
# ---------------------------------------------------------------------------------


@pytest.mark.order(9)
def test_status_approved_to_reported(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Approved"
    update_status: str = "Reported"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    updated_status: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(updated_status).is_equal_to("Reported")
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(10)
def test_status_rejected_to_reported(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Rejected"
    update_status: str = "Reported"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(11)
def test_status_reported_to_approved(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Pending"
    update_status: str = "Approved"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(12)
def test_status_pending_to_pending(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Pending"
    update_status: str = "Approved"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


# ---------------------------------------------------------------------------------
# Approved -> Rejected
# Rejected -> Rejected
# Reported -> Rejected
# Pending -> Rejected
# ---------------------------------------------------------------------------------


@pytest.mark.order(13)
def test_status_approved_to_rejected(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Approved"
    update_status: str = "Rejected"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(14)
def test_status_rejected_to_rejected(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Rejected"
    update_status: str = "Rejected"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(15)
def test_status_reported_to_rejected(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Reported"
    update_status: str = "Rejected"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )


@pytest.mark.order(16)
def test_status_pending_to_rejected(get_staff_token):
    req = Requester()
    random_data: dict = common.get_random_payload_data()
    current_status: str = "Pending"
    update_status: str = "Rejected"
    question_type: str = "STAAR"
    approved_classic: dict = get_db().question_collection.find_one(
        {"question_type": question_type, "question_status": current_status}
    )
    sql_classic_id: str = approved_classic["_id"]
    header: dict = req.create_basic_headers(token=get_staff_token)
    patch_payload = json.dumps(
        {
            "status": f"{update_status}",
            "update_note": f"{random_data['random_sentence']}",
        }
    )

    patch_url: str = (
        f"{req.base_url}/v1/questions/update/question_status/{sql_classic_id}"
    )
    patch_response = requests.request(
        "PATCH", patch_url, headers=header, data=patch_payload
    )
    json_patch_response = json.loads(patch_response.text)

    questions_returned: dict = get_db().question_collection.find_one(
        {"_id": ObjectId(sql_classic_id)}
    )
    status_updated: str = questions_returned["question_status"]
    assert_that(patch_response.status_code).is_equal_to(200)
    assert_that(update_status).is_equal_to(status_updated)
    assert_that(json_patch_response["data"]["question_status"]).is_equal_to(
        update_status
    )
