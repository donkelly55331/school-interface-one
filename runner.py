from classes.school import School
# from classes.student import Student

school = School('Ridgemont High') 

# my_input prints <prompt> and accepts an integer from <min> to <max>
# returns if <enter> pressed
def my_input(prompt1, prompt2, min, max):
    val = None
    print(prompt1)
    while val == None:
        try:
            val = input(f"\n{prompt2}  ")
            if val == '':
                return ''
            if not val.isnumeric():
                val = None
            else:
                val = int(val)
        except: 
            pass

        if val == None or not (min <= val and val <= max):
            print(f"Please enter a number from {min} to {max}.")
            val = None
    return val

def find_student():
    student_id = str(my_input('', 'Student ID:', 1, 999999))
    if student_id == "":
        return None
    else: 
        result = school.find_student_by_id(student_id)
        if result == None:
            print(f"Student {student_id} not in database")
            return None
        else:
            return result

print(school.name)

# from runner2.py
# print(school.staff)
# print(school.students)

mode = None
while mode != '5':
    menu = "\nWhat would you like to do?\n\nOptions:\n\n1. List All Students\n2. View Individual Student\n3. Add a Student\n4. Remove a Student\n5. Quit"

    mode = str(my_input(menu, 'mode:', 1, 5))
    if mode == '':
        break

    if mode == '1':
        school.list_students()

    elif mode == '2':
        student = find_student()
        if student != None:
           print(str(student))

    elif mode == '3':
        student_data = {'role': 'student'}
        student_data['name'] = input('Enter student name:  ')
        student_data['age'] = input('Enter student age:  ')
        student_data['school_id'] = input('Enter student school id:  ')
        student_data['password'] = input('Enter student password:  ')
        school.add_student(student_data)
        print(f"Added student {student_data['name']}")

    elif mode == '4':
        student = find_student()
        if student != None:
            school.delete_student(student)
    