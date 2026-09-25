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
    for i in range(num):
        s_id = input("Student ID: ")
        name = input("Student Name: ")
        dob = input("DoB (DD//MM/YYYY): ")
        students.append({'id':s_id,'name':name,'dob':dob})

def student_lists():# list all of added info in list
    print("\n----Student List ----")
    for student in students:
        print(f"ID:{student['id']}\nName:{student['name']}\nDoB:{student['dob']}\n-----------------")
#------------------------------------------------
def input_number_of_courses():#add total courses
    return int(input("Enter number of courses: "))

def input_course_info():#add courses info
    print("\n------ Course_Info---------")
    num = input_number_of_courses()
    for i in range(num):
        c_id = input("Course ID: ")
        c_name = input("Course Name: ")
        courses.append({'id':c_id,'name':c_name})

def course_lists():#list courses
    print("\n----Course List----")
    for course in courses:
        print(f"ID:{course['id']},Name:{course['name']}")
#-----------------------------

def input_course_marks():#add marks to courses
    #validation
    if not courses:
        print("No courses available")
        return
    if not students:
        print("No students")
        return
    #Display courses
    print("----Available courses----")
    for course in courses:
        print(f"ID:{course['id']},Name:{course['name']}")
    #Select courses
    course_id = input("\nEnter Course ID: ").strip()
    #check if course exists
    selected_course = None
    for course in courses:
        if (course['id']== course_id):
            selected_course = course
            break
    if not selected_course:
        print(f"Course with ID {course_id} not found.")
        return

    #loop through student and input marks
    print(f"Entering Marks For Course {selected_course['name']}({course_id}):")
    for student in students:
        while True:
            try:
                score = float(input(f"Enter mark for {student['name']}(ID:{student['id']}): "))
                if 0 <= score <=20:
                    marks[(course_id,student['id'])] = score
                    break
                else:
                    print("Please enter a mark between 0 and 20")
            except ValueError:
                print("Invalid input. Please enter an actual number")
#--------------------------------------------
def show_student_marks():#show student marks
    print("\n-------Student Marks-----------")
    course_id = input("\nEnter Course ID to view marks: ").strip()
    print(f"\n---- Marks for Course ID: {course_id}----")
    found = False
    for student in students:
        key = (course_id,student['id'])
        if key in marks:
            print(f"Student: {student['name']}(ID: {student['id']}) -> Mark:{marks[key]}")
            found = True
    if not found:
        print("Marks not found")       

input_students_information()
student_lists()

input_course_info()
# course_lists()

input_course_marks()
show_student_marks()
