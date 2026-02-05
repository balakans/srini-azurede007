"""
Comprehensions in Python provide a short and concise way to construct new sequences
(such as lists, set, dictionary etc.) from existing iterables.
They are more readable and faster than traditional loops.

When we want concise, readable, and fast transformations of iterables.

Avoid if they get too complex (use normal loops for clarity).


#1. List Comprehensions
#A quick way to create lists.

lst = [10,20,30,40]

lst1 = []

for i in lst:
    lst1.append(i + 10)
print(lst1)


#List comprehension
lst1 = [i+10 for i in lst]
#syntax [return_value for_loop]

print(lst1)

lst = [35,21,10,34,52,90,71]


lst1 = []

for i in lst:
    if i % 2 == 0:
        lst1.append(i)

print("====Even number list=======")
print(lst1)

lst1 = [i for i in lst if i%2 == 0]

#syntax [return_value for_loop if_condition ]
print(lst1)


lst1 = ["even" if i%2 == 0 else "odd" for i in lst ]

#syntax: [return_true if_condition else return_false for_loop]
print(lst)
print(lst1)


#genertor
'''
Look like list comprehensions but use () instead of [].
They create a generator (lazy evaluation, saves memory).
'''

lst = [35,21,10,34,52,90,71]
lst1 = ("even" if i%2 == 0 else "odd" for i in lst )

print("==========================")
print(tuple(lst1))

"""

#Dictionary comprehension
lst = [35,21,10,34,52,90,71]
lst1 = {k:v for k,v in enumerate(lst)}

print(lst1)

lst1 = {}
for k,v in enumerate(lst):
    lst1[k] = v

print(lst1)


print("======Dict Comprehension=====")
lst1 = {k:k*k for k in lst }

print(lst1)

print("======Set Comprehension=====")
lst1 = {k*k for k in lst }

print(lst1)



print("=======Enumerate===========")
lst = ["Orange","Apple","Mango"]
for indx,value in enumerate(lst):
    print(indx)
    print(value)
