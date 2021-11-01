#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Import dependencies 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[13]:


#Read in Data Files
crime_data_path = "COBRA-2009-2019.csv"


# In[14]:


crime_data_df = pd.read_csv(crime_data_path)
crime_data_df.head()


# In[15]:


#Top 3 Crimes in the past ten years
crime_data_df.count()


# In[39]:


average = 342914 / 3650
average


# In[16]:


crime_data_df["UCR Literal"].value_counts()


# In[42]:


#Average crimes per day
len(crime_data_df)


# In[131]:


len(crime_data_df) / 12


# In[130]:


len(crime_data_df) / 365 * 12


# In[108]:


crime_data_df["Report Date"]


# In[110]:


list(crime_data_df["Report Date"])


# In[125]:


crime_data_array = np.array([x.split("-")[0] for x in list(crime_data_df["Report Date"])])
crime_data_array


# In[138]:


crimes = [39395, 35500, 34871, 33405, 32439, 31128, 30087, 29022, 26410, 25627, 25030]
x_axis = np.arange(len(crimes))


# In[139]:


x = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]
y = [28576.166666666668]*len(x)
plt.plot(x, y) 
plt.bar(x_axis, crimes, color='r', alpha=0.5, align="center")


# In[75]:


crimedatelist = np.array(crime_data_df["Report Date"].tolist())


# In[96]:


np.array([x.split("-")[0] for x in crimedatelist])


# In[98]:


crimedatelist


# In[99]:


count_2009 = np.count_nonzero(crime_data_df == "2009")
count_2009 


# In[66]:


years = ["2009", "2010", "2011", "2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019"]
y_axis = np.arange(len(years))


# In[47]:


crime_data_df["UCR Literal"].value_counts()


# In[52]:


crime_data_df["Report Date"].value_counts()


# In[140]:


print("November 17th, 2009 was the most dangerous day, with 170 crimes committed")


# In[141]:


print("February 2nd, 2014 was the least dangerous day, with only 21 crimes being committed")


# In[ ]:




