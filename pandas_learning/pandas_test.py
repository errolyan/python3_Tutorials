# -*- coding:utf-8 -*-
# /usr/bin/python
'''
@Author:  Yan Errol  
@Email:2681506@gmail.com   
@Date:  2019-05-29  09:16
@File：pandas_test.py
@Describe:pandas
'''

import pandas as pd
import numpy as np

data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
       'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
       'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
       'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(data,index = labels)
#print("df",df,type(df),id(df))
print(df.iloc[:,:3])
print(id(df.head(3)) , id(df.iloc[:3]) )

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),columns=['a', 'b', 'c'])
print("df2\n",df2,type(df2))

df3 = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv', chunksize=50)
df3 = pd.DataFrame()
print(df3)