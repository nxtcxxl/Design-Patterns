from datetime import datetime

from staff import PersonalInfo
from staff import Student
from staff import Professor
from course import Course
from course import CourseInfo

date = datetime.today()

student_info = PersonalInfo("Denis", "Smith", "1710 H St NW ", "denissmith123@lab1.com", 12341234567)
student_1 = Student(student_info, 7534866, 1)
student_1.__str__()

course_info = CourseInfo("High Math", datetime(2021, 9, 1), 0, 20)
course1 = Course(1, course_info)
course1.__str__()

professor_info = PersonalInfo("Jeniffer", "Brown", "726 Jackson Pl NW", "professor.brown@lab1.com", 234345651)
professor_1 = Professor(4000, professor_info)
professor_1.__str__()

print("\nEnroll student")
student_1.enroll(course1)
student_1.taken_courses()
print("\nUnroll student")
student_1.unroll(course1)
student_1.taken_courses()

print("\n")
course1.add_student(7534866)
student_1.can_enroll(course1)
course1.remove_student(7534866)