from course import Course
from student import Student

math = Course("Algebra I")
language = Course("Spanish I")
science = Course("Earth Science")
history = Course("U.S. History I")
phys_ed = Course("Physical Education I")
drivers = Course("Drivers Education")
Ied = Course("intro to engineering design")

test_student = Student("Jill", "Sample")
test_student.add_course(math)
test_student.add_course(language)
test_student.add_course(science)
test_student.add_course(history)

test_student2 = Student("Bill", "Sample")
test_student2.add_course(math)
test_student2.add_course(phys_ed)
test_student2.add_course(science)
test_student2.add_course(history)

test_student3 = Student("joe", "Sample")
test_student3.add_course(language)
test_student3.add_course(science)
test_student3.add_course(math)
test_student3.add_course(history)


student_list = test_student, test_student2, test_student3

print(Student)

# iterate over each of the students in the list and print their names and course schedules
for student in student_list:
    print(student)