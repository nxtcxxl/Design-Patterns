"""
class Course
"""
from dataclasses import dataclass
from datetime import datetime

@dataclass
class CourseInfo:
    name: str
    date: datetime
    fee: float
    seminars_number: int


class Course:
    """
    ...
    Attributes
    ----------
    course_info: CourseInfo
    course_id: int
    course_limit: int
    student_id_list: []
    ----------
    Methods
    -------
    add_student()
    remove_student()

    """

    course_limit = 10

    def __init__(self, course_id: int, course_info: CourseInfo) -> None:
        self.course_id = course_id
        self.course_info = course_info
        self.student_id_list = []

    def __str__(self):
        print(f"""Course {self.course_info.name}
        Program start: {self.course_info.date}
        Tuition: {self.course_info.fee}
        Seminars: {self.course_info.seminars_number}""")

    def add_student(self, student_id: int) -> None:
        if isinstance(student_id, int) and student_id > 0:
            self.student_id_list.append(student_id)
            print(f"Student's id {student_id} has been added.")
        else:
            raise ValueError('student id has to be int > 0')

    def remove_student(self, student_id: int) -> None:
        idx = -1
        for i, st_id in enumerate(self.student_id_list):
            if student_id == st_id:
                idx = i
                print(f"Student with ID {student_id} has been removed.")
                break
        if idx < -1:
            del self.student_id_list[idx]
            print("No ID")
