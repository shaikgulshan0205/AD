#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns 
import statsmodels.formula.api as smf
import numpy as np


# In[2]:


#Read the data 
cars = pd.read_csv(r"http://localhost:8889/edit/Cars.csv")
cars.head


# In[ ]:


cars.info()


# In[ ]:


cars.isna().sum


# correlation matrix

# In[ ]:


cars.corr()


# In[3]:


import warnings
warnings.filterwarnings('ignore')


# In[4]:


sns.scatterplot(x=cars['WT'],y=cars['MPG'])


# In[14]:


sns.arplot(x=cars['WT'],y=cars['MPG'])


# In[15]:


import pandas as pd
import numpy as np
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[16]:


data=pd.read_csv('/content/NewspaperData.csv')
data.head()


# In[17]:


data.shape


# In[ ]:




