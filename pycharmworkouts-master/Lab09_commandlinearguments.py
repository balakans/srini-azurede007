
from sys import argv

#argv is list type

filename = argv[0]

print("First Argument:",filename)

a = int(argv[1])
b = int(argv[2])

print(f"Sum of {a} and {b} is {a+b}")

