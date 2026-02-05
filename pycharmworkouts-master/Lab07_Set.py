"""
A set is an unordered collection of items.
Set itself is mutable. We can add or remove items from it.
Every element is unique (no duplicates)
Every element inside a set must be immutable can’t put lists or dictionaries inside a set, 
but you can put tuples, numbers, or strings).

In Python sets are written with curly brackets.
"""

a = {10,20,30,60,89,20,10}

print(a)

lst = [10,20,30,60,89,20,10]

print(lst)

#remove duplicates from the list
print(list(set(lst)))

tup = (10,20,30,60,89,20,10)
#remove duplicates from the tuple
print(tuple(set(lst)))

a = {1.0, "Hello", (1, 2, 3)}

print(a)

#Add element to the set
a.add(2)

print(a)


#add muliple elements
a.update([10,20,30])

print(a)
print("==================")
# we cannont have list inside the set
#a1 = {10,20,30,[1,2,3]}

# we cannont have dict inside the set
#a1 = {10,20,30,{"india":"new delhi"}}


a = {35,90,100,40}

a.remove(100)

print(a)

a.remove(90)

print(a)
#even element not there in the set, no error
a.discard(60)

#defining empty types
a = [] # list

a = [10,20,30]

print(type(a))

a = () # tuple
a = (10,20,30)
print(type(a))

a = {} # dict
a = {1:10,2:20,3:30}
print(type(a))

a1 = set() # set

if len(a1) == 0:
    print("No Elements")


a = {10,20,30}
print(type(a))

