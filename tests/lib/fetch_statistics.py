def get_stat_by_question(data: list, question_type: str) -> dict:
    for i in data:
        if i['question_type'] == question_type:
            return i