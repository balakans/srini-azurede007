"""
1. open the file
2. read/write the content of file
3. close the file

"""

#default mode = 'r'
f = open("D:\Training\data.txt")
content = f.read()
print(content)
f.close()



custfile = open("D:\Training\cust.txt",mode="r")
#Entire filecontent stored in string
custdata = custfile.read()
print(custdata)

#reset the cursor position to 0
custfile.seek(0)
custdata = custfile.read()
print(custdata)

print("==========================")

custfile.seek(0)
#filecontent is converted into list and get stored
custdata = custfile.readlines()

print(custdata)

custfile.close()

pdata = list(map(lambda s : s.replace("\n",""),custdata))

print(pdata)

fdata = list(filter(lambda x: True if ".com" in x else False, custdata))

print(fdata)

