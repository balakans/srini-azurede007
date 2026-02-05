
lst = [10,20,30]

lst1 = []

for i in lst:
    lst1.append(i + 2)

print("Using For Loop:",lst1)

#list comprehension

lst1 = [ i+2 for i in lst ]

print("Using Comprehension:",lst1)

#using map and lambda function

lst1 = map(lambda x: x+2,lst)

print(type(lst1))
print("Using Map",list(lst1))



def func1(n):
    return n + 2

lst1 = map(func1,lst)

print("Calling function:",list(lst1))

l = [12,45,36,57,90]
#Output: ["Even","Odd","Even","Odd","Even"]

r = map(lambda a : "Even" if a % 2 == 0 else "Odd" ,l)

print(list(r))

def checkoddoreven(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

r = map(checkoddoreven,l)
print(list(r))

l1 = [4,10,3,8]

def findfact(x):
    f = 1
    for i in range(2,x + 1):
        f = f * i
    return f

r1 = map(findfact,l1)

print(tuple(r1))


l1 = [10,20,30]
l2 = [5,10,20]

r2 = map(lambda x,y : x + y,l1,l2)

print(list(r2))

def addnum(m,n):
    return m + n

r2 = map(addnum,l1,l2)

print(list(r2))


#filter

print("================================")

lst = [25,10,11,20,7]

lst1 = []

for i in lst:
    if i % 2 == 1:
        lst1.append(i)

print(lst1)

#List comprehension

lst1 = [i for i in lst if i % 2 == 1]

print(lst1)

lst1 = filter(lambda x:  x % 2 == 1,lst)

print(list(lst1))


def checkodd(n):
    if n %2 == 1:
        return True
    else:
        return False

lst1 = list(filter(checkodd,lst))

n= 10
print(type(n))
print(type(lst1))
print(lst1)
print(lst1)




