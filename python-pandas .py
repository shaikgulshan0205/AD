#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns


# In[2]:


df=sns.load_dataset('taxis')
df


# In[3]:


df.sample(10)


# In[4]:


df.tail(10)


# In[6]:


df['color'].isnull()


# In[9]:


df['color'].isnull().sum()


# missing data handling
# 1) Imputation  (fill in the blanks)
#     1) statistical measures
#     2) parameter
#     
# 2)  delete data 
#     rows
#     columns
# 

# In[11]:


df.drop('pickup_zone',axis=1)

