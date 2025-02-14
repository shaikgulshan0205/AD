#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[5]:


df=pd.read_csv(r"C:\Users\Asus\Downloads\Wholesale customers data.csv")


# In[6]:


print(df.describe())


# In[7]:


print (df.info())


# In[8]:


df.head()


# In[9]:


df.info()


# In[10]:


df.drop(['Channel','Region'],axis=1,inplace=True)


# In[11]:


array=df.values


# In[12]:


array


# In[13]:


array.shape


# In[14]:


array


# In[15]:


stscaler = StandardScaler().fit(array)
x = stscaler.transform(array)
x


# In[19]:


import scipy.cluster.hierarchy as sch


# In[20]:


plt.figure(figsize=(20,6))
dendo=sch.dendrogram(sch.linkage(x,method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customer data')
plt.ylabel("Eucl Distance")
plt.show()


# In[21]:


len(set(dendo['color_list']))-1


# In[22]:


from sklearn.cluster import AgglomerativeClustering


# In[23]:


group=AgglomerativeClustering(n_clusters=3)
group.fit_predict(x)


# In[24]:


cluster=group.fit_predict(x)
cluster.shape


# In[25]:


from sklearn.metrics import silhouette_score
silhouette_score(x,cluster)


# In[26]:


x


# In[27]:


import warnings
warnings.filterwarnings('ignore')
from sklearn.cluster import KMeans
wcss=[]
for i in range(2,11):
  kmeans=KMeans(n_clusters=i,init = 'k-means++',random_state=42)
  kmeans.fit(x)
  wcss.append(kmeans.inertia_)


# In[28]:


plt.plot(range(2,11),wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()


# In[29]:


model=KMeans(n_clusters=5,random_state=606)
groups=model.fit_predict(x)


# In[30]:


groups.shape


# In[31]:


groups


# In[32]:


group_num=pd.DataFrame(groups,columns=['Group'])
group_num


# In[33]:


cust_kmeans_data=pd.concat([df,group_num],axis=1)
cust_kmeans_data


# In[34]:


silhouette_score(x,groups)


# In[35]:


cust_kmeans_data[cust_kmeans_data['Group']==4]


# In[36]:


cust_kmeans_data[cust_kmeans_data['Group']==3]


# In[37]:


silhouette_score(x,groups)


# In[38]:


from sklearn.cluster import DBSCAN


# In[39]:


db_model=DBSCAN(eps=3.2,min_samples=10)
db_model.fit(x)


# In[40]:


label=db_model.labels_
label


# In[41]:


silhouette_score(x,label)


# In[42]:


cl=pd.DataFrame(db_model.labels_,columns=['cluster'])
df_cluster=pd.concat([df,cl],axis=1)


# In[43]:


df_cluster


# In[44]:


df_cluster[df_cluster['cluster']==-1]


# In[1]:


get_ipython().system('pip install mlxtend')


# In[3]:


import numpy as np
import pandas as np
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules


# In[13]:


data=[
    ['milk','bread','butter','jam'],
    ['milk','cola','jam'],
    ['bread','jam','butter'],
    ['milk','diapers','bread','jam'],
    ['milk','cola','beer'],
    ['milk','bread','butter'],
    ['bread','jam','butter','beer'],
]


# In[14]:


from mlxtend.preprocessing import TransactionEncoder


# In[15]:


te=TransactionEncoder()
df=te.fit(data).transform(data)


# In[ ]:





# In[ ]:




