"""
Tuple is another data type which is a sequence of data similar to list. But it is immutable.
Data in a tuple is written using parenthesis and commas.
"""

a = (10,20,30)

#Access element from the tuple
n = a[1]
print(n)

n = ("Spark",100,12.5,True)

#Access the value from the tuple

#To get the first element in the tuple
print(n[0])
#Output:Spark

#To get the last element in the tuple
print(n[-1])
#Output:True

studinfo = ("1001","Rajesh",90,89,97)

#To get marks
print(studinfo[2:])
#Output:[90, 89, 97]

print(studinfo[-3:])
#Output:[90, 89, 97]

#Tuple is immutable

#studinfo[1] = "Karthik"

print(studinfo)

#Does not support append,insert,remove elements in the tuple
#studinfo.append("A")

num = (25,30,55,89,90)

print("Maximum value=",max(num))
#Output: Maximum value: 90

print("Minimum value=",min(num))

print(f"Minimum value= {min(num)}")

print(f"Sum of all values= {sum(num)}")

n = (10,20,2,100,40)

#To get number of elements in the list
print(len(n))
#Output:5

#sort the tuple
print(sorted(n))
#Output=[2, 10, 20, 40, 100]

#sort the tuple
print(sorted(n,reverse=True))
#Output:[100, 40, 20, 10, 2]

empdata = (5001,"Irfan","Manager",["23,Newstree","Chennai","India"])

print(empdata[3][2])
#Output:India

empdata1 = [5001,"Irfan","Manager",("23,Newstreet","Chennai","India")]

print(empdata1[3][2])
#Output:India

empdata1[3][2] = "China"

print(empdata1)

#It fails because the element inside the list is tuple
#empdata1[3][2] = "China"

#Convert tuple to a list
studinfo = ("1001","Rajesh",90,89,97)

studinfo1 = list(studinfo)

print(studinfo1)

studinfo2 = tuple(studinfo1)

print(studinfo2)


