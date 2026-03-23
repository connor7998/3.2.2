from course import Course

class Student:
    
    student_id = 0
    
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.courses = []
        self.student_id = Student.student_id
        Student.student_id += 1
    
    def __str__(self):
        # Calling "print(student)" from main.py will call this method instead
        # Build a list of course names from the student's course list
        course_names = []
        for course in self.courses:
            course_names.append(str(course))

        courses_str = ", ".join(course_names) if course_names else "No courses"

        return f"{self.first_name} {self.last_name} (ID: {self.student_id}) - Courses: {courses_str}"
        
    def get_first_name(self):
        return self.first_name
        
    def get_last_name(self):
        return self.last_name
        
    def get_student_id(self):
        return self.student_id
    
    def add_course(self, new_course):
        if isinstance(new_course, Course):
            self.courses.append(new_course)
        else:
            raise TypeError("add_course expects a Course instance")
        return self