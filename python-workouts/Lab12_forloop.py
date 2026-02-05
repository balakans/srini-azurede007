"""
i = 0
while i < 5:
    print("Learning Azure Bricks in inceptez", i)
    i = i + 1

print("======================")


for n in range(5):
    print("Learning Azure Bricks in inceptez",n)



print("=============")
for i in range(5,10):
    print("Learning bigdata in inceptez", i)
print("=============")

for i in range(5,10,2):
    print("Learning bigdata in inceptez", i)

print("=============")
for i in range(5,n,2):
    print("Learning bigdata in inceptez", i)

"""


#Find the summation of the given number
n  = int(input("Enter Number:"))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(f"Summation of {n} is {sum}")



#find the factorial of a given number using while loop

# 5! = 1 * 2 * 3 * 4 * 5

fact = 1
for c in range(1, n+1):
    fact = fact * c

print(f"factorial of {n} is {fact}")

"""
5

2 to 4

5 % 2 == 0 = False
5 % 3 == 0 = False
5 % 4 == 0 = False

"""
#Find the given number is  prime or not
isprime = True
for counter in range(2,n):
    print("Value of counter is :", counter)
    if n % counter == 0:
        print("Given number is not prime")
        isprime = False
        break

print(f"The given number {n} is prime number:{isprime}")


