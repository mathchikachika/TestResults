from pytest import fixture
import pdb, requests
import os, sys, json
from assertpy import assert_that
import random

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import lib.common as common
import lib.generate_token as generate_token
from lib.requester import Requester

role_list: list = ['admin', 'staff', 'teacher']


@fixture(scope="module")
def get_admin_token():
    token = generate_token.generate_token(email="adminXYZ@gmail.com", password="Admin123!")
    yield token
    print("\n\n---- Tear Down Test ----\n")

    
@pytest.mark.tc_001
def test_update_all_details(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')
    
    # PARSE MEMBER DATA
    uuid: str = member['staff']['uuid']
    first_name: str = member['staff']['first_name']
    middle_name: str = member['staff']['middle_name']
    last_name: str = member['staff']['last_name']
    email: str = member['staff'] ['email']
    old_role: str = member['staff']['user_role']
    school: str = member['staff']['school']
    updated_by: str = member['staff']['updated_by']
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_role]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{uuid}'
    update_response: requests.models.Response =  \
        requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{uuid}'
    get_response: requests.models.Response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(email)
    assert_that(json_response['user']['first_name']).is_not_equal_to(first_name)
    assert_that(json_response['user']['middle_name']).is_not_equal_to(middle_name)
    assert_that(json_response['user']['last_name']).is_not_equal_to(last_name)
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_role) 
    assert_that(json_response['user']['uuid']).is_equal_to(uuid)
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{uuid}'
    delete_response: requests.models.Response = requests.request( "DELETE", url=delete_url, headers=header)    
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_002
def test_update_first_name_only(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')
    
    # PARSE MEMBER DATA
    uuid: str = member['staff']['uuid']
    first_name: str = member['staff']['first_name']
    middle_name: str = member['staff']['middle_name']
    last_name: str = member['staff']['last_name']
    email: str = member['staff'] ['email']
    role: str = member['staff']['user_role']
    school: str = member['staff']['school']
    updated_by: str = member['staff']['updated_by']
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{middle_name}",
            "last_name": f"{last_name}",
            "role": f"{role}",
            "email": f"{email}",
            "school": f"{school}",
            "updated_by": f"{updated_by}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{uuid}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('email is invalid')

@pytest.mark.tc_003
def test_update_middle_name_only(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')
    
    # PARSE MEMBER DATA
    uuid: str = member['staff']['uuid']
    first_name: str = member['staff']['first_name']
    middle_name: str = member['staff']['middle_name']
    last_name: str = member['staff']['last_name']
    email: str = member['staff'] ['email']
    user_role: str = member['staff']['user_role']
    school: str = member['staff']['school']
    updated_by: str = member['staff']['updated_by']
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{first_name}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{last_name}",
            "role": f"{user_role}",
            "email": f"{email}",
            "school": f"{school}",
            "updated_by": f"{updated_by}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{uuid}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('email is invalid')

@pytest.mark.tc_004
def test_update_last_name_only(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')
    
    # PARSE MEMBER DATA
    uuid: str = member['staff']['uuid']
    first_name: str = member['staff']['first_name']
    middle_name: str = member['staff']['middle_name']
    last_name: str = member['staff']['last_name']
    email: str = member['staff'] ['email']
    user_role: str = member['staff']['user_role']
    school: str = member['staff']['school']
    updated_by: str = member['staff']['updated_by']
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{first_name}",
            "middle_name": f"{middle_name}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{user_role}",
            "email": f"{email}",
            "school": f"{school}",
            "updated_by": f"{updated_by}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{uuid}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('email is invalid')

@pytest.mark.tc_005
def test_update_email_only(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{old_payload['first_name']}",
            "middle_name": f"{old_payload['middle_name']}",
            "last_name": f"{old_payload['last_name']}",
            "role": f"{old_payload['role']}",
            "email": f"{email_random}",
            "school": f"{old_payload['school']}",
            "updated_by": f"{old_payload['first_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(200)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    updated_response = requests.request("GET", url=get_url, headers=header)
    json_updated_response: dict = json.loads(updated_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_updated_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_updated_response['user']['first_name']).is_equal_to(old_payload['first_name'])
    assert_that(json_updated_response['user']['middle_name']).is_equal_to(old_payload['middle_name'])
    assert_that(json_updated_response['user']['last_name']).is_equal_to(old_payload['last_name'])
    assert_that(json_updated_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_updated_response['user']['user_role']).is_equal_to(old_payload['role']) 
    assert_that(json_updated_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)

@pytest.mark.tc_006
def test_update_role_only(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{old_payload['first_name']}",
            "middle_name": f"{old_payload['middle_name']}",
            "last_name": f"{old_payload['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{old_payload['email']}",
            "school": f"{old_payload['school']}",
            "updated_by": f"{old_payload['updated_by']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('email is invalid')

@pytest.mark.tc_007
def test_update_school_only(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    old_payload['email'] = common.chop_string(old_payload['email'])
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{old_payload['first_name']}",
            "middle_name": f"{old_payload['middle_name']}",
            "last_name": f"{old_payload['last_name']}",
            "role": f"{old_payload['role']}",
            "email": f"{old_payload['email']}",
            "school": f"{random_data['first_name']} State University",
            "updated_by": f"{old_payload['updated_by']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('email is invalid')

@pytest.mark.tc_008
def test_update_updated_by_only(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{old_payload['first_name']}",
            "middle_name": f"{old_payload['middle_name']}",
            "last_name": f"{old_payload['last_name']}",
            "role": f"{old_payload['role']}",
            "email": f"{old_payload['email']}",
            "school": f"{old_payload['school']}",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('email is invalid')


@pytest.mark.tc_009
def test_update_missing_first_name(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "user_role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['user_role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": "",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['last_name']} State University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('first_name field should not be empty')

@pytest.mark.tc_010
def test_update_missing_middle_name(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": "",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['last_name']} State University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(200)
    assert_that(json_response['Successfully updated']).is_true

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    updated_response = requests.request("GET", url=get_url, headers=header)
    json_updated_response: dict = json.loads(updated_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA    
    assert_that(json_updated_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_updated_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_updated_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_updated_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_updated_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_updated_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)


@pytest.mark.tc_010
def test_update_missing_last_name(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": "X",
            "last_name": "",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['last_name']} State University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to('last_name field should not be empty')


@pytest.mark.tc_011
def test_update_missing_role(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": "X",
            "last_name": f"{random_data['last_name']}",
            "role": "",
            "email": f"{email_random}",
            "school": f"{random_data['last_name']} State University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("value is not a valid enumeration member; permitted: 'staff', 'admin', 'subscriber'")

@pytest.mark.tc_012
def test_update_invalid_role(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": "X",
            "last_name": f"{random_data['last_name']}",
            "role": "Janitor",
            "email": f"{email_random}",
            "school": f"{random_data['last_name']} State University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("value is not a valid enumeration member; permitted: 'staff', 'admin', 'subscriber'")

@pytest.mark.tc_013
def test_update_missing_email(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": "X",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": "",
            "school": f"{random_data['last_name']} State University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("email field should not be empty")

@pytest.mark.tc_014
def test_update_missing_school(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": "X",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": "",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(200)
    assert_that(json_response['Successfully updated']).is_true()

@pytest.mark.tc_015
def test_update_missing_updated_by(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }
    
    # CREATE UPDATE PAYLOAD    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    role_list: list = ['admin', 'staff', 'teacher']
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": "X",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['last_name']} State University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(200)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    updated_response = requests.request("GET", url=get_url, headers=header)
    json_updated_response: dict = json.loads(updated_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA    
    assert_that(json_updated_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_updated_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_updated_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_updated_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_updated_response['user']['user_role']).is_not_equal_to(old_payload['role'])     
    assert_that(json_updated_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)

@pytest.mark.tc_016
def test_update_same_first_name(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{old_payload['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{random_data['mw_role']}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)
    new_role = [ role for role in role_list if role != old_payload['role']]

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(new_role) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_017
def test_update_same_middle_name(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{old_payload['middle_name']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{random_data['mw_role']}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)
    new_role = [ role for role in role_list if role != old_payload['role']]

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(new_role) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_018
def test_update_same_last_name(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{old_payload['last_name']}",
            "role": f"{random_data['mw_role']}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)
    new_role = [ role for role in role_list if role != old_payload['role']]

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(new_role) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_019
def test_update_same_role(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{old_payload['role']}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)
    new_role = [ role for role in role_list if role != old_payload['role']]

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_020
def test_update_same_email(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{old_payload['email']}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(update_response.status_code).is_equal_to(422)
    assert_that(json_response['detail'][0]['msg']).is_equal_to("email is invalid")
    
@pytest.mark.tc_021
def test_update_same_school(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')
    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{old_payload['school']}",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_022
def test_update_same_updated_by(get_admin_token):
    req = Requester()    

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{old_payload['updated_by']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)


@pytest.mark.tc_023
def test_update_max_first_name(get_admin_token):
    req = Requester()    
    max_number: int = 50

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time: str = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(max_number)

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{max_char_width}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
        requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response:  requests.models.Response = \
        requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)


@pytest.mark.tc_024
def test_update_max_middle_name(get_admin_token):
    req = Requester()    
    max_number: int = 50

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(50)

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{max_char_width}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
        requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.models.Response = \
        requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_025
def test_update_max_last_name(get_admin_token):
    req = Requester()    
    max_number: int = 50

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time: str = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(50)

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{max_char_width}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
          requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.models.Response = \
        requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response: requests.models.Response = \
          requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)


@pytest.mark.tc_026
def test_update_max_email(get_admin_token):
    req = Requester()    
    max_number: int = 15

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    # CREATE RANDOM PAYLOAD
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(max_number) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{max_char_width}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_027
def test_update_min_email(get_admin_token):
    req = Requester()    
    min_number: int = 10

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    min_char_width: str = common.create_random_string_width(50) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random}",
            "role": f"{new_role[0]}",
            "email": f"{min_char_width}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
          requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.Response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response: requests.models.Response = \
          requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_028
def test_update_max_school(get_admin_token):
    req = Requester()    
    max_number: int = 50

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(50) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{max_char_width} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
        requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.Response = \
          requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_029
def test_update_max_updated_by(get_admin_token):
    req = Requester()    
    max_number: int = 50

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(50) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{max_char_width}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.Response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)


@pytest.mark.tc_030
def test_update_min_first_name(get_admin_token):
    req = Requester()    
    min_number: int = 10

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    min_char_width: str = common.create_random_string_width(50) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{min_char_width}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
        requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.Response = \
        requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response: requests.models.Response = \
        requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_030
def test_update_min_middle_name(get_admin_token):
    req = Requester()    
    min_number: int = 1

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    min_char_width: str = common.create_random_string_width(50) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{min_char_width}",
            "last_name": f"{random}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
        requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.Response = \
        requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response: requests.models.Response = \
        requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_031
def test_update_min_last_name(get_admin_token):
    req = Requester()    
    min_number: int = 1

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    min_char_width: str = common.create_random_string_width(50) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{min_char_width}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
        requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.Response = \
          requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response: requests.models.Response = \
        requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_032
def test_update_min_school(get_admin_token):
    req = Requester()    
    min_number: int = 1

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data: dict = json.loads(common.create_fake_payload())
    email_random: str = common.random_email()
    current_date_time = common.current_date_time()
    new_role: list = [ role for role in role_list if role != old_payload['role']]
    min_char_width: str = common.create_random_string_width(50) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{min_char_width}",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url: str = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response: requests.models.Response = \
        requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.Response = \
        requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response: requests.models.Response = \
        requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_033
def test_update_min_updated_by(get_admin_token):
    req = Requester()    
    min_number: int = 1

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]
    min_char_width: str = common.create_random_string_width(50) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{min_char_width}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url: str = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response: requests.Response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)

@pytest.mark.tc_034
def test_update_max_plus_first_name(get_admin_token):
    req = Requester()    
    max_number: int = 25

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(max_number)

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{max_char_width}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{max_char_width} University",
            "updated_by": f"{random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_equal_to(True)

@pytest.mark.tc_035
def test_update_max_plus_middle_name(get_admin_token):
    req = Requester()    
    max_number: int = 25

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(max_number)

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{max_char_width}",
            "last_name": f"{random_data['last_name']}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_equal_to(True)

    
@pytest.mark.tc_036
def test_update_max_plus_last_name(get_admin_token):
    req = Requester()    
    max_number: int = 25

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(max_number)

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{max_char_width}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

    # RETRIEVE UPDATED STAFF MEMBER
    get_url = f'{req.base_url}/staff/specific/{old_payload["uuid"]}'
    get_response = requests.request("GET", url=get_url, headers=header)
    json_response: dict = json.loads(get_response.text)

    # VERIFY UPDATE != INITIALLY REGISTERED DATA
    assert_that(json_response['user']['email']).is_not_equal_to(old_payload['email'])
    assert_that(json_response['user']['first_name']).is_not_equal_to(old_payload['first_name'])
    assert_that(json_response['user']['middle_name']).is_not_equal_to(old_payload['middle_name'])
    assert_that(json_response['user']['last_name']).is_not_equal_to(old_payload['last_name'])
    assert_that(json_response['user']['user_role']).is_not_equal_to(old_payload['role']) 
    assert_that(json_response['user']['uuid']).is_equal_to(old_payload['uuid'])
 
    # DELETE STAFF MEMBER
    delete_url: str = f'{req.base_url}/staff/delete/{old_payload["uuid"]}'
    delete_response = requests.request("DELETE", url=delete_url, headers=header)
    json_response: dict = json.loads(delete_response.text)
    assert_that(json_response['message']).is_equal_to('Successfully deleted')

@pytest.mark.tc_037
def test_update_max_plus_email(get_admin_token):
    req = Requester()    
    max_number: int = 15

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['updated_by'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(max_number) + '@gmail.com'

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random}",
            "role": f"{new_role[0]}",
            "email": f"{max_char_width}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{random_data['first_name']} {random_data['last_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()

@pytest.mark.tc_038
def test_update_max_plus_school(get_admin_token):
    req = Requester()    
    max_number: int = 35

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['first_name'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(max_number)

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{max_char_width}",
            "updated_by": f"{random_data['first_name']}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()


@pytest.mark.tc_039
def test_update_max_plus_updated_by(get_admin_token):
    req = Requester()    
    max_number: int = 50

    # REGISTER STAFF MEMBER
    header: dict = req.create_basic_headers(token=get_admin_token)
    member:dict = common.register_staff_member()
    assert_that(member['detail']).is_equal_to('Successfully Added Staff')    

    # PARSE MEMBER DATA
    old_payload: dict = {
        "uuid": member['staff']['uuid'],
        "first_name": member['staff']['first_name'],
        "middle_name": member['staff']['middle_name'],
        "last_name": member['staff']['last_name'],
        "role": member['staff']['user_role'],
        "email": member['staff']['email'],
        "school": member['staff']['school'],
        "updated_by": member['staff']['first_name'],
    }       
    
    random_data = json.loads(common.create_fake_payload())
    email_random = common.random_email()
    current_date_time = common.current_date_time()
    new_role = [ role for role in role_list if role != old_payload['role']]
    max_char_width: str = common.create_random_string_width(max_number)

    # CREATE UPDATE PAYLOAD 
    update_payload: dict = {
            "first_name": f"{random_data['first_name']}",
            "middle_name": f"{random_data['middle_initial']}",
            "last_name": f"{random}",
            "role": f"{new_role[0]}",
            "email": f"{email_random}",
            "school": f"{random_data['first_name']} University",
            "updated_by": f"{max_char_width}",
            "updated_at": f"{current_date_time}"
            }
    
    # UPDATE STAFF MEMBER
    update_url = f'{req.base_url}/staff/update_staff_details/{old_payload["uuid"]}'
    update_response = requests.request("PUT", url=update_url, headers=header, data=json.dumps(update_payload))
    json_response: dict = json.loads(update_response.text)
    assert_that(json_response['Successfully updated']).is_true()
    