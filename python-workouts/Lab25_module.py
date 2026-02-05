count = 0

def addnum(a,b):
    global count
    count = count + 1
    return a + b

def subnum(a,b):
    global count
    count = count + 1
    return a - b

def mulnum(a,b):
    global count
    count = count + 1
    return a * b

print("Name:",__name__)
if __name__ == "__main__":
    a = int(input("Enter Value1:"))
    b = int(input("Enter Value2:"))
    print("Inside Module:",addnum(a,b))