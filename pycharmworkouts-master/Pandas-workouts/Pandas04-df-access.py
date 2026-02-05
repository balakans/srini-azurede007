import pandas as pd

df = pd.read_csv("D:\\Training\\pycharmworkouts\Data\\custs.txt")
print(df)

df_name = df['custid']
print(df_name) #Returns a Series
print(type(df_name))

df = df[["custid","fname"]]
print(df)

print("By index using .loc[] (label-based):")
df1 = df.loc[0]  # Row with index label 0
print(df1)

print("By position using .iloc[] (integer position):")
df1 = df.iloc[0]  # First row
print(df1)

print("Slice rows:")
df1 = df[1:4]  # Rows 1 to 3 (like list slicing)
print(df1)

print("===Access Individual Cell -  By label: .loc[row_label, column_label]===")
custid = df.loc[0, 'custid']

print("===Access Individual Cell -  By position: .iloc[row_index, column_index]===")
cusid = df.iloc[0, 0]
print(cusid)


df = pd.read_csv("D:\\Training\\pycharmworkouts\Data\\custs.txt")

prof = df.loc[4,"profession"]
prof = df.iloc[4,4]

print("===filter===")
df1 = df[df['age'] > 25]  # Rows where Age > 25
print(df1)

"""
Using at and iat (Fast single access)
    at is label-based (like loc)
    iat is index-based (like iloc)
"""

strname = df.at[0, 'fname']
print(strname)

strname = df.iat[0, 1]
print(strname)

print("===Using query() for SQL-like filtering===")
#select lname,fname from customer where age > 25 and profession = "Pilot"
df1 = df.query('age > 25 and profession == "Pilot"')
df1 = df1[["lname","fname"]]
print(df1)

#slicing to get rows
#select * from table where rownum between 0 and 3
print(df[0:4])
print(df.head(4))


#Get only custid,age,profession
#select custid,age,profession from tbl where age > 25
df1 = df[["custid","age","profession"]].query("age > 25")
print(df1)

age = df.at[1,"age"]
age = df.iat[1,3]