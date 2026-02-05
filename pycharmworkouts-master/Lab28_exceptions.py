
"""
try:
    x = int(input("Enter a Number1:"))
    y = int(input("Enter a Number2:"))
    r = x + y
    print("Output:",r)

except Exception:
    print("Error:Invalid Integer Value")
else:
    print("No Error")

"""

#ZeroDivsionError
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: You cannot divide by zero.")

#NameError
try:
    print(my_variable)
except NameError:
    print("Error: The variable 'my_variable' is not defined.")

#FileNotFoundError
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: The file was not found.")

#TypeError
try:
    result = "hello" + 5
except TypeError:
    print("Error: You cannot concatenate a string and an integer.")

#ValueError
try:
    number = int("abc")
except ValueError:
    print("Error: 'abc' cannot be converted to an integer.")

#IndexError
my_list = [1, 2, 3]
try:
    element = my_list[5]
except IndexError:
    print("Error: The list index is out of range.")

#KeyError
my_dict = {"name": "Alice"}
try:
    print(my_dict["age"])
except KeyError:
    print("Error: The key 'age' does not exist in the dictionary.")

#Exception is a base class for all other errors

try:
    result = 10 / 0
    number = int("123")
    print(my_variable)
    result = "hello" + 5

except ValueError:
    print("Error: Value Error")
except ZeroDivisionError:
    print("Error: ZeroDivision Error")
except Exception:
    print("Error: Exception")