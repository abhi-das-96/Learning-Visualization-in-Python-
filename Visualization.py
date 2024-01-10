#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sis


# In[3]:


iris=sis.load_dataset("iris")


# In[4]:


iris.head()


# In[5]:


sis.countplot(data=iris)


# In[6]:


type(iris)


# In[7]:


iris.dtypes


# In[14]:


iris.corr()


# In[9]:


sis.heatmap(iris.corr())


# In[10]:


sis.pairplot(iris,hue="species")


# In[11]:


sis.distplot(iris["sepal_length"])


# In[12]:


sis.distplot(iris["sepal_length"],bins=20,kde=True,rug=True)


# In[13]:


sis.boxplot(iris)


# In[ ]:




