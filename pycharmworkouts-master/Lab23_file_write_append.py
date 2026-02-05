
#To Write into the file
f = open("D:\Training\data1.txt",mode="w")
f.write("Python is a high level programming language\n")
f.write("Its a multi purpose programming language\n")
f.close()
print("Content written into the file")


#To append into the file
file = open("D:\Training\data1.txt",mode="a")
file.write("Python is a high level programming language - append\n")
file.write("Its a multi purpose programming language - append")
file.close()
print("Content appended into the file")



#To read the content of the file
file = open("D:\Training\data1.txt",'r')
data = file.read()
file.close()
print(data)


with open("D:\Training\data1.txt",'r') as file:
    data = file.read()

print("===============")
print(data)



with open("D:\Training\data1.txt","a") as f:
    f.write("Python is a high level programming language - append\n")
    f.write("Its a multi purpose programming language - append")

print("Content appended into the file")


