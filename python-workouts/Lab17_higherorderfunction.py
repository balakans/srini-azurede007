"""
Higher Order Functions:Functions that can accept other functions as arguments or return function as value are called higher-order functions.
Functions are objects we can pass them as arguments to other functions.
"""

def addnum(a,b):
    c = a + b
    return c

def subnum(a,b):
    c = a - b
    return c

def prodnum(a,b):
    c = a * b
    return c
def square(a):
    return a * a

#Higher order function
def calculator(a,b,ops):
    print("a value is",a)
    print("b value is", b)
    print(ops(a,b))

def calculator1(a,b,func):
    print(a)
    print(b)
    print(func(a,b))

if __name__ == "__main__":
    calculator(10,5,addnum)
    calculator(10,5,subnum)

