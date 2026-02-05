
class Student():

    def __init__(self,sid,sname,mark1,mark2,mark3):
        self.studid = sid
        self.studname = sname
        self.m1 = mark1
        self.m2 = mark2
        self.m3 = mark3

    def displaystudentinfo(self):
        print("********Student Info**********")
        print("Student Id:",self.studid)
        print("Student Name:", self.studname)
        print("Student Mark1:", self.m1)
        print("Student Mark2:", self.m2)
        print("Student Mark3:", self.m3)


    def calcualtemarks(self):
        totalmarks = self.m1 + self.m2 + self.m3
        print("=================")
        print("Total Marks:",totalmarks)


s1 = Student("1001","Rajesh",85,90,87)
s1.displaystudentinfo()
s1.calcualtemarks()

s2 = Student("1002","SWathi",95,90,100)
s2.displaystudentinfo()
s2.calcualtemarks()



