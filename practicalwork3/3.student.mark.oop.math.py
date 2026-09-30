
import math
import numpy as np
import curses
students = []
    # {'id': 'S001',
    # 'name':'thach',
    # 'dob':'15/07/2007'}

courses = []
    # {'id': 'MAT1.001','name':'Calculus I'},
    # {'id': 'MAT1.002','name':'Linear Algebra'}

marks = {}

def get_input(stdscr, prompt_str):
    """Curses UI Assistance"""
    stdscr.clear()
    stdscr.addstr(0,0, prompt_str)
    curses.echo()
    input_bytes = stdscr.getstr(1,0)
    curses.noecho()
    return input_bytes.decode('utf-8').strip()

def wait_for_key(stdscr,row =10):
    """Waitting for user request to Menu"""
    stdscr.addstr("\nClick any button to return")
    stdscr.refresh()
    stdscr.getch()


def input_number_of_students(stdscr): #total of students
    val = get_input(stdscr,"Enter the number of students: ")
    return int(val) if val.isdigit() else 0


def input_students_information(stdscr):# adding infos into list
    num = input_number_of_students(stdscr)
    for i in range(num):
        stdscr.clear()
        stdscr.addstr(0,0,f"---- Student {i+1} ----")
        s_id = get_input(stdscr,f"Student {i+1} ID: ")
        name = get_input(stdscr,f"Student {i+1} Name: ")
        dob = get_input(stdscr,"DoB (DD/MM/YYYY): ")
        students.append({'id':s_id,'name':name,'dob':dob,'gpa':0.0})

def student_lists(stdscr):# list all of added info in list
    stdscr.clear()
    stdscr.addstr(0,0, "\n---- Student List ----")
    row = 2
    for student in students:
        gpa_val = student.get('gpa',0.0)
        stdscr.addstr(row,0,f"ID:{student['id']}")
        stdscr.addstr(row+1,0,f"Name:{student['name']}")
        stdscr.addstr(row+2,0,f"DoB:{student['dob']}")
        stdscr.addstr(row+3,0,f"----------------------------------------------")
        row+=4
    wait_for_key(stdscr)
#------------------------------------------------
def input_number_of_courses(stdscr):#add total courses
    val = get_input(stdscr,"Enter number of courses: ")
    return int(val) if val.isdigit() else 0

def input_course_info(stdscr):#add courses info
    num = input_number_of_courses(stdscr)
    for i in range(num):
        stdscr.addstr(f"\n---- Course {i+1} ----")
        c_id = get_input(stdscr,f"Course ID: ")
        c_name = get_input(stdscr,f"Course Name: ")
        credit_str = get_input(stdscr,f"Course Credits: ")
        try:
            credit = float(credit_str)
        except ValueError:
            credit = 1.0
        courses.append({'id':c_id,'name':c_name,'credit': credit})

def course_lists(stdscr):#list courses
    stdscr.clear()
    stdscr.addstr(0,0,"\n----Course List----")
    row = 2 # row = truc x, column = truc y
    for course in courses:
        stdscr.addstr(row,0,f"ID:{course['id']},Name:{course['name']}")
        row +=1
    wait_for_key(stdscr)
#-----------------------------

def input_course_marks(stdscr):#add marks to courses
    #validation
    if not courses:
        stdscr.clear()
        stdscr.addstr(0,0, "No courses available")
        wait_for_key(stdscr)
        return
    if not students:
        stdscr.clear()
        stdscr.addstr(0,0, "No students")
        wait_for_key(stdscr)
        return
    stdscr.clear()
    row = 2
    for course in courses:
        stdscr.addstr(row,0,f"ID:{course['id']},Name:{course['name']}")# this runs after stdscr.addstr(0,0,"\n----Selecting Course----")
        row +=1
    #Select courses
    stdscr.addstr(0,0,"\n----Selecting Course----")
    # course_id = get_input(stdscr,"Enter Course ID: ")
    stdscr.addstr(row+1,0,"Enter Course ID: ")
    curses.echo()
    input_bytes = stdscr.getstr(row + 2, 0)
    curses.noecho()
    course_id = input_bytes.decode('utf-8').strip()
    
    #check if course exists
    selected_course = None
    for course in courses:
        if (course['id']== course_id):
            selected_course = course
            break
    if not selected_course:
        stdscr.clear()
        stdscr.addstr(0,0,f"Course with ID {course_id} not found.\n")
        wait_for_key(stdscr)
        return

    #loop through student and input marks
    stdscr.addstr(0,0,f"\n---- Marks For {selected_course['name']}({course_id}) Course ----")
    for student in students:
        while True:
            score_str = get_input(stdscr,
            f"Enter mark for {student['name']},(ID:{student['id']})")
            try:
                score = float(score_str)
                if 0 <= score <=20:
                    #Round down the score into 1 decimal
                    rounded_score = math.floor(score*10)/10.0
                    marks[(course_id,student['id'])] = rounded_score
                    break
                else:
                    stdscr.addstr("Please enter a mark between 0 and 20")
            except ValueError:
                stdscr.addstr("Invalid input. Please enter an actual number")
