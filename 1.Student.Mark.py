students ={}
courses ={}
marks={}
def input_students():
    number_std=int(input("The number of students in the class: "))
    for i in range(number_std):
        std_id=input("Student ID: ")
        std_name=input("Student Name:")
        std_date_of_birth=input("Date of birth: ")
        students[std_id]={"studentname": std_name, "dateofbirth":std_date_of_birth}

def input_courses():
    number_courses=int(input("The number of courses: "))
    for i in range(number_courses):
        course_id=input("Course ID: ")
        course_name=input("Course Name: ")
        courses[course_id]={"coursename":course_name}
def input_stdmarks():
    course_id=input("Course ID: ")
    if course_id not in courses:
        print("No course available.")
        return
    if std_id in students:
        mark=int(input(f"Enter the marks for {students[std_id][studentname]}: "))
        if std_id not in marks:
            marks[std_id]={}
            students[std_id][course_id]=mark

def list_students():
    for std_id in students:
        print(f"{std_id}: {students[std_id][studentname]}")
def list_course():
    for course_id in courses:
        print(f"{course_id}: {course[coursename]}")
def list_mark():
    std_id=input("Student ID: ")
    course_id=input("Course ID: ")
    if std_id in students and course_id in courses:
        print(f"{std_id} - {course_id}: {marks[std_id]}")
    else:
        print("Non-existing Student ID or Course ID")          
selection=int(input("Enter your choice of selection: "))
if selection==1:
    input_students()
elif selection==2:
    input_courses()
elif selection==3:
    input_stdmarks()
elif selection==4:
    list_students()
elif selection==5:
    list_course()
elif selection==6:
    list_mark()