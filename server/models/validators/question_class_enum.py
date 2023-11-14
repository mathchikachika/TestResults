from enum import Enum

class TypeEnum(str, Enum):
    staar = 'STAAR'
    college = 'College Level'
    mathworld = 'Mathworld'


class ResponseEnum(str, Enum):
    open_response_exact = 'Open Response Exact'
    open_response_range = 'Range Open Response'
    multiple_choice = 'Multiple Choice'
    checkbox = 'Checkbox'


class StatusEnum(str, Enum):
    pending = 'Pending'
    approved = 'Approved'
    rejected = 'Rejected'
    reported = "Reported"


class ClassificationEnum(str, Enum):
    sat = 'SAT'
    tsi = 'TSI'
    act = 'ACT'


class DifficultyEnum(str, Enum):
    easy = "Easy"
    average = "Average"
    hard = "Hard"
    advance = "Advance"