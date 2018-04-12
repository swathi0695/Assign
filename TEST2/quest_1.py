import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('C:\\Users\\user\\.spyder-py3\\convertcsv.csv')
print(df.columns.values)
#print(x)
print(df.dtypes)
x=df['Model']
print(x[:25])
y=df['Release date']
print(y[:25])
z=df['Price']
print(z[:25])
#summerize 
print(df.describe())
print(df['Price'].mean())
print("\n")
print(df['Price'].median())
print("\n")
print(df['Price'].modex())
item_name=df['Data']
profit=df['Price']

plt.bar(item_name,profit)
plt.title("Bar Graph for Total profit and Item Type")
plt.xlabel("Item Type")
plt.xticks(item_name, fontsize=8,rotation=45)
plt.ylabel("Total Profit")
plt.show()
