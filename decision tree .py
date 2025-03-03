#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install streamlit


# In[3]:


## import libraries
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,roc_auc_score,confusion_matrix


# In[9]:


### load dataset
data=pd.read_csv('Heart_Disease_Dataset.csv')


# In[10]:


data.head()


# In[11]:


data.info()


# In[13]:


data.tail()


# In[12]:


data.describe()


# In[14]:


## missing values
data.isnull().sum()


# In[16]:


data.duplicated()


# In[20]:


#checking the duplicates
(data.duplicated().sum())


# In[19]:


len(data[data.duplicated()])


# In[21]:


data.columns


# In[24]:


#checking for counting of class in each column
for column in data.columns:
    print(data[column].value_counts())


# In[ ]:




