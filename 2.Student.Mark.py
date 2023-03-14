class Student:
    def __init__(self, student_id, student_name, student_dateofbirth):
        self.id=student_id
        self.name=student_name
        self.dateofbirth=student_dateofbirth

# This class displays information about Course 
class Course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name

class Major(Student,Course):
    def __init__(self):
        self.student = {}
        self.course = {}
        self.mark = {}

    def addStudent(self):
        studentNum = int(input("Enter studentNum: "))
        for i in range(studentNum):
            id = input("Student ID: ")
            name = input("Student Name: ")
            dateofbirth = input("Student Dob: ")
            self.student[id] = Student(id, name, dateofbirth)

    def addCourse(self):
        courseNum = int(input("Ender courseNum: "))
        for i in range (courseNum):
            id = input("Course ID: ")
            name = input("Course Name: ")
            self.course[id] = Course(id, name)

    def addMark(self):
        courseID = input("CourseID: ")
        if courseID not in self.course:
            print("No course exists!")
            return  
        
        for studentID in self.student:
            mark = input("MARK: ")
            if studentID not in self.mark:
                self.mark[id] = {}
            self.mark[studentID] = mark

    def outputStudent(self):
        for id in self.student:
            print(f"{id} :  {self.student[id]['name']['dob']}")
    def outputMark(self):
        for id in self.student:
            print(f"{id} : {self.mark[id]}")



runcode = Major()
runcode.addStudent()
runcode.addCourse()
runcode.addMark()
runcode.outputMark()