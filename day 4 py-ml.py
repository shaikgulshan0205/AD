#!/usr/bin/env python
# coding: utf-8

# In[2]:


y='MallA reddy 2025'
y


# In[3]:


len(y)


# In[5]:


y.count('a')


# In[15]:


def calArea(r):
    a=3.14*r*r
    return a


# In[7]:


calArea(r=10)


# In[12]:


def aor(l,w):
    area=l*w
    return area


# In[13]:


aor(w=5,l=10)


# In[14]:


aor(5,10)


# In[16]:


t='Hyderabad 500008 Telangana'
t


# In[17]:


def countA(x):
    d=x.lower()
    return d.count('a')


# In[19]:


countA(t)


# In[23]:


def count_num_alpha(x):
    c=0
    d=0
    for i in x:
        if i.isalpha():
            c+=i
        elif i.isnumeric():
            d+=i
    return{"Number of alphabets" :c,'Number of digits':d}


# In[ ]:




