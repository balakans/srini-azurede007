

#Read the file D:\Training\custs and extract only profession and print

cdatafile  = open("D:\Training\custs.txt",mode="r")

cdata = cdatafile.readlines()

flag = False
for l in cdata:
    if flag:
        tmp = l.split(",")
        print(tmp[4])
    flag = True


#using map function

#profdata = list(map(lambda l: l.split(",")[4],cdata)

#print(list(profdata))

pilotdata = list(filter(lambda f : "Pilot" in f, cdata))

print("Pilot Count:",len(pilotdata))

prdata = set(map(lambda l: l.split(",")[4].replace("\n",""),cdata))

print("********************")
print(prdata)



def extractprof(t):
    cust = t.split(",")
    prof = cust[4]
    return prof

profdata = map(extractprof,cdata)

print(list(profdata))


cdatafile.close()

