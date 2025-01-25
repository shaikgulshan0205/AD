#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
import warnings
warnings.filterwarnings('ignore')


# In[2]:


df=sns.load_dataset('titanic')


# In[3]:


df.head


# In[4]:


df.tail


# In[25]:


df['who'].unique()


# In[8]:


df.duplicated().sum()


# In[7]:


df[df.duplicated()]


# In[14]:


df[df.duplicated()]


# In[15]:


df.drop_duplicates(inplace=True)


# In[17]:


df.reset_index(drop=True)


# In[18]:


df


# In[19]:


df.isnull().sum


# In[20]:


sns.heatmap(df.isnull())
plt.show()


# In[21]:


df


# In[22]:


df.dropna()


# In[23]:


((784-181)/784)*100


# In[24]:


df.isnull().sum


# In[26]:


df.drop('deck',axis=1,inplace=True)


# In[28]:


df.dtypes


# In[29]:


df['embark_town'].unique()


# In[31]:


df['embark_town'].mode()[0]


# In[32]:


df['embark_town'].isnull().sum()


# In[33]:


df['embark_town'].isnull().sum()


# In[34]:


df['age'].isnull().sum()


# In[35]:


df['age'].median()


# In[36]:


df['age'].fillna(df['age'].median(),inplace=True)


# In[37]:


df['age'].isnull().sum


# In[ ]:


print('Missing values before imputation - ',df['embarked'].isnull().sum())
df['embarak']


# In[38]:


df.describe()


# In[39]:


df.describe(include='O')


# In[41]:


df['embarked']


# In[40]:


df['alive']

