import math 
import curses
import numpy as np
def wait_for_key(stdscr):
    """Waitting for user request to Menu"""
    stdscr.addstr("\nClick any button to return")
    stdscr.refresh()
    stdscr.getch()

def course_lists(stdscr,courses):#list courses
    stdscr.clear()
    stdscr.addstr(0,0,"\n----Course List----")
    row = 2 # row = truc x, column = truc y
    for course in courses:
        stdscr.addstr(row,0,f"ID:{course['id']},Name:{course['name']}")
        row +=1
    wait_for_key(stdscr)

def student_lists(stdscr,students):# list all of added info in list
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

def show_student_marks(stdscr,students,courses,marks):#show student marks
    stdscr.clear()
    stdscr.addstr(0,0,"\n-------Student Marks-----------")
    row = 2
    stdscr.addstr(row+1,0,"Enter Course ID to view marks: ")
    curses.echo()
    input_bytes = stdscr.getstr(row + 2,0)
    curses.noecho()
    course_id = input_bytes.decode('utf-8').strip()
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

def calculate_student_gpa(student_id,courses,marks):

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

def sort_students_by_gpa(students,courses,marks):
    """Update GPA and sort them"""
    for student in students:
        student['gpa'] = calculate_student_gpa(student['id'])
    #sort descending
    students.sort(key = lambda s: s['gpa'],reverse = True) #reverse = false => ascending order
    # s= value s: => run each value in s['gpa'] array

def show_sorted_gpa_list(stdscr,students,courses,marks):
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