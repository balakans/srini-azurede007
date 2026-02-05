
def addnum(n1,n2):
    return n1 + n2

def subnum(n1,n2):
    return n1 - n2

def mulnum(n1,n2):
    return n1 * n2

def divnum(n1,n2):
    return n1 / n2

def squarenum(n1):
    return n1 ** 2

def cubenum(n1):
    return n1 ** 3

p1 = int(input("Enter Num1:"))

p2 = int(input("Enter Num2:"))



res = addnum(p1,p2)
print(f"Sum of {p1} and {p2} is {res}")

res = subnum(p1,p2)
print(f"Difference of {p1} and {p2} is {res}")

res = mulnum(p1,p2)
print(f"Product of {p1} and {p2} is {res}")

res = divnum(p1,p2)
print(f"Division of {p1} and {p2} is {res}")

res = squarenum(p1)
print(f"Square of {p1} is {res}")

res = squarenum(p2)
print(f"Square of {p2} is {res}")

res = cubenum(p1)
print(f"Cube of {p1} is {res}")


res = cubenum(p2)
print(f"Cube of {p2} is {res}")

