#!/usr/bin/env python
# coding: utf-8
if condition1:
   task1 block of code
elif condition2:
     task2 block of code
elif condition3:
     task3 block of code
else:
    task4 block of code
# In[1]:


x=9
if x%2==0:
    print("Even")
else:
    print("odd")


# In[4]:


7%2==0


# In[5]:


x=8


# In[6]:


x%2==0


# In[7]:


x>6


# In[8]:


x<=5


# In[9]:


x*9


# In[10]:


bool(x+6)


# In[12]:


x=-5.8
if x>0:
    print('pos')
elif x<0:
    print('neg')
else:
    print('zero')


# In[16]:


x=20
if x>0:
    print('pos')
    if x>10:
        print('M')
    elif x>20:
        print('P')
    elif x<10:
        print('K')
    else:
        print('T')
elif x==0:
    print('neg')
    
    if x<-20:
        print('Q')
    elif x>-10:
        print('C')
    elif x>-30:
        print('Z')
else:
    print('zero')
    
    


# In[24]:


x=7.5
if x>0:
    print('pos')
    if x>10:
        print('M')
    elif x>20:
        print('P')
    elif x<10:
        print('K')
    else:
        print('T')
elif x<0:
    print('neg')
    
    if x<-20:
        print('Q')
    elif x>-10:
        print('C')
    elif x>-30:
        print('Z')
else:
    print('zero')


# In[25]:


x='telangana'
x='Tiger'
x='Toy'


# In[29]:


x='lion'
if x[0]=='t' or x[0]=='T':
    print('yes')
else:
    print('no')


# In[30]:


x='tiger'
if x[0]=='t' or x[0]=='T':
    print('yes')
else:
    print('no')


# In[ ]:




