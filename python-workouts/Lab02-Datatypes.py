"""Dats Types

int – n:int = 10

A float in Python is an immutable data type that represents real numbers with decimal points,
supporting both positive and negative values.
supports 15 decimal points
float – score:float = 3.14

str – name: = "hello"


bool –  True, False

flag:bool = True

datatype conversions:
x = int("10")       # from str
y = int(3.7)        # from float → 3

Convert to float:
x = float("10.5")   # from str
y = float(5)        # from int → 5.0

Convert to str
x = str(123)        # from int → "123"
y = str(3.14)       # from float → "3.14"

Convert to bool
bool(0)      # False
bool(1)      # True
bool("")     # False
bool("hi")   # True

"""

n:int = 10

print(type(n))

n = "inceptez"

print(n)

print(type(n))


r = 10

print(type(r))

# Convert to Integer
s = "450"

x = int(s)

#Float datatype

#upto 15 decimal points
f = 10.25
f1 = float(s)
print(f1)

#====String=====
s1 = "Inceptez Technologies"
s2 = 'Inceptez Technologies'

s3 = "'Inceptez' Technologies"
print(s3)

s4 = '"Inceptez" Technologies'
print(s4)

s5 = "Inceptez \"Technologies\""

print(s5)


# Boolean

a = True
a1 = False


a = 10

a = ""

x = bool(a)
print(x)
