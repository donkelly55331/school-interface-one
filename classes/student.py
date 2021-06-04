from .person import Person
import csv
import os
class Student(Person):
    def __init__(self, name, age, role, school_id, password):
        # (super)__init__(self, name, age, role, password)
        super().__init__(name, age, role, password)
        # super(self, **school_info)
        self.school_id = school_id

    def __str__(student):
        return(f"{student.name}\n------------------\nage: {student.age}\nid: {student.school_id}")

    @classmethod     # will be called as 'Student.all_students()
    def all_students(cls):
        my_path = os.path.abspath(os.path.dirname(__file__))
        path = os.path.join(my_path, "../data/students.csv")
        # print(path)
        
        # with open('../data/students.csv') as student_file:
        with open(path) as student_file:
            student_reader = csv.DictReader(student_file)
            student_arr = []
            for row in student_reader:
                # student_arr.append(Student(row['name'], row['age'], row['role'], row['school_id'], row['password']))
                student_arr.append(Student(**dict(row)))
            return student_arr

    def age_of(self, name):
        for student in student_arr:
            if student('name') == name:
                return f"{student.name} is {student.age} years old"

# students = Student(self, name, age, role, school_id, password)
    
    # all_students()

# if __name__ == "__main__"
#     source = sys.argv[1]
#     td = MyClass()
#     needed_stuff = td.convert(source)
#     print(needed_stuff)


# calling
Student.all_students()
