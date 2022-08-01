#!/usr/bin/env python
# coding: utf-8

# # Practice Week 2
# 
# ## Numpy and Pandas
# 
# ### These labs provide an opportunity for you to practice your new NumPy and Pandas knowledge. There is a lot of flexibility in how to answer these questions so they are not autograded. Call over an insutrctor or TA for help or to review your answers.

# ## Step 1: Import necessary packages

# In[4]:


## import necessary packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline


# ## Step 2: Load in the dataset

# In[5]:


# Read in data from source 
df_orig = pd.read_csv("../my_hw_repo/admissions.csv")
print df_orig.head()


# ## Step 3: Create a variable you can work with (so you don't overwrite your original)

# In[6]:


df = df_orig


# ## Step 4: What does your data look like?
# ### Look at some of the columns or rows using indexing
# #### Hint: Use [].

# In[7]:


df[0]
df[:,0]
df[0,:]


# ### How many observations are there?

# In[8]:


df.count()
df_total = # numbers from df.count() added together


# ### Summarize the data in a summary table.

# In[12]:


df.describe()


# ### Access just a single column using the index

# In[13]:


df['Percentage']


# ### Define a function that implements some of the math operations of NumPy on your data.
# #### Perhaps it's helpful to change the decimal places on a given column, or multiply the column by another number. You decide!

# In[ ]:


df['Percentage'] = df['Percentage'] * 100


# ### Create a new df with only the data you are interested in.
# #### Hint: use [] or the .drop attribute()

# In[14]:


df_new = df.drop(['Something', 'Something2'])


# In[ ]:




