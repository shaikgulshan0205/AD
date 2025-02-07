#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels.formula.api


# In[2]:


cars = pd.read_csv('cars.csv')
cars.head()


# In[3]:


cars.info()


# In[4]:


cars.describe()


# In[5]:


cars.isna().sum()


# In[6]:


import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[8]:


sns.displot(x=cars['HP'])
plt.show()


# In[9]:


sns.displot(x=cars["MPG"])
plt.show()


# In[10]:


sns.displot(x=cars["VOL"])
plt.show()


# In[11]:


sns.displot(x=cars["SP"])
plt.show()


# In[12]:


sns.displot(x=cars["WT"])
plt.show()


# In[13]:


sns.scatterplot(x=cars['HP'],y=cars['MPG'])
plt.show()


# In[14]:


sns.scatterplot(x=cars['HP'],y=cars['VOL'])
plt.show()


# In[15]:


sns.scatterplot(x=cars['HP'],y=cars['SP'])
plt.show()


# In[16]:


sns.scatterplot(x=cars['HP'],y=cars['WT'])
plt.show()


# In[17]:


sns.scatterplot(x=cars['VOL'],y=cars['HP'])
plt.show()


# In[18]:


sns.scatterplot(x=cars['VOL'],y=cars['MPG'])
plt.show()


# In[19]:


sns.scatterplot(x=cars['VOL'],y=cars['SP'])
plt.show()


# In[20]:


sns.scatterplot(x=cars['VOL'],y=cars['WT'])
plt.show()


# In[21]:


sns.scatterplot(x=cars['SP'],y=cars['HP'])
plt.show()


# In[22]:


sns.scatterplot(x=cars['SP'],y=cars['MPG'])
plt.show()


# In[23]:


sns.scatterplot(x=cars['SP'],y=cars['VOL'])
plt.show()


# In[24]:


sns.scatterplot(x=cars['SP'],y=cars['WT'])
plt.show()


# In[25]:


sns.scatterplot(x=cars['SP'],y=cars['WT'])
plt.show()


# In[26]:


sns.scatterplot(x=cars['MPG'],y=cars['HP'])
plt.show()


# In[27]:


sns.scatterplot(x=cars['MPG'],y=cars['VOL'])
plt.show()


# In[28]:


sns.scatterplot(x=cars['MPG'],y=cars['SP'])
plt.show()


# In[29]:


sns.scatterplot(x=cars['MPG'],y=cars['WT'])
plt.show()


# In[ ]:




