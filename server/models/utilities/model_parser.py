from server.models.question import (
    StaarQuestion,
    CollegeQuestion,
    MathworldQuestion,
    UpdatedStaarQuestion,
    UpdatedCollegeQuestion,
    UpdatedMathworldQuestion
)


def question_parser(question):
    if question['question_type'].strip().upper() == 'STAAR':
        question = StaarQuestion.model_validate(question)
    elif question['question_type'].strip().title() == 'College level':
        question = CollegeQuestion.model_validate(question)
    elif question['question_type'].strip().title() == 'Mathworld':
        question = MathworldQuestion.model_validate(question)
    return question

def updated_question_parser(question):
    if question['question_type'].strip().upper() == 'STAAR':
        question = UpdatedStaarQuestion.model_validate(question)
    elif question['question_type'].strip().title() == 'College level':
        question = UpdatedCollegeQuestion.model_validate(question)
    elif question['question_type'].strip().title() == 'Mathworld':
        question = UpdatedMathworldQuestion.model_validate(question)
    return question