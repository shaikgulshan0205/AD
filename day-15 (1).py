#!/usr/bin/env python
# coding: utf-8

# In[5]:


from sklearn.ensemble import IsolationForest
import seaborn as sns
import pandas as pd
import numpy as np


# In[2]:


data=sns.load_dataset('iris')
#data_encodees=pd.get_dummies(data)
data


# In[2]:


import seaborn as sns
from scipy.stats import zscore
data=sns.load_dataset('iris')
df=data.copy()


# In[3]:


df


# In[6]:


z_scores=np.abs(zscore(df.drop('species',axis=1)))
z_scores


# In[7]:


non_outliers = (z_scores < 3).all(axis=1)
df_no_ouliers = df[non_outliers]


# In[8]:


df_no_ouliers


# In[14]:


(z_scores<=3).all(axis=1)


# In[16]:


outliers=(z_scores>3).any(axis=1)
outlier_rows=df[outliers]
outlier_rows


# In[17]:


from sklearn.ensemble import IsolationForest
import seaborn as sns
import pandas as pd
import numpy as np


# In[18]:


data=sns.load_dataset("iris")
data


# In[22]:


from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()
data['species']=lb.fit_transform(data['species'])


# In[23]:


data.head(3)


# In[30]:


clf=IsolationForest(random_state=10,contamination=0.02)
clf.fit(data)


# In[28]:


y_hat=clf.predict(data)
y_hat


# In[32]:


y_hat[y_hat==-1]


# In[33]:


np.where(y_hat==-1)


# In[34]:


data.drop(index=[117,131,118],axis=0)


# In[ ]:




