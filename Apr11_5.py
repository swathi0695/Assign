import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statistics import mode
from collections import Counter

#reading the file 
df=pd.read_excel('C:\\Users\\user\\.spyder-py3\\Book1.xlsx')
print(df.describe())
unit_price=df['Unit price']
meanx=np.mean(unit_price)
print("Mean of unit price : %d " % meanx)
print("Median of unit price : %d " % np.median(unit_price))
print("Mode of unit price : " ,Counter(unit_price))

#
print(type(df.values[0]))
print(df.dtypes)

name=df['Name'+'Ext price']
ext=df['Ext price']
print(name,ext)

ws = wb.active
first_column = ws['A']

# Print the contents
for x in xrange(len(first_column)): 
    print(first_column[x].value)