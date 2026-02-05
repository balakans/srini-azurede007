
#For loop on collection

lst = [10,15,22,30,75]

"""
for n in lst:
    print(n)
"""


for n in lst:
    #print("Even Number:",n) if n % 2 == 0 else print("Odd Number:",n)
    if n % 2 == 0:
        print("Even Number:", n)
    else:
        print("Odd Number:", n)




fruits = ("apple","orange","mango")

print("=======================")
for f in fruits:
    print(f)


print("************************")

for i,f in enumerate(fruits):
    print("Index:",i,"value:",f)

print("***********************")


print("============")
for i in range(len(fruits)):
    print("Index:",i,"value:",fruits[i])



print("============Dict in for loop================")

countries = {"India": "New Delhi", "China": "Beijing", "USA": "Washington", "Australia": "Canberra"}

for l in countries.items():
    print(f"Country:{l[0]},Capital: {l[1]}")


fruits = {"apple","orange","mango"}

print("=======Set in loop================")
for f in fruits:
    print(f)


