class Course:
    def show_course(self):
        print("This is OOP ")
class Student:
    def __init__(self,):
        self.course = Course()
    def show_course(self):
        self.course.show_course()
s1=Student()
s1.show_course()