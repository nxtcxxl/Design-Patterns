from datetime import datetime

from course import Course


class Enrollment:
    """
    ...
    Attributes
    ----------
    received_marks: dict
    course[]
    Methods
    -------
    get_average_to_date(date: datetime)
    get_final_mark()

    """

    def __init__(self, course: Course):
        self.course = course
        self.received_marks = dict()

    def get_average_to_date(self, date_to: datetime):
        grades = []
        for date, grade in self.received_marks.items():
            if date_to <= date:
                grades.append(grade)
        return sum(grades)/len(grades)

    def get_final_mark(self):
        return sum(self.received_marks.values())/len(self.received_marks)
