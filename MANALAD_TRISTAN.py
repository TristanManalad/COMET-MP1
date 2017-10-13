
class Course:

    def __init__(self, code, unit):
        self.student_list = []
        if unit > 4 or unit < 0:
            self.units = 0
        else:
            self.units = unit

        if len(code) == 7:
            self.code = code
        else:
            self.code = 'UNKNOWN'



    def edit_courseCode(self, code):
        if len(code) == 7:
            self.code = code.upper()
        else:
            self.code = 'UNKNOWN'


    def edit_courseunit(self, unit):
        if unit>4 or unit<0:
            self.units = 0
        else:
            self.units = unit


    def enroll_student(self, s):
        self.student_list.append(s)

    def drop_student(self, s):
        self.student_list.remove(self.student_list[int(s)])


    def get_name(self):
        return self.code


    def get_units(self):
        return self.units

    def print_studlist(self):
        ctr = 0
        while ctr != len(self.student_list):
            self.student_list[ctr].print_info()
            print(ctr)
            ctr = ctr + 1

    def check_enrolled(self):
        if len(self.student_list) != 0:
            return True
        else:
            return False

    def print_info(self):
        print(self.code, self.units, self.student_list)

##################################################################################################################################

class Student:

    def __init__(self, name, id):
        self.scourseList = []
        self.gradeList = []
        self.name = name
        self.enrolled = False

        if id > 10000000 or id < 99999999:
            self.uid = id
        else:
            self.uid = '00000000'

    def edit_studentname(self, name):
        self.name = name

    def edit_studentid(self, id):
        if id > 10000000 and id < 99999999:
            self.uid = id
        else:
            self.uid = '11111111'

    def set_grade(self, g):
        self.gradeList.append(g)

    def report_card(self):
        print("=============================================================================================\n")
        i = 0
        while i < len(self.scourseList):
                print(self.scourseList[i].get_name(), self.gradeList[i])
                i = i+1
        print("=============================================================================================\n")
    def print_info(self):
        print(self.name, self.uid)

    def print_courses(self):
        print("=============================================================================================\n")
        i = 0
        while i < len(self.scourseList):
                print(self.scourseList[i].get_name())
                i = i+1
        print("=============================================================================================\n")

    def get_name(self):
        return self.name

    def add_course(self, course):
        self.scourseList.append(course)


def isint():

    test = True
    while test is True:
        i = input("Enter: ")
        try:
            return int(i)
        except ValueError:
            print("Invalid input. Try again!")

#############################################################################################################################

courseList = []
studentList = []

while True:

    print(' 1-Enroll student to course\n'
          " 2-Drop student from course\n"
          " 3-Edit student information\n"
          " 4-Edit course information\n"
          " 5-Add course\n"
          " 6-Delete course\n"
          " 7-Add Student\n"
          " 8-Delete Student\n"
          " 9-View Report Card\n"
          " 10-View students\n"
          " 11-View available courses\n")

    opt = isint()

    if opt == 1:
        if len(courseList) != 0 and len(studentList) != 0:

            ctr = 0
            while ctr < len(courseList):
                print(courseList[ctr].get_name(), courseList[ctr].get_units())
                ctr = ctr + 1

            cour = input("Select course name: ")

            ctr = 0
            while ctr != len(studentList):
                studentList[ctr].print_info()
                print(ctr)
                ctr = ctr + 1

            stud = input("Select student NUMBER to enroll: ")

            i = 0
            while i < len(courseList):
                c = courseList[i].get_name()

                if cour == c:
                    courseList[i].enroll_student(studentList[int(stud)])
                    studentList[int(stud)].add_course(courseList[int(i)])
                    g = input("Enter students grade for this course: ")
                    studentList[int(stud)].set_grade(g)
                    print("ENROLLMENT SUCCESSFUL")

                i = i+1

        if len(courseList) == 0:
            print("No courses available. Please add some.")

        if len(studentList) == 0:
            print("No students available. Please add some.")


    elif opt == 2:
        if len(courseList) != 0:

            ctr = 0
            while ctr < len(courseList):
                print(courseList[ctr].get_name(), courseList[ctr].get_units())
                ctr = ctr + 1

            cour = input("Select course name: ")

            i = 0
            while i < len(courseList):
                c = courseList[i].get_name()

                if cour == c and courseList[i].check_enrolled is True:
                    courseList[i].print_studlist()
                    stud = input("Select student NUMBER to drop: ")
                    courseList[i].drop_student(stud)
                    print("DROPPING SUCCESSFUL")

                else:
                    print("No students enrolled to this course.")

                i = i+1


    elif opt == 3:
        ctr = 0
        while ctr != len(studentList):
            studentList[ctr].print_info()
            print(ctr)
            ctr = ctr + 1

        editstud = input("Enter student NUMBER to be edited: ")
        eds = input("Enter new name: ")
        ed = input("Enter new ID: ")

        studentList[editstud].edit_studentname(eds)
        studentList[editstud].edit_studentid(ed)


    elif opt == 4:
        print("To be finished")

    elif opt == 5:
        newc = input("Enter course name: ")
        unit = input("Enter units: ")

        courseList.append(Course(newc, int(unit)))

    elif opt == 6:
        print("To be finished")

    elif opt == 7:
        news = input("Enter student name: ")
        id = input("Input ID number: ")

        studentList.append(Student(news, int(id)))

    elif opt == 8:
        ctr = 0
        while ctr != len(studentList):
            studentList[ctr].print_info()
            print(ctr)
            ctr = ctr + 1
        stud = input("Enter student NUMBER to delete: ")
        studentList.remove(studentList[stud])

    elif opt == 9:
        if len(studentList) != 0:
            ctr = 0
            while ctr != len(studentList):
                studentList[ctr].print_info()
                print(ctr)
                ctr = ctr + 1

            stud = input("Enter student NUMBER to view: ")

            studentList[int(stud)].report_card()
        else:
            print("No students available")



    elif opt == 10:
        ctr = 0
        while ctr != len(studentList):
            studentList[ctr].print_info()
            ctr = ctr + 1

    elif opt == 11:
        ctr = 0
        while ctr < len(courseList):
            print(courseList[ctr].get_name(), courseList[ctr].get_units())
            ctr = ctr + 1


    else:
        print("Invalid input. Please try again.")






