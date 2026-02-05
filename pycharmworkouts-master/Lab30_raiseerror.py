
"""
try:

    x = input("Enter a Number1:")
    y = input("Enter a Number2:")

    if(x.isnumeric() and y.isnumeric()):
        r = x + y
        print("Output:", r)
    else:
        raise ValueError("Invalid Input")

except ValueError as err:
    print(err)

"""

try:
    r = 10/0
except Exception as err:
    print(err)

#------raising error manually---------------
while(True):
    try:
        try:
            age = int(input("Enter Age:"))
            if age < 0:
                raise Exception("Invalid Age")
            print(age)
        except Exception as err:
            print(err)
            exit()
        else:
            print("Else Block")
        finally:
            print("************************")
    except Exception:
        print("Parent Error")
    else:
        print("Parent Else")
    finally:
        print("Finally")

print("Hello")