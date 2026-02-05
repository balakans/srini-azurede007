import pandas as pd

#From text file
df = pd.read_csv('D:\\Training\\pycharmworkouts\Data\\custs.txt', delimiter=',')
print(df['profession'].unique())

print("===Frequency For Each Value===")
print(df['profession'].value_counts())

print(df["age"].mean())
print(df["age"].median())
print(df["age"].sum())
print(df["age"].min())
print(df[["custid","age"]].max())
print("===Cleaning Functions===")



#Remove rows with NaN
dfemp = pd.read_csv("D:\\Training\\pycharmworkouts\Data\\emp.csv")
print(dfemp)
dfemp1 = dfemp.dropna()
print(dfemp1)

#Replace NaN with value
dfemp1 = dfemp.fillna(0)
print(dfemp1)

fvalue = {"empsalary": 0, "empcity": "NA"}
dfemp1 = dfemp.fillna(value=fvalue)
print(dfemp1)


df = pd.read_csv("D:\\Training\\pycharmworkouts\Data\\txns.csv",
                 names=["txnid", "txndate", "custid", "amount", "category","product","city","state","paytype"],
                 header=None)

#Total Transactions
print("Total Records:", df.shape[0])

#select txnid,txndate,amount,state from tnxs
df1 = df[["txnid","txndate","amount","state"]]

#select txnid,txndate,amount,state from tnxs where amount > 50

df1 = df1.query("amount > 50")

#select state, count(*) as cnt from txns where amount > 50 group by state

df1 = df1.groupby("state").size()

df.groupby('state').reset_index(name="cnt").size()

#select city,state, sum(amount) as total_amount,count(txnid) as txn_count from txns group by city,state order by txn_count desc
df = (df.groupby(["city", "state"])
      .agg(txn_count=("txnid", "count"),total_amount=("amount", "sum"))
      .query("txn_count > 10")
      .reset_index()
      .sort_values(by="txn_count", ascending=False))

#Sorting
df.sort_values("state")

df.sort_values("state", ascending=False)

#seelct * from txns order by amount desc, city, state desc
df.sort_values(["amount", "city", "state"], ascending = [False, True, False], inplace = True)

#Add columns
df['country'] = "United States"

#Rename columns
df.rename(columns={'country': 'Region'},inplace=True)

#rename multiple columns
df.rename(columns={'Region': 'region',"amount":"amt"},inplace=True)

#Drop row with index 2
df1 = df.drop(0).reset_index()

#drop multiple rows
df.drop([1, 3], inplace=True)

#drop column
df1 = df.drop('ptype', axis=1)

#drop multiple columns
df1 = df.drop(['paytype','category','product'], axis=1)

df['state'] = df['state'].str.upper()

df['txnid'] = df['txnid'].apply(lambda x: x+1)

def incr(i):
    return i + 1

df['txnid'] = df['txnid'].apply(incr)

"""
TEXAS = 2
CALIFORNIA = 3
NEW YORK = 4
WASHINGTON = 5
Other = 1
"""

def calc_discount(state):
    disc = 0
    if state == "TEXAS":
        disc = 1
    elif state == "CALIFORNIA":
        disc = 2
    elif state == "NEW YORK":
        disc = 3
    else:
        disc = 4
    return disc


df["discount"] = df['state'].apply(calc_discount)
