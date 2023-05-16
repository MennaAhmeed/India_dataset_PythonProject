#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[4]:


data=pd.read_csv(r'C:\Users\Dell\Downloads\India Census.csv')


# In[5]:


data


# In[6]:


data.isnull().sum()


# In[10]:


data.duplicated()


# In[8]:


#Q. 1) How will you hide the indexes of the dataframe.


# In[21]:


data.style.hide(axis='index')    #answer


# In[22]:


#Q. 2) How can we set the caption / heading on the dataframe.


# In[25]:


data.style.set_caption('India Census DataSet 2011')   #answer


# In[24]:


#Q. 3) Show the records related with the districts - New Delhi , Lucknow , Jaipur.


# In[31]:


data[data['District_name'].isin(['New Delhi' , 'Lucknow' , 'Jaipur'])]   #answer


# In[32]:


#Q. 4) Calculate state-wise :
#A. Total number of population.


# In[35]:


data.groupby('State_name').Population.sum().sort_values(ascending=False)   #answer


# In[36]:


#B. Total no. of the population with different religions.


# In[37]:


data.columns


# In[46]:


data.groupby('Population')['Hindus', 'Muslims', 'Christians', 'Sikhs', 'Buddhists', 'Jains'].sum()   #answer


# In[47]:


#Q. 5) How many Male Workers were there in Maharashtra state ?


# In[50]:


data[data['State_name']=='MAHARASHTRA']['Male_Workers'].sum()  #answer


# In[51]:


#Q. 6) How to set a column as index of the dataframe ?


# In[52]:


data.set_index('District_code')   #answer


# In[ ]:




