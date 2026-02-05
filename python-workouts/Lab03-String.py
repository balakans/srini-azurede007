
"""
The string is a sequence of characters.
Generally, strings are represented by either single or double quotes.

"""

s = "Inceptez Technologies"

a = 'Inceptez'

b = "123"

d = '345.67'

f = "True"

s1 = "Inceptez"

s2 = "Technologies"

# Concatnate
s3 = s1 + s2

print(s3)

s3 = "Inceptez" "Technologies"

print(type(s3))

print(s3)

n = 123
s1 = "Inceptez"
s2 = "Technologies"

print(s1)
print(s2)
"""
Output:
Inceptez
Technologies
"""

print(s1,end="$")
print(s2)
#Output: Inceptez$Technologies

print(s1,s2,"Chennai",n)
#Output: Inceptez Technologies Chennai 123

print(s1,s2,"Chennai",end="")
print("TN India")



strdata = "this IS test Data"

print("Convert to Upper Case:",strdata.upper())



print("Check upper:",strdata.isupper())

strdata1 = strdata.upper()

print("Check upper:",strdata1.isupper())

print("Convert to lower Case:",strdata.lower())

print("Check lower:",strdata.islower())

print("Check numeric:",strdata.isnumeric())

print(strdata.isalpha())

print(strdata.isalnum())


print("Length of the string is", len(strdata))


print("===============")
strdata = "this IS test Data"

print("get no of occurances:",strdata.count("s"))

print("Starts with :",strdata.startswith("r"))

print("Ends with :",strdata.endswith("a"))



strdata = "this IS test Data"

s1 = strdata.split(" ")


print("Split Output:",s1)

s2 = "".join(s1)

print("Joining the string into one single string:", s2)



empdata = "1001,Karthik,Manager,Hyderabad"

empinfo = empdata.split(",")

print(empinfo)
print("Empid:" ,empinfo[0])
print("EmpName:",empinfo[1])
print("EmpDesignation:",empinfo[2])
print("EmpCity:",empinfo[3])



print(empinfo)

print("Emp city:",empinfo[3])


studdata="Stud101#Kavi#90#98#80"

studinfo = studdata.split("#")

print("Student Name:",studinfo[1])


"""

STRING SLICING
Slicing allows you to grab a subsection of multiple characters, a “Slice” of the string. 
This has the following syntax:


[start:stop:step]
"""

orgname = "Inceptez"

print("Index 0:",orgname[0])
print("Index 1:",orgname[1])
print("Index 2:",orgname[2])
print("Index 3:",orgname[3])
print("Index 4:",orgname[4])
print("Index 5:",orgname[5])
print("Index 6:",orgname[6])
print("Index 7:",orgname[7])

"""

0  1  2  3  4  5  6  7     -> Postive
I  n  c  e  p  t  e  z
-8 -7 -6 -5 -4 -3 -2 -1    -> Negative

"""

print("Lsst Character:",orgname[-1])
print("First Character:",orgname[0])

n = len(orgname)
print("Length of the String:",n)
print("Extract first 4 character using postive index:", orgname[0:4])
print("Extract first 4 character using negative index:", orgname[-8:-4])
print("Extract first 4 character using postive index:", orgname[:4])
print("Extract last 4 character using postive index:", orgname[-4:])


print(orgname[0:4])
#Output:Ince

print(orgname[:4])
#Output:Ince

print(orgname[-8:-4])
#Output:Ince

print(orgname[1:5])
#Output:ncep

print(orgname[-7:-3])
#Output:ncep


print(orgname[1:])
#Output:nceptez





#I  n  c  e  p  t  e  z
print(orgname[0::2])
#Output:icp

print("=========")
print(orgname[:])
print(orgname[::])
print(orgname[::1])
print("=========")


#Reverse the string
print("Reverse of the String:",orgname[::-1])


str = "Learning python"

print(str[::2])
#Output:Lann yhn

print(str[::3])
#Output:Lrnph

print(str[1::2])

#Output:erigpto

print(str[-14::2])
#Output:erigpto


str1 = "Messi is the best soccer player. soccer is popular game"

str2 = str1.find("soccer")
print(str2)
#Output:18


print(str1.index("soccer"))
#Output:18


print(str1[str1.index("soccer")::])
#Output:soccer player

print("soccer" in str1)
#Output:True
print("soccer" not in str1)
#Output:False


print("========================")


#Format

l1 = "Java"
l2 = "Scala"
l3 = "Python"
l4 = "R"


print("Spark supports languages like Java , Scala , Python , R")

print("Spark supports languages like" , l1 , ",",l2 , ",",l3 , ",",l4)

r = "Spark supports languages like " + l1 + " , " + l2 + " , " + l3 + " , "+ l4
print(r)

r1 = "Spark supports languages like {} , {} , {} , {}".format(l1,l2,l3,l4)
print(r1)

r2 = "Spark supports languages like {0} , {1} , {2} , {3}".format(l1,l2,l3,l4)
print(r2)

r3 = f"Spark supports languages like {l1} , {l2} , {l3} , {l4}"
print(r3)


a = 10
b = 20

c = a + b

print(f"Sum of {a} + {b} = {a+b}")
#Output: Sum of 10 + 20 = 30


n1 = "Hadoop"
n2 = "Sqoop,Hive,HBase,oozie"

n3 = f"Tools like {n2} are eco-system of {n1}"

print(n3)

#================Multipl-Line Strings==================

#If we need a string to span multiple lines then we can use triple quotes.




s1 = """Python language is easy to learn.
       It support multiple 
       programming paradigm.
Its an interpreted language"""


print(s1)

#String is Immutable(not changable)

s1 = "Inceptez"


print(id(s1))

s1 = "Azure Databricks".replace("a","z")

print(id(s1))

print(s1[0])

#s1[0] = "Z"
#update string is not supported because string are immutable in python

print(s1)





















