from .staff import Staff
from .student import Student
import csv
import os

class School:
    def __init__(self, name):
        self.name = name
        self.students = Student.all_students()
        # self.staff = Staff.all_staff

    def list_students(self):
        for i, student in enumerate(self.students):
            print(f"{i+1} Name: {student.name} Age: {student.age} Role: {student.role} ID #: {student.school_id} Password: {student.password}")
        
    def find_student_by_id(self, s_id):
        for student in self.students:
           if student.school_id == s_id:
               return student

    def add_student(self, student_data):
        new_student = Student(**dict(student_data))
        self.students.append(new_student)
        self.store_students()
        
    def store_students(self):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        with open(path, 'w', newline = '\n') as csvfile:
            field_names = ['name', 'age', 'password', 'role', 'school_id']
            writer = csv.DictWriter(csvfile, field_names)
            writer.writeheader()
            for student in self.students:
                writer.writerow({'name': student.name, 'age': student.age, 'role': student.role, 'school_id': student.school_id, 'password': student.password})

    def delete_student(self, student):
        self.students.remove(student)
        self.store_students()