#--------------------------------------------
def show_student_marks(stdscr):#show student marks
    stdscr.clear()
    stdscr.addstr(0,0,"\n-------Student Marks-----------")
    course_id = get_input(stdscr,"Enter Course ID to view marks: ")
    stdscr.clear()
    stdscr.addstr(0,0,f"\n---- Marks for Course ID: {course_id}----")
    row = 2
    found = False
    for student in students:
        key = (course_id,student['id'])
        if key in marks:
            stdscr.addstr(row,0,f"Student: {student['name']}(ID: {student['id']}) -> Mark:{marks[key]}")
            row +=1
            found = True

    if not found:
        stdscr.addstr(row,0,"Marks not found") 
    wait_for_key(stdscr)      

def calculate_student_gpa(student_id):

    """numpy array"""
    student_marks = []
    credits = []
    for course in courses:
        key = (course['id'],student_id)
        if key in marks:
            student_marks.append(marks[key])
            credits.append(course['credit'])
    if not credits:
        return 0.0

    #Convert to Numpy array
    marks_arr = np.array(student_marks)
    credits_arr = np.array(credits)

    #weighted sum
    weighted_sum = np.sum(marks_arr*credits_arr)
    total_credits = np.sum(credits_arr)
    if total_credits == 0:
        return 0.0
    gpa = weighted_sum / total_credits
    return math.floor(gpa*100)/100.0

def sort_students_by_gpa():
    """Update GPA and sort them"""
    for student in students:
        student['gpa'] = calculate_student_gpa(student['id'])
    #sort descending
    students.sort(key = lambda s: s['gpa'],reverse = True) #reverse = false => ascending order
    # s= value s: => run each value in s['gpa'] array

def show_sorted_gpa_list(stdscr):
    sort_students_by_gpa()
    stdscr.clear()
    stdscr.addstr(0,0,"---- Student List Sorted By Desceding GPA ----")
    row = 2
    for rank, student in enumerate(students,start =1):
        stdscr.addstr(
            row,0,
            f"Rank {rank} | ID: {student['id']} | Name: {student['name']} | GPA: {student['gpa']}"
        )
        row += 1
    wait_for_key(stdscr)

def main_curses(stdscr):
    curses.curs_set(1)
    stdscr.keypad(True)

    while True:
        stdscr.clear()
        stdscr.addstr(0,0, "=== STUDENT MANAGEMENT SYSTEM ===")
        stdscr.addstr(2,0, "1. Input Student Information")
        stdscr.addstr(3,0, "2. Input Course Information")
        stdscr.addstr(4,0, "3. Input Course Marks")
        stdscr.addstr(5,0, "4. List Students")
        stdscr.addstr(6,0, "5. List Courses")
        stdscr.addstr(7,0, "6. Show Course Marks")
        stdscr.addstr(8,0, "7. Sort & Show Students by GPA (Descending)")
        stdscr.addstr(9,0, "8.Exit")
        stdscr.addstr(11,0, "Select option [1-8]: ")
        stdscr.refresh()

        key = stdscr.getch()
        choice = chr(key) if 0 <= key <= 256 else ''
        if choice == '1':
            input_students_information(stdscr)
        elif choice == '2':
            input_course_info(stdscr)
        elif choice == '3':
            input_course_marks(stdscr)
        elif choice == '4':
            student_lists(stdscr)
        elif choice == '5':
            course_lists(stdscr)
        elif choice == '6':
            show_student_marks(stdscr)
        elif choice == '7':
            show_sorted_gpa_list(stdscr)
        elif choice == '8':
            break
def main():
    curses.wrapper(main_curses)

if __name__ == "__main__":
    main()

# input_students_information()
# student_lists()

# input_course_info()
# # course_lists()

# input_course_marks()
# show_student_marks()
