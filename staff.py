from dataclasses import dataclass

from course import Course
from enrollment import Enrollment


@dataclass
class PersonalInfo:
    first_name: str
    last_name: str
    address: str
    email: str
    phone_number: int


class Student:
    """
       ...
        student_info: PersonalInfo
        student_id: int
        enrollments: []

        Methods
        ----------
        can_enroll(course: Course): static
        taken_courses()
        enroll()
        unroll()

    """

    def __init__(self, student_info: PersonalInfo, student_id: int, student_number: int) -> None:
        self.student_info = student_info
        self.student_number = student_number
        self.student_id = student_id
        self.enrollments = []

    def __str__(self):
        print("""Student {} {} has {} id.
        \tPhone number: {}"
        \tEmail: {}
        \tAddress: {}""".format(self.student_info.first_name, self.student_info.last_name,
                                self.student_id, self.student_info.phone_number,
                                self.student_info.email, self.student_info.address))

    @staticmethod
    def can_enroll(course: Course):
        if len(course.student_id_list) > course.course_limit:
            print("You can`t enroll to this course because it is full")
        else:
            print("You can enroll in this course if you want")

    def taken_courses(self):
        count = len(self.enrollments)
        if count == 1:
            print("1 course was taken")
        elif count > 1:
            print(f"{count} courses were taken")
        else:
            print("No course taken")

    def enroll(self, course_id: Course):
        course_id.add_student(student_id=self.student_id)
        enrollment = Enrollment(course = course_id)
        self.enrollments.append(enrollment)
        print("Student with ID{} has enrolled to {}".format(self.student_id, course_id.course_info.name))

    def unroll(self, course_id: Course) -> None:
        idx = -1
        for i, item in enumerate(self.enrollments):
            if item.course == course_id:
                item.course.remove_student(student_id = self.student_id)
                idx = i
                break
        del self.enrollments[idx]
        print("Student with ID{} has unrolled to {}".format(self.student_id, course_id.course_info.name))

class Professor:
    """
    ...
    Attributes
    ----------
    professor_info: PersonalInfo
    salary: float

    """

    def __init__(self, salary: float, professor_info: PersonalInfo) -> None:
        self.salary = salary
        self.professor_info = professor_info

    def __str__(self):
        print("""Professor {} {}
        \tPhone number: {}"
        \tEmail: {}
        \tSalary: {}
        \tAddress: {}""".format(self.professor_info.first_name, self.professor_info.last_name,
                                self.professor_info.phone_number, self.professor_info.email,
                                self.salary, self.professor_info.address))