
"""
Lambda Function, also referred to as ‘Anonymous function’ is same as a regular python function
but can be defined without a name

The syntax for lambda function is given by : lambda arguments: expression
There can be any number of arguments but can contain only a single expression


"""
def addnum(a,b):
    return a + b

print("Normal Output:",addnum(10,20))


addnum1 = lambda a,b : a + b

print("Lambda output:",addnum1(10,20))

#write lambda function to check given number is odd or even

def checkoddoreven(a):
    if a % 2 == 0:
        print("Even Number")
    else:
        print("ODD Number")

checkoddoreven(1235)

checkoddoreven1 = lambda a: print("Even Number") if a %2 == 0 else print("ODD Number")

checkoddoreven1(1235)




#Higher order function
def calculator(a,b,f):
    print("a value is",a)
    print("b value is", b)
    res = f(a,b)
    print(res)


calculator(10,20,addnum)


calculator(10,20,lambda x,y: x + y)




def subnum(a,b):
    return a - b

calculator(20,10, subnum)
calculator(20,10,lambda x,y: x - y)



calculator(10,20,lambda x,y: x * y)


def func1():
    print("I called from lambda function")
    print("I am func1")

#lambda function without parameters
h = lambda : print("Hi, I am lambda function")

#calling other function inside lambda function
h = lambda : func1()

h()

print("=======================================")

def hdfc(p,n):
    return p * n * 5 / 100

def axis(p,n):
    return p * n * 8 / 100

def citi(p,n):
    return p * n * 10 / 100

def otherbank(p,n):
    return p * n * 12 / 100


#interetamt = axis(1000,5)

#print("InterestAmount:",interetamt)

#Higher order function
def calcualteinterest(p,n,banktype):
    intrst = banktype(p,n)
    print("Before return:",intrst)
    return intrst

interetamt = calcualteinterest(1000,5,axis)
#or
interetamt = calcualteinterest(1000,5,lambda p,n: p* n * 5/100)

print("InterestAmount:",interetamt)

interetamt = calcualteinterest(1000,5,hdfc)
#or
interetamt = calcualteinterest(1000,5,lambda p,n: p* n * 8/100)

print("InterestAmount:",interetamt)

interetamt = calcualteinterest(1000,5,citi)
#or
interetamt = calcualteinterest(1000,5,lambda p,n: p* n * 10/100)

print("InterestAmount:",interetamt)

interetamt = calcualteinterest(1000,5,otherbank)
#or
interetamt = calcualteinterest(1000,5,lambda p,n: p* n * 12/100)

print("InterestAmount:",interetamt)

calcinterest = lambda p,n: p* n * 12/100

interetamt = calcualteinterest(1000,5,calcinterest)
