#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv("C:/Users/MSI-PC/OneDrive - IIT Kanpur/Industrial Management & Engineering/Semester 2/IME625A Introduction To Stochastic Processes And Their Applications/Stochastic Project/Data/data.csv")


# In[3]:


data.describe()


# In[4]:


data_train = data.head(143)
data_test = data.tail(50)


# In[5]:


from sklearn.cluster import KMeans


# In[6]:


kmeans = KMeans(n_clusters=3)
kmeans.fit(data_train)


# In[7]:


kmeans.cluster_centers_


# In[8]:


labels_train = kmeans.labels_
labels_train


# In[9]:


np.count_nonzero(labels_train==0)


# In[10]:


np.count_nonzero(labels_train==1)


# In[11]:


np.count_nonzero(labels_train==2)


# In[12]:


data_train['symbol'] = labels_train


# In[13]:


data_train['symbol'] = np.where(data_train['symbol']==0,'low',np.where(data_train['symbol']==1,'high','medium'))


# In[15]:


data_train.to_csv(r"C:/Users/MSI-PC/OneDrive - IIT Kanpur/Industrial Management & Engineering/Semester 2/IME625A Introduction To Stochastic Processes And Their Applications/Stochastic Project/Data/train_data_r.csv", index = False)


# In[16]:


labels_test= kmeans.predict(data_test)
labels_test


# In[17]:


np.count_nonzero(labels_test==0)


# In[18]:


np.count_nonzero(labels_test==1)


# In[19]:


np.count_nonzero(labels_test==2)


# In[20]:


data_test['symbol'] = labels_test


# In[21]:


data_test['symbol'] = np.where(data_test['symbol']==0,'low',np.where(data_test['symbol']==1,'high','medium'))


# #### data_test.to_csv(r"C:/Users/MSI-PC/OneDrive - IIT Kanpur/Industrial Management & Engineering/Semester 2/IME625A Introduction To Stochastic Processes And Their Applications/Stochastic Project/Data/test_data_r.csv", index = False)
