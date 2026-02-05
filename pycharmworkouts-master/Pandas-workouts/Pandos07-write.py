import pandas as pd

df = pd.read_csv('D:\\Training\\pycharmworkouts\Data\\TopRichestInWorld.csv',usecols=['Name', 'NetWorth', 'Age','Country/Territory','Industry'])

df.rename(columns={"Country/Territory":"Country"},inplace=True)

df.query("Country == 'India'", inplace=True)

df.to_csv('D:\\Training\\output\\india_toprichest.csv',sep=",", index=False)
df.to_excel('D:\\Training\\output\\india_toprichest.xlsx', index=False)
df.to_html('D:\\Training\\output\\india_toprichest.html', index=False)
df.to_json('D:\\Training\\output\\india_toprichest.json',orient='records',  index=False) #split,index,columns
df.to_string('D:\\Training\\output\\india_toprichest.txt', index=False)

