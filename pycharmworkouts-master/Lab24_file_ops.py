import os

from os import path
import time

fileexist = os.path.exists("D:\Training\data1.txt")
print(fileexist)


#Create Directory
if os.path.exists("D:\Training\python1"):
    print("Directory Already Exists")
else:
    os.mkdir("D:\Training\python1")
    print("Directory Created")


#check its a directory
print(os.path.isdir("D:\Training\cust.txt"))
print(os.path.isdir("D:\Training"))


print("============================")
#check its a file
print(os.path.isfile("D:\Training\cust.txt"))
print(os.path.isfile("D:\Training"))


print("============================")

#Delete the file
if os.path.exists("D:\Training\data1.txt"):
    os.remove("D:\Training\data1.txt")
    print("File deleted")


#Delete the directory
print("============================")
os.rmdir("D:\Training\python1")
print("Folder deleted")


#Get the current directory of the file
print("============================")
print(os.getcwd())

print("============================")
#Get the path of the current file
print("File Path:", __file__)



#List the files in the directory D:\Training\pycharmworkouts
print("============================")

lst = os.listdir(os.getcwd())


for f in lst:
    print(f)

#Get file properties
prop = os.stat( "D:\Training\custs.txt")

print("============================")

print("File Size:", prop.st_size, "bytes")
print("Last Modified:", time.ctime(prop.st_mtime))
print("Last Accessed:", time.ctime(prop.st_atime))
print("Created:", time.ctime(prop.st_ctime))
print("Permissions (mode):", prop.st_mode)

