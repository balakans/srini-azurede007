#import Lab25_module as calc
from Lab25_module import *
from Lab17_higherorderfunction import calculator
import math
from math import sqrt

a = int(input("Enter Value1:"))
b = int(input("Enter Value2:"))
print(addnum(a,b))
print(subnum(a,b))
print(mulnum(a,b))
print(count)

"""
built in modules: math, os
Custom module: created by us
Third party modules: using via pip
pip install pandas
"""

print("Square root:",math.sqrt(16))

print("Square root:",sqrt(16))
calculator(10,20,lambda a,b: a +b)
