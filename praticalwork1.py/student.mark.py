students = []
    # {'id': 'S001',
    # 'name':'thach',
    # 'dob':'15/07/2007'}

courses = []
    # {'id': 'MAT1.001','name':'Calculus I'},
    # {'id': 'MAT1.002','name':'Linear Algebra'}

marks = {}

def input_number_of_students(): #total of students
    return int(input("Enter number of students: "))

def input_students_information():# adding infos into list
    num = input_number_of_students()
    for students in range(num):
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("DoB (DD//MM/YYYY): ")
        students.append({'id':s_id,'name':name,'dob':dob})

def student_lists():# list all of added info in list
    print("\n----Student List ----")
    for student in students:
        print(f"ID:{student['id']}, Name:{student['name']},DoB:{student['dob']}")
#------------------------------------------------
def input_number_of_courses():
    return int(input("Enter number of courses: "))

def input_course_info():
    num = input_number_of_courses()
    for courses in range(num):
        c_id = input("Course ID: ")
        c_name = input("Course Name: ")
        courses.append({'id':c_id,'name':c_name})

def course_lists():
    print("\n----Course List----")
    for course in courses:
        print(f"ID:{course['id']},Name:{course['name']}")



