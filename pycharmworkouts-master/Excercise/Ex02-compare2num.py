"""
Write a program to find the greatest of 2 numbers:
1. Get 2 numbers as input
2. Check the numbers are integers
3. Compare the numbers and find which is greater, which is lesser or equal
4. print the result as follows:-
    Greatest Value is
    Lesser Value is
    Both are equal/not equal



x = input("Enter Value1:")
y = input("Enter Value2:")


if x.isnumeric() and y.isnumeric():
    print("Invalid Input..Enter Only Integer Value..")
    exit(-1)


x = int(x)
y = int(y)

if x > y:
    print(f"Greatest Value is {x}")
elif x < y:
    print(f"Greatest Value is {y}")
else:
    print("Both are Equal")



x = input("Enter Value1:")
y = input("Enter Value2:")



res = x if x > y else y
print(f"Greatest value is {res}")

print(f"Greatest value is {x}") if x > y else print(f"Greatest value is {y}")

print(f"Greatest value is {x}") if x > y else (print(f"Greatest value is {y}") if x < y else print("Both are equal"))

"""

# if condition is False(0,None,"",[])
name = 0

name and print(f"Hello, {name}!")


