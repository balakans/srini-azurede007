import pandas as pd

#Create Series

data = [2,5,8,7,9]
s = pd.Series(data)
print(s)

#Access data using index from the series
print(s[1])

#Define custom index
s = pd.Series(data,index=[10,15,16,18,24])
print(s[16])


#Get values
print(s.values)

#Get Index
print(s.index)

print("========================")
s = pd.Series(data,index=["A","B","C","D","E"])
print(s["E"])

print("========using loc================")
#Access using .loc[] (label-based)
print(s.loc['B'])
print(s.loc[['B', 'C']])

print("========using iloc ================")
#Access using .iloc[] (position-based)
print(s.iloc[1])
print(s.iloc[[1,2]])  # Multiple positions

s1 = pd.Series(["India","China","United States"],index=["c1","c2","c3"])

print(s1)

print(s1["c1"])
print(s1.loc["c1"])

l = ["c1","c3"]
print(s1.loc[l])
print(s1.iloc[0])

# Slicing (position-based)
print(s1[0:2])

s1 = "Country:" + s1

print(s1)

s1 = pd.Series([10, 20, 30, 40])

#filter
s1 = s1[s1 > 20]
print(s1)


print("=======================")

#From a Python dictionary
data = {'a': 400, 'b': 200, 'c': 300}
s = pd.Series(data)
print(s)

#Access by Label
print(s['a'])

#Sort values
print(s.sort_values())

#Sort values by descending
print(s.sort_values(ascending=False))
