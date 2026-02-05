
"""
a = int(input("Enter Number1:"))
b = int(input("Enter Number2:"))


#a = int(a)
#b = int(b)

print(f"Sum of {a} and {b} is {a+b}")
"""



sid = input("Enter student id:")

if (sid.isnumeric()):
    sid = int(sid)
else:
    print("Invalid Student Id or Student Id should be Numeric")
    exit(-1)


sname = input("Enter student name:")
englishmark = int(input("Enter english mark:"))
sciencemark = int(input("Enter science mark:"))
mathsmark = int(input("Enter maths mark:"))




totalmarks = englishmark + sciencemark + mathsmark

print("=============Student Info=================")
print(f"Student Id: {sid}")
print(f"Student Name: {sname}")
print(f"English Mark: {englishmark}")
print(f"Science Mark: {sciencemark}")
print(f"Maths Mark: {mathsmark}")
print(f"Total Marks: {totalmarks}")
print("==========================================")





