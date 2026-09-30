
import curses
import input as input_module
import output as output_module
students =[]
courses = []
marks = {}
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
            input_module.input_students_information(stdscr,students)
        elif choice == '2':
            input_module.input_course_info(stdscr,courses)
        elif choice == '3':
            input_module.input_course_marks(stdscr,students,courses,marks)
        elif choice == '4':
            output_module.student_lists(stdscr,students)
        elif choice == '5':
            output_module.course_lists(stdscr,courses)
        elif choice == '6':
            output_module.show_student_marks(stdscr,students,courses,marks)
        elif choice == '7':
            output_module.show_sorted_gpa_list(stdscr,students,courses,marks)
        elif choice == '8':
            break
def main():
    curses.wrapper(main_curses)

if __name__ == "__main__":
    main()