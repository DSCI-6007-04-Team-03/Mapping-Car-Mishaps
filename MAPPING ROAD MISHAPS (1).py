#!/usr/bin/env python
# coding: utf-8

# ##### Step 1 : Download the dataset and pre-process/clean it using Pandas and Numpy

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


accident_dataset = pd.read_csv("US_Accidents_March23.csv")


# In[3]:


accident_dataset.head()


# In[4]:


accident_dataset.shape


# In[5]:


accident_dataset.info()


# In[6]:


accident_dataset.describe()


# In[7]:


numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
numeric_dataset = accident_dataset.select_dtypes(include=numerics)
print(numeric_dataset.shape)
numeric_dataset


# In[8]:


accident_dataset.isnull().sum().sort_values(ascending=False)


# In[9]:


missing_val = accident_dataset.isnull().sum().sort_values(ascending=False)/len(accident_dataset) * 100
missing_val[missing_val>0]


# In[10]:


pip install missingno


# In[11]:


import missingno as msn
msn.bar(accident_dataset)


# In[12]:


accident_dataset['Weather_Condition'].isnull().sum()


# In[13]:


cities = accident_dataset['City']
cities


# In[14]:


unique_cities = cities.unique()
print("The number of unique cities where accidents have taken place in USA: ",len(unique_cities))
unique_cities


# In[15]:


unique_city_count = cities.value_counts()
unique_city_count


# In[16]:


print("The Top 10 Cities of USA with highest number of accidents are:")
unique_city_count[:11]


# In[17]:


unique_city_count[:20].plot(kind='barh')


# In[18]:


percent_moreThan1000 = len(unique_city_count[unique_city_count>1000]) / len(unique_city_count) * 100
print("The percentage of cities have more than 1000 accidents in a year is: ", percent_moreThan1000, " which is less than 5%")


# In[19]:


high_accident_cities = unique_city_count[unique_city_count>1000]
sns.distplot(high_accident_cities)


# In[20]:


one_accident_cities = unique_city_count[unique_city_count == 1]
one_accident_cities
print(len(one_accident_cities))


# In[21]:


accident_dataset['Start_Time']


# In[22]:


accident_dataset['Start_Time'] = pd.to_datetime(accident_dataset['Start_Time'])
accident_dataset['Start_Time']


# In[23]:


accident_dataset['Start_Time'].dt.hour


# In[24]:


sns.distplot(accident_dataset['Start_Time'].dt.hour)


# In[25]:


accident_dataset['Start_Time'].dt.hour.value_counts()


# In[26]:


accident_dataset['Start_Time'].dt.dayofweek.value_counts()
#The day of the week with Monday=0, Sunday=6.


# In[27]:


sns.distplot(accident_dataset['Start_Time'].dt.dayofweek)


# In[28]:


state_wise_counts= accident_dataset['State'].value_counts()[:20]
state_wise_counts


# In[29]:


state_wise_counts[:11].plot(kind='barh')


# In[30]:


list(zip(accident_dataset['Start_Lat'],accident_dataset['Start_Lng']))[:10]


# In[31]:


pip install folium


# In[32]:


from folium import plugins
from folium.plugins import HeatMap


# In[34]:


import folium
from folium.plugins import HeatMap

# Assuming accident_dataset is a DataFrame with 'Start_Lat' and 'Start_Lng' columns

# Create a folium map centered at a specific location or use the default settings
mapWorld = folium.Map()

HeatMap(list(zip(accident_dataset['Start_Lat'], accident_dataset['Start_Lng']))).add_to(mapWorld)

mapWorld


# In[ ]:




