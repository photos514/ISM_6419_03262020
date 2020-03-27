#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
salesMen = ['Ahmed', 'Omar', 'Ali', 'Ziad', 'Salwa', 'Lila']
Mobile_Sales = [2540, 1370, 1320, 2000, 2100, 2150]
TV_Sales = [2200, 1900, 2150, 1850, 1770, 2000]
df = pd.DataFrame()
df ['Name'] =salesMen
df ['Mobile_Sales'] = Mobile_Sales
df['TV_Sales']=TV_Sales
df.set_index("Name",drop=True,inplace=True)
df


# In[7]:


#Create a bar plot of the sales volume
df.plot.bar( figsize=(20, 10), rot=0).legend(bbox_to_anchor=(1.1, 1)) 
plt.xlabel('Salesmen') 
plt.ylabel('Sales')
plt.title('Sales Volume for two salesmen in \nJanuary and April 2017')
plt.show()


# In[10]:


#Create a pie chart of item sales
df.plot.pie(subplots=True)


# In[11]:


#Create a box plot of item sales
df.plot.box()


# In[12]:


#Create an area plot of item sales.
df.plot.area(figsize=(6, 4)).legend(bbox_to_anchor=(1.3,1))


# In[15]:


#Create a stacked bar plot of item sales.
df.plot.bar(stacked=True, figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[ ]:




