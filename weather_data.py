# -*- coding: utf-8 -*-
"""Weather_data.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Vn0eKo8LUVXbZaBCqKwxrsK_Hrre3D-S

**(A part of Big data analysis)**

**The weather dataset ** 

Here, the weather dataset is a time-series data set with per-hour information about the weather condition at a particular location. It records Temperature, Dew point temperature, Relative humidity, Wind Speed, Visibility, Pressure and conditions

This data is available as a CSV file. We are going to analyze this data set using the Pandas DataFrame
"""

import pandas as pd

data = pd.read_csv('/content/1. Weather Data.csv')
data

# it shows first N rows in the data (By default, N=5)
data.head()

# it shows the total no. of rows and columns in the dataframe 
data.shape

# this attribute provides the index of the dataframe 
data.index

# it shows the name of each columns 
data.columns

# it shows the data-types of each columns 
data.dtypes

# it shows the total no .of unique values in each column. it can be applied on a single column as well as on whole dataframe
data.nunique()

# in a column, it shows all the unique values, it can be applied on a single column only, not on the whole dataframe 
data['Weather'].unique()

# it shows the total no. of non-null values in each column. it can be applied on a single column as well as on the whole dataframe 
data.count()

# in a column. it shows all the unique values with their count. it can be applied on single column only 
data['Weather'].value_counts()

# provides basic info about dataframe 
data.info()

"""Q) 1. Find all the unique "Wind Speed" values in the data."""

data.head(2)

data.nunique()

data['Wind Speed_km/h'].nunique()

data['Wind Speed_km/h'].unique()

"""Q) 2. Find the number of times when the 'Weather is exactly Clear'."""

data.head(2)

# value_counts()
data.Weather.value_counts()

# filtering 
#data.head(2)
data[data.Weather == 'Clear']

# groupby()
# data.head(2)
data.groupby('Weather').get_group('Clear')

"""Q) 3. Find the number of times when the 'Wind Speed was exactly 4km/h'."""

data.head(2)

data[data['Wind Speed_km/h'] == 4] # Answer

"""Q. 4) Find out all the Null Values in the data."""

data.isnull().sum()

data.notnull().sum()

"""Q. 5) Rename the column name 'Weather' of the dataframe to 'Weather Condition'."""

data.head(2)

data.rename(columns = {'Weather':'Weather Condition'}, inplace = True)

data.head()

"""Q.6) What is the mean 'Visibility' ?"""

data.head(2)

data.Visibility_km.mean()

"""Q. 7) What is the Standard Deviation of 'Pressure' in this data?"""

data.Press_kPa.std()

"""Q. 8) What is the variance of 'relative humidity' in this data?"""

data['Rel Hum_%'].var()

"""Q. 9) Find all instances when 'Snow' was recorded."""

# value_counts()
#data.head(2)
data['Weather Condition'].value_counts()

# Filtering 
data[data['Weather Condition'] == 'Snow']

# str.contains 
data[data['Weather Condition'].str.contains('Snow')]

"""Q. 10) Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'."""

data.head(2)

data[(data['Wind Speed_km/h'] > 24) & (data['Visibility_km'] == 25)]

"""Q. 11) What is the Mean value of each column against each 'Weather Condition'?"""

data.head(2)

data.groupby('Weather Condition').mean()

"""Q. 12) What is the minimum & maximum value of each column against each 'Weather Condition'?"""

data.head(2)

data.groupby('Weather Condition').min()

data.groupby('Weather Condition').max()

"""Q. 13) Show all the Records where Weather Condition is Fog."""

data[data['Weather Condition'] == 'Fog']

"""Q. 14) Find all instances when 'Weather is Clear' or 'Visibility is above 40'."""

data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]

"""Q. 15) Find all instances when:

A. 'Weather is Clear' and 'Relative Humidity is greater than 50'

or

B. 'Visibility is above 40
"""

data.head(2)

data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40)]