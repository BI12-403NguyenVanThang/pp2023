class Course:
    def __init__(self):
        self.__info={}
    def setInfo(self, id, name):
        self.__info.update({id : name})
    def getInfo(self):
        return self.__info
class Student(Course):
    def __init__(self, dob):
        super().__init__()
        self.__dob=dob
    def setInfo(self, id, name, dob):
        super().setInfo(id, name + " " + dob)
    def getInfo(self):
        return super().getInfo()

class Marks:
    def __init__(self):
        self.__mark = []

    def setMark(self, studentNum, courseNum):
        for i in range(courseNum):
            a = []
            for j in range(studentNum):
                mark = float(input("Input mark of student " + str((j+1)) + " in course " + str((i+1)) ))
                a.append(mark)
            self.__mark.append(a)
    def getMark(self):
        return self.__mark

runcode = Student('')
studentNum=int(input("Input number of students: "))

for i in range(studentNum):
    id=input("Input id: ")
    name=input("Input name: ")
    dob=input("Input dob: ")
    runcode.setInfo(id,name,dob)
runcode.getInfo()

runcode2 =Course()
courseNum=int(input("Input number of course: "))

for i in range(courseNum):
    id=input("Input id: ")
    name=input("Input name: ")
    runcode2.setInfo(id,name)
runcode2.getInfo()

runcode3 = Marks()
runcode3.setMark(studentNum,courseNum)
print(runcode3.getMark())
