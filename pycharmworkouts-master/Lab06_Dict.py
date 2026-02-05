"""
Python Dictionary is an unordered sequence of data of key-value pair form.
It is similar to Map or hash table type.
Dictionaries are written within curly braces in the form key:value
Dictionary is a mutable datatype
Keys must be unique and immutable (e.g., strings, numbers, tuples).
Values can be of any data type and can be duplicated.
Syntax: {key: value, key: value}
"""

countries = {"India":"New Delhi"}

countries = {1 :"New Delhi"}

countries = {"India":True}


print(countries["India"])



empinfo = [1001,"srini","software","chennai"]

d_empinfo = {"empid":100,"empname":"srini","empdes":"software","empcity":"chennai"}


marks = {"english":95,"maths":100,"science":67}

studdata = [{"english":95,"maths":100,"science":98},marks]

print(studdata)

print("English mark is ", marks["english"])



marks["english"] = 99
marks["science"] = 100

print(marks)
print(studdata)

print("=================================")

countries = {"India":"New Delhi","USA":"Washington"}

print(countries.keys())

print(list(countries.keys()))

print(list(countries.values()))

print(tuple(countries))

print(tuple(countries.values()))

mysql_con = {"server":"78.34.56.190","port":1433,"username":"admin","password":"admin","dbname":"empdb","table":"tblemp"}

print("ServerName:",mysql_con["server"])

countries = {"India":"New Delhi","USA":"Washington"}

print(list(marks))


#append the element(if key exists then update else add)

countries["UK"] = "Berlin"

print(countries)



countries["UK"] = "London"

print(countries)

print("=================================")
#remove element from the dict


#print(countries["China"])

print(countries.get("China"))

print(countries.get("China","Not exists"))

emp = {1:"a","x":"b",3:"c"}


print(emp[1])

print(emp["x"])





#==============
studdata = {"stud1": {"english":95,"maths":100,"science":98}, "stud2": {"english":91,"maths":94,"science":92}}

studdata["stud1"]["social"] = "78"
studdata["stud2"]["social"] = "89"

print(studdata)




