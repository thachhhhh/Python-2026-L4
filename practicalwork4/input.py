import curses
import math
from domains import Student, Course

#UI for curses

def get_input(stdscr, prompt_str):
    """Curses UI Assistance"""
    stdscr.clear()
    stdscr.addstr(0,0, prompt_str)
    curses.echo()
    input_bytes = stdscr.getstr(1,0)
    curses.noecho()
    return input_bytes.decode('utf-8').strip()

#Students

def input_number_of_students(stdscr): #total of students
    val = get_input(stdscr,"Enter the number of students: ")
    return int(val) if val.isdigit() else 0
def input_students_information(stdscr,students):# adding infos into list
    num = input_number_of_students(stdscr)
    for i in range(num):
        stdscr.clear()
        stdscr.addstr(0,0,f"---- Student {i+1} ----")
        s_id = get_input(stdscr,f"Student {i+1} ID: ")
        name = get_input(stdscr,f"Student {i+1} Name: ")
        dob = get_input(stdscr,"DoB (DD/MM/YYYY): ")
        students.append({'id':s_id,'name':name,'dob':dob,'gpa':0.0})



#Courses

def input_number_of_courses(stdscr):#add total courses
    val = get_input(stdscr,"Enter number of courses: ")
    return int(val) if val.isdigit() else 0
def input_course_info(stdscr,courses):#add courses info
    num = input_number_of_courses(stdscr)
    for i in range(num):
        stdscr.clear()
        stdscr.addstr(f"\n---- Course {i+1} ----")
        c_id = get_input(stdscr,f"Course ID: ")
        c_name = get_input(stdscr,f"Course Name: ")
        credit_str = get_input(stdscr,f"Course Credits: ")
        try:
            credit = float(credit_str)
        except ValueError:
            credit = 1.0
        courses.append({'id':c_id,'name':c_name,'credit': credit})
def input_course_marks(stdscr,students,courses,marks):#add marks to courses
    #validation
    if not courses:
        stdscr.clear()
        stdscr.addstr(0,0, "No courses available")
        stdscr.getch()
        return
    if not students:
        stdscr.clear()
        stdscr.addstr(0,0, "No students")
        stdscr.getch()
        return
    #Display courses
    stdscr.clear()
    row = 2
    for course in courses:
        stdscr.addstr(row,0,f"ID:{course['id']},Name:{course['name']}")
        row +=1
    #Select courses
    stdscr.addstr(0,0,"\n----Selecting Course----")
    stdscr.addstr(row+1,0,"Enter Course ID: ")
    curses.echo()
    input_bytes = stdscr.getstr(row +2,0)
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
        stdscr.getch()
        return

    #loop through student and input marks
    for student in students:
        while True:
            stdscr.clear()
            stdscr.addstr(0,0,f"\n---- Marks For {selected_course['name']}({course_id}) Course ----")
            stdscr.addstr(2,0,f"Enter mark for {student['name']} (ID: {student['id']}[0-20]):)")
            curses.echo()
            input_bytes = stdscr.getstr(3,0)
            curses.noecho()
            score_str = input_bytes.decode('utf-8').strip()
            
            try:
                score = float(score_str)
                if 0 <= score <=20:
                    #Round down the score into 1 decimal
                    rounded_score = math.floor(score*10)/10.0
                    marks[(course_id,student['id'])] = rounded_score
                    break
                else:
                    stdscr.addstr(5,0,"Please enter a mark between 0 and 20")
                    stdscr.getch()
            except ValueError:
                stdscr.addstr(5,0,"Invalid input. Please enter an actual number")
                stdscr.getch()