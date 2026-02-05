
# while statement

"""
while <expression>:
    statements
"""

#print 0 to 100

"""
cnt = 0

while cnt <= 5:
    print(f"Value:{cnt}")
    cnt = cnt + 1
print("Completed")


#find the summazation of given number

# = 1 + 2 + 3 + 4 + 5
n = int(input("Enter the value to find the summation:"))
cnt = 1
sum = 0

while cnt <= n:
    print(f"{cnt} + {sum} = {cnt + sum}")
    sum = sum + cnt
    cnt = cnt + 1

print(f"Summation of {n} is {sum}")



x = input("Enter Value1:")
y = input("Enter Value2:")


while not (x.isnumeric() and y.isnumeric()):
    print("=====================")
    print("Invalid Input..Enter Integer Value..")
    x = input("Enter Value1:")
    y = input("Enter Value2:")

x = int(x)
y = int(y)

if x > y:
    print(f"Greatest Value is {x}")
elif x < y:
    print(f"Greatest Value is {y}")
else:
    print("Both are Equal")

"""