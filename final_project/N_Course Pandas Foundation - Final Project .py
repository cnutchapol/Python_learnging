# -*- coding: utf-8 -*-

# -- Project --

# # Final Project - Analyzing Sales Data
# 
# **Date**: 30 jan 2021
# 
# **Author**: Nutchapol Chaiyanon
# 
# **Course**: `Pandas Foundation`


# import data
import pandas as pd
df = pd.read_csv("sample-store.csv")

# preview top 5 rows
df.head()

# shape of dataframe
df.shape

# see data frame information using .info()
df.info()

# We can use `pd.to_datetime()` function to convert columns 'Order Date' and 'Ship Date' to datetime.


# example of pd.to_datetime() function
pd.to_datetime(df['Order Date'].head(), format='%m/%d/%Y')


# TODO - convert order date and ship date to datetime in the original dataframe
#df.head()

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%m/%d/%Y')
df['Ship Date']  = pd.to_datetime(df['Ship Date'], format='%m/%d/%Y')
df

# TODO - count nan in postal code column
len(df[df['Postal Code'].isna()])

print(f"the number of nan is postal is {len(df[df['Postal Code'].isna()])}")

# TODO - filter rows with missing values

df[df['Postal Code'].isna()]

# TODO -Count ordey by Segment ,State 
df_seg_sta = df[['Segment','State']].value_counts().reset_index()
df_seg_sta.columns = ['segment','state','order']
df_seg_sta.sort_values('segment')

# ## Data Analysis Part
# 
# Answer 10 below questions to get credit from this course. Write `pandas` code to find answers.


# TODO 01 - how many columns, rows in this dataset
df.info()
print("The numbers of columns is: ",df.shape[1])
print("The numbers of row is: ",df.shape[0])

# TODO 02 - is there any missing values?, if there is, which colunm? how many nan values?
df_missing = df.isna().sum().sort_values(ascending= False)
print(f"the missing values is {df_missing.head(1)}")

# TODO 03 - your friend ask for `California` data, filter it and export csv for him
df_cal = df[df['State'] == 'California' ]
df_cal.to_csv('California_data')

# TODO 04 - your friend ask for all order data in `California` and `Texas` in 2017 (look at Order Date), send him csv file

df['year']= df['Order Date'].dt.year
df.query('State == ["California","Texas"] & year == 2017')





# TODO 05 - how much total sales, average sales, and standard deviation of sales your company make in 2017
df_sale_2017=df.query('year == 2017').agg(['sum','mean','std'])
df_sale_2017['Sales']


# TODO 06 - which Segment has the highest profit in 2018
df.query('year == 2018').groupby(['Segment'])['Profit'].sum()
print(f" the highest profil Segment in 2018 : {df.query('year == 2018').groupby(['Segment'])['Profit'].sum()}")

# TODO 07 - which top 5 States have the least total sales between 15 April 2019 - 31 December 2019

df['Order Date'] = pd.to_datetime(df['Order Date'], format='%Y-%m-%d')
# Filter data between two dates
filtered_df = df.loc[(df['Order Date'] >= '2019-04-15') & (df['Order Date'] < '2019-12-31')]
df_5 =filtered_df.groupby(['State'])['Sales'].agg('sum')
df_5.sort_values(ascending = True).head(5)



# TODO 08 - what is the proportion of total sales (%) in West + Central in 2019 e.g. 25% 
#df['Region'].unique()
proportion_df = df.query('Region == ["West","Central"] & year == 2019')['Sales'].sum() / df.query('year == 2019')['Sales'].sum()
print(f"the proportion of total sales in west and cental : {round(proportion_df *100,1)} %")
#df.query('Region == ["West","Central"] & year == 2019')

# TODO 09 - find top 10 popular products in terms of number of orders vs. total sales during 2019-2020
#df.head()

df_1920 = df.query('year == [2019,2020]')
round(df_1920.groupby('Product Name')['Sales']\
.agg(['count','sum'])\
.sort_values(['sum','count'],ascending = False).head(10),2)

 # TODO 10 - plot at least 2 plots, any plot you think interesting :)

df_region = df.groupby('Region')['Region'].count().sort_values(ascending = False).plot(kind = 'bar',color = 'navy')

df.head()
df.groupby('Category')['Category'].count().sort_values().plot(kind ='area',color = 'yellow')

# TODO Bonus - use np.where() to create new column in dataframe to help you answer your own questions
# find the top 5 product that best seller in Texas 
import numpy as np

df_texas = df.query("State == 'Texas'")[['State','Product Name','Quantity']] 
df_texas['new_column'] = np.where(df_texas['Quantity']> 10,"best seller","normal")
df_texas.sort_values('Quantity',ascending=False)




