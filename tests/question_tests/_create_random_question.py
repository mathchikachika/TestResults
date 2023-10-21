from pytest import fixture
import pdb, requests
import os, sys, json
from faker import Faker
import random
import requests

CURRENT_DIR = os.getcwd()
PARENT_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(CURRENT_DIR)
sys.path.append(PARENT_DIR)

import logging as logger, pytest
import tests.lib.common as common

faker = Faker()


def create_token():
    url = "http://localhost:8000/staff/login"

    payload = json.dumps({
      "email": "adminXYZ@gmail.com",
      "password": "Admin123!"
    })
    headers = {
      'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response_dict = json.loads(response.text)
    return response_dict['access_token']

    
def set_random_staar_fields():
    random_month = str (random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']))
    random_date = "2024-" + str(random_month) 
    random_response_type: str = random.choice(['Open Response Exact', 'Range Open Response', 'Multiple Choice', 'Checkbox'])
    random_question_type: str = random.choice(['STAAR', 'College Level', 'MathWord'])
    random_grade_level: int = random.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    random_letter: str = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    random_unit: str = random.choice(['pounds', 'kilograms', 'meters', 'centimeters', 'inches', 'feet', 'yards', 'miles', 'grams', 'liters'])
    url = "http://localhost:8000/question/STAAR/create"

    payload = {'data': '{"question_type": "' + random_question_type + '", "grade_level": 3, "release_date": "' + random_date + '", "category": "math","keywords": ["math"], "student_expectations": ["good"],"response_type": "Reported Open Response","question_content": "this is a test","question_img": "","options": [{"letter": "' + random_letter + '","content": "this is a test","image": "","unit": "'+ random_unit + '","is_answer": true},{"letter": "' + random_letter + '","content": "option b","image": "","unit": "' + random_unit + '","is_answer": false}]}'} 

    files=[
      ('question_image',('image_01.jpg',open('C:\\QA\\Dev\\projects\\_GitLab\\mathworld\\Merging\\Admin-BackEndDev\\tests\\images\\image_01.jpg','rb'),'image/jpeg'))
    ]
    token = create_token()
    headers = {
      'Authorization': f'Bearer {token}'
    }        
    response = requests.request("POST", url, headers=headers, data=payload, files=files)


def set_random_mathworld_fields():
    random_month = str (random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']))
    random_date = "2024-" + str(random_month) 
    random_response_type: str =  'Range Open'  # random.choice(['Open Response Exact', 'Range Open Response', 'Multiple Choice', 'Checkbox'])
    random_question_type: str = random.choice(['STAAR', 'College Level', 'MathWord'])
    random_grade_level: int = random.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    random_letter: str = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    random_unit: str = random.choice(['pounds', 'kilograms', 'meters', 'centimeters', 'inches', 'feet', 'yards', 'miles', 'grams', 'liters'])
    random_topic: str = random.choice(['topic 1', 'topic 2', 'topic 3', 'topic 4', 'topic 5', 'topic 6', 'topic 7', 'topic 8', 'topic 9', 'topic 10'])
    random_subject: str = random.choice(['Math', 'Science', 'Social Studies', 'English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Russian'])
    random_category: str = random.choice(['category 1', 'category 2', 'category 3', 'category 4', 'category 5', 'category 6', 'category 7', 'category 8', 'category 9', 'category 10'])
    random_difficulty: str = random.choice(['Easy','Average','Hard','Advance'])

    url = "http://localhost:8000/question/mathworld/create"

    token = create_token()
    payload = {'data': '{"question_type": "MathWorld","grade_level": 3,"teks_code": "202402","subject": "' + random_unit + '","topic": "' + random_topic + '","category": "' + random_category + '","keywords": ["string"],"student_expectations": ["string"],"difficulty": "' + random_difficulty + '","points": 2,"response_type": "Open Response Exact","question_content": "string","question_img": "","options": [{"letter": "' + random_letter + '","content": "string","image": "","unit": "' + random_unit +'","is_answer": true}]}'}
    files=[]
    headers = {
      'Authorization': f'Bearer {token}'
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text)

    
def set_random_college_level_fields():
    random_month = str (random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']))
    random_date = "2024-" + str(random_month) 
    random_response_type: str = random.choice(['Open Response Exact', 'Range Open Response', 'Multiple Choice', 'Checkbox'])
    random_question_type: str = random.choice(['STAAR', 'College Level', 'MathWord'])
    random_grade_level: int = random.choice([3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    random_letter: str = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'])
    random_unit: str = random.choice(['pounds', 'kilograms', 'meters', 'centimeters', 'inches', 'feet', 'yards', 'miles', 'grams', 'liters'])
    random_topic: str = random.choice(['topic 1', 'topic 2', 'topic 3', 'topic 4', 'topic 5', 'topic 6', 'topic 7', 'topic 8', 'topic 9', 'topic 10'])
    random_subject: str = random.choice(['Math', 'Science', 'Social Studies', 'English', 'Spanish', 'French', 'German', 'Chinese', 'Japanese', 'Russian'])
    random_category: str = random.choice(['category 1', 'category 2', 'category 3', 'category 4', 'category 5', 'category 6', 'category 7', 'category 8', 'category 9', 'category 10'])
    random_difficulty: str = random.choice(['Easy','Average','Hard','Advance'])
    random_classification: str = random.choice(['SAT','TSI','ACT'])
    random_question: str = common.get_random_question()

    url = "http://localhost:8000/question/college/create"

    payload = {'data': '{"question_type": "College Level","classification": "' + random_classification + '","test_code": "123456","keywords": ["2"],"response_type": "Checkbox",  "question_content": "' + random_question + '","question_img": "","options": [{"letter": "' + random_letter + '","content": "string","image": "","unit": "' + random_unit + '","is_answer": true}]}'}
    files=[]
    
    token = create_token()

    headers = {
      'Authorization': f'Bearer {token}'
      }

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)


counter : int = 250

for i in range(counter):
  set_random_mathworld_fields()
  print(i)
