import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#reading the file 
df=pd.read_excel('C:\\Users\\user\\.spyder-py3\\100s.xlsx')

#printing  column names 
print(df.columns)
print("\n")
cost=df['Total Profit']
item=df['Item Type']
unit_sold=df['Units Sold']

plt.bar(item,unit_sold)
plt.ylabel("unit_sold")
plt.xlabel("item")
plt.xticks(item,rotation=60)
plt.show()

