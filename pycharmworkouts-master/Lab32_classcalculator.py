
#Create class called Calculator
class Calculator():
    def addnum(self,a,b):
        return a + b

    def subnum(self, a, b):
        return a - b

    def mulnum(self, a, b):
        return a * b

#Creating an Object for the class calculator
c1 = Calculator()

print("=======Object c1======")
#Access the Calcualtor class methods
print(c1.addnum(10,20))
print(c1.subnum(10,20))
print(c1.mulnum(10,20))

print("=======Object c2======")
c2 = Calculator()
print(c2.addnum(10,20))
print(c2.subnum(10,20))
print(c2.mulnum(10,20))