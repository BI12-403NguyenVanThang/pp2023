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

class Credits(Course):
    def __init__(self,courseNum):
        self.__credits = np.empty(0)
    def getSum(self,i):
        return self.__credits[i]
        
class Marks(Credits):
    def __init__(self):
        self.__midterm = []
        self.__final = []
        self.__mark = []
    def setMark(self, studentNum, courseNum):
        for i in range(courseNum):
            c = []
            for j in range(studentNum):
                midterm = np.floor(float(input("Input mark of student " + str((j+1)) + " in course " + str((i+1)) + ": " )))
                final = np.floor(float(input("Input mark of student " + str((j+1)) + " in course " + str((i+1)) + ": " )))
                mark = 0.4  * midterm + 0.6 * final
                c.append(mark)
            self.__mark.append(c)
    def getMark(self):
        return self.__mark
    def sortMark(self):
        a = np.empty(0)
        arr = a.append(a , self.__mark)
        sortedarr = np.sort(arr)[::-1]
        return sortedarr
    def averageGPA(self, courseNum, studentNum):
        super().__init__(courseNum)
        sum = 0
        j=0
        i=0
        while i < studentNum:
            if j==courseNum:
                i += 1
            else:
                while j < courseNum:
                    sum += (self.__mark[j][i]*super().getSum(j))
                    sumCredit = super().getSum(courseNum)
                    j+=1
        
        return sum/sumCredit
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
runcode3.getMark()
runcode3.averageGPA(courseNum,studentNum)
