
"""
#Nested loop
for i in range(1,3):
    print(f"i value:{i}")
    for j in range(1,3):
        print(f"\tj value:{j}")
        for k in range(1,3):
            print(f"\t\tk value:{k}")





print("================Table format using for loop=======")
n = 5
for i in range(1,n+1):
    print(f"{n} * {i} = {n*i}")

"""


print("================Table from 1 to n using for loop=======")
n = 5

for i in range(1,n+1):
    print(f"=====Table:{i}=======")
    for j in range(1,n+1):
        print(f"{i} x {j} = {i*j}")

