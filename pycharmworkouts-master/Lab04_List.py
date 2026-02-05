"""
A list is a collection which is ordered and changeable/Mutable.
In Python lists are written with square brackets.
"""

a = 10
b = 20
c = 25

n = [10,20,25]

print(type(n))

#List can store hetrogeneous datatypes

n = ["Spark",100,12.5,True]

#Access the value from the list

#To get the first element in the list
print(n[0])
#Output:Spark

s1 = n[0]
s2 = n[1]
s3 = n[2]
s4 = n[3]



#To get the last element in the list
print(n[-1])
#Output:True


studinfo = ["1001","Rajesh",90,89,97]




#To get marks
print(studinfo[2:])
#Output:[90, 89, 97]

print(studinfo[-3:])
#Output:[90, 89, 97]


#List is mutable

studinfo[1] = "karthik"

print(studinfo)

#To add new element
studinfo.append("Chennai")

print(studinfo)
#Output: ['1001', 'Karthik', 90, 89, 97, 'Chennai']

#To remove element
studinfo.remove("Chennai")


print(studinfo)
#Output: ['1001', 'Karthik', 90, 89, 97]


#Remove element by using index value
studinfo.pop(2)
studinfo.pop(2)
studinfo.pop(2)
print(studinfo)
#Output:['1001', 'Karthik']

studinfo.insert(0,"PSBB School")

print(studinfo)


num = [25,30,55,89,90]

print("Maximum value=",max(num))
#Output: Maximum value: 90

print(f"Minimum value= {min(num)}")

print(f"Sum of all values= {sum(num)}")




#Empty list
lst1 = []

lst1.append("Tiger")
lst1.append("Elephant")
lst1.insert(1,"Lion")

print(lst1)

n = [10,20,2,100,40]

#To get number of elements in the list
print("No of elements in the list is",len(n))
#Output:5

#sort the list
print("Sorted list",sorted(n))
#Output=[2, 10, 20, 40, 100]

#sort the list
print("Sorted list in Descending",sorted(n,reverse=True))
#Output:[100, 40, 20, 10, 2]

empdata = [5001,"Irfan","Manager",["23,Newstreet","Chennai","India"]]

print(empdata[3][2])
#Output:India



