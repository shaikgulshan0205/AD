#!/usr/bin/env python
# coding: utf-8

# In[31]:


import seaborn as sns 
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt


# In[32]:


df=sns.load_dataset("tips")
df


# In[33]:


df.info()


# In[34]:


df.isnull()


# In[35]:


from sklearn.preprocessing import LabelEncoder
lb=LabelEncoder()


# In[36]:


df['smoker']=lb.fit_transform(df['smoker'])
df['sex']=lb.fit_transform(df['sex'])
df['time']=lb.fit_transform(df['time'])
df['day']=lb.fit_transform(df['day'])


# In[37]:


df.dtypes


# In[38]:


df.corr()


# In[39]:


import matplotlib.pyplot as plt
sns.heatmap(np.abs(df.corr()),cmap='Blues')
plt.show()


# In[40]:


import matplotlib.pyplot as plt
sns.heatmap(np.abs(df.corr())>0.5,cmap='Reds')
plt.show()


# In[41]:


sns.heatmap(np.abs(df.corr())>0.6,cmap="Purples")
plt.show()


# In[42]:


sns.heatmap(np.abs(df.corr())>0.8,cmap='Reds')
plt.show()


# In[43]:


df.describe()


# In[44]:


from sklearn.preprocessing import StandardScaler
sc=StandardScaler()


# In[45]:


sc_array=sc.fit_transform(df)


# In[46]:


sc_array.shape


# In[47]:


df.head()


# In[48]:


sc_df=pd.DataFrame(sc_array,columns=df.columns)
sc_df.head(3)


# In[49]:


sc_df.describe()


# In[50]:


np.round(sc_df.describe(),2)


# In[51]:


from sklearn.preprocessing import MinMaxScaler
mx_scaler=MinMaxScaler()


# In[52]:


mx_array=mx_scaler.fit_transform(df)
mx_array


# In[53]:


mx_df=pd.DataFrame(mx_array,columns=df.columns)
mx_df


# In[57]:


import statsmodels.api as sm
sm.qqplot(df['total_bill'],line='s')
plt.show()


# In[59]:


sns.regplot(x='total_bill', y='tip', data=df, line_kws={'color':'red'}, scatter_kws={'color':'green'})
plt.show()


# In[65]:


sns.regplot(x='total_bill',y='tip',data=df,ci=None,line_kws={'color':'yellow'},scatter_kws={'color':'purple'})
plt.show()


# In[ ]:




