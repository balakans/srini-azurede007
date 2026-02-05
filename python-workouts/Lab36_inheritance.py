"""
Inheritance is the process of inherits one class(parent) with the other class(child).
child class can access all the members and methods of parent class
"""

import math

class calculator:

    def addnum(self, a, b):
        print(f"calculator:Sum of {a} and {b} is {a + b}")

    def subnum(self, a, b):
        print(f"Difference of {a} and {b} is {a - b}")

    def prodnum(self, a, b):
        print(f"Product of {a} and {b} is {a * b}")

#Child class scicalculator inherits parent class Calculator
class scicalculator(calculator):

    def square(self,a):
        print(f"Square of {a} is {a**2}")

    def cube(self, a):
        print(f"Cube of {a} is {a ** 3}")

class advcalculator(scicalculator):
    def dollartorupee(self,a):
        print(f"For the given dollar value {a}, the equivalent rupee value is {a * 70}")

    def eurotorupee(self,a):
        print(f"For the given euro value {a}, the equivalent rupee value is {a * 120}")

scalc = scicalculator()

#parent class method
scalc.addnum(10,20)
scalc.subnum(20,10)
scalc.prodnum(10,20)

#child class method
scalc.square(10)
scalc.cube(10)



print("=====Multi-Level Inheritance===")
acalc = advcalculator()

acalc.dollartorupee(10)
acalc.eurotorupee(10)
#Calculator methods
acalc.addnum(10,20)
acalc.subnum(20,10)
acalc.prodnum(10,20)

#scientic class method
acalc.square(10)
acalc.cube(10)

#Adv class methods
acalc.dollartorupee(10)
acalc.eurotorupee(10)

class scicalculator1():

    def addnum(self, a, b):
        print(f"scicalculator1:Sum of {a} and {b} is {a + b}")

    def square(self,a):
        print(f"Square of {a} is {a**2}")

    def cube(self, a):
        print(f"Cube of {a} is {a ** 3}")

#Multiple Inheriance
class trigcalculator(scicalculator1,calculator):
    def getcosvalue(self,x):
        res = math.cos(x)
        print(f"Cos value of {x} is {res}")

    def getsinvalue(self,x):
        res = math.sin(x)
        print(f"Sin value of {x} is {res}")

tcalc = trigcalculator()
tcalc.addnum(10,20)
