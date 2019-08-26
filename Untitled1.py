#!/usr/bin/env python
# coding: utf-8

# In[12]:


import numpy as np
a = np.zeros(3)
type(a[0])


# In[13]:


z = np.zeros(10)
z


# In[14]:


z.shape


# In[17]:


z.shape = (10,1)
z


# In[5]:


z = np.ones(10)
z


# In[44]:


z = np.empty(6)
z


# In[38]:


z = np.linspace(2,10,5)
z


# In[39]:


z = np.array((10,20))
z


# In[40]:


a_list = [1,2,3,4,5,6,7]
z = np.array([a_list])
z


# In[28]:


type(z)


# In[17]:


b_list = [[9,8,7,6,5,4,3,2,1],[1,2,3,4,5,6,7,8,9]]
z = np.array([b_list])
z


# In[47]:


z.shape
get_ipython().run_line_magic('pinfo', 'z.shape')


# In[23]:


np .random.seed(0)
zl = np.random.randint(10,size=6)
zl


# In[25]:


zl[0]


# In[27]:


zl[0:2]


# In[28]:


zl[-1]


# In[ ]:





# In[ ]:




