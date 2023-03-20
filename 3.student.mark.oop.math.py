import numpy as np
import math as math
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

class Credits:
    def __init__(self,courseNum):
        for i in range(courseNum):
            b = []
            take_input = int(input('Input the number of credits of course: '))
            b.append(take_input)
        self.__credits=b.append(take_input)
    def getInfo(self):
        return self.__credits

class Marks:
    def __init__(self):
        self.__midterm = []
        self.__final = []
        self.__mark = []
    def setMark(self, studentNum, courseNum):
        for i in range(courseNum):
            a = []
            b = []
            c = []
            for j in range(studentNum):
                midterm = float(input("Input mark of student " + str((j+1)) + " in course " + str((i+1)) + ": " ))
                final = float(input("Input mark of student " + str((j+1)) + " in course " + str((i+1)) + ": " ))
                mark = 0.4  * midterm + 0.6 * final
                midterm.append()
                a.append(midterm)
                b.append(final)
                c.append(mark)
            self.__midterm.append(a)
            self.__final.append(b)
            self.__mark.append(c)
    def getMark(self):
        return self.__midterm, self.__final, self.__mark
    def sortMark(self):
        a = np.array[]
        arr = a.append(a , self.__mark)
        sortedarr = np.sort(arr)
        return sortedarr
    def averageGPA(self):
        
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


runcode4 = Credits(courseNum)

