#!/usr/bin/env python
# coding: utf-8

# In[39]:


import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[3]:


df=sns.load_dataset("tips")
df


# In[4]:


df.info()


# In[5]:


df.isnull()


# In[6]:


from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()


# In[10]:


df['smoker']=lb.fit_transform(df['smoker'])
df['sex']=lb.fit_transform(df['sex'])
df['time']=lb.fit_transform(df['time'])
df['day']=lb.fit_transform(df['day'])


# In[12]:


df.dtypes


# In[13]:


df.corr()


# In[51]:


import matplotlib.pyplot as plt
sns.heatmap(np.abs(df.corr()),cmap='Blues')
plt.show()


# In[57]:


import matplotlib.pyplot as plt
sns.heatmap(np.abs(df.corr())>0.5,cmap='Reds')
plt.show()


# In[58]:


sns.heatmap(np.abs(df.corr())>0.6,cmap="Purples")
plt.show()


# In[60]:


sns.heatmap(np.abs(df.corr())>0.8,cmap='Reds')
plt.show()


# In[61]:


df.describe()


# In[64]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()


# In[65]:


sc_array=sc.fit_transform(df)


# In[67]:


sc_array.shape


# In[69]:


df.head()


# In[68]:


sc_df=pd.DataFrame(sc_array,columns=df.columns)
sc_df.head(3)


# In[71]:


sc_df.describe()


# In[72]:


np.round(sc_df.describe(),2)


# In[ ]:




