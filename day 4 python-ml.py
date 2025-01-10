#!/usr/bin/env python
# coding: utf-8

# In[1]:


x=5
while x<10:
    print('yes')
    x=x+0.5


# In[3]:


dollars=[40,20,80,50,30]
dollars


# In[7]:


dollars*6


# In[8]:


for i in dollars:
    print(i*85)


# In[10]:


num=[31,45,66,33,90,78,67,89,93,25,59,9,81]
num


# In[13]:


j=[]
k=[]
for i in num:
    if i%2==0:
        j.append(i)
    else:
        k.append(i)


# In[14]:


j


# In[15]:


k


# In[17]:


num=[39,45,66,93,90,78,67,87,89,93,25,59,49,91]
num


# #replace 9 with 1

# In[18]:


num = [39, 45, 66, 93, 90, 78, 67, 87, 89, 93, 25, 59, 49, 91]
updated_num = [int(str(n).replace('9', '1')) for n in num]
print(updated_num)


# In[19]:


h=[]
for i in num:
    a=str(i)
    b=a.replace('9','1')
    c=int(b)
    h.append(c)


# In[ ]:




