#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing necessary libraries 
from sklearn import datasets 
from sklearn.metrics import confusion_matrix, accuracy_score 
from sklearn.model_selection import train_test_split
import pandas as pd
from PIL import Image
import pytesseract
import re


# In[2]:


dataframe = pd.read_csv("data.csv")
X = dataframe.iloc[:,0:12]
y = dataframe.iloc[:,12]


# In[3]:


dataframe.info()


# In[4]:


dataframe.name.unique()


# In[5]:


dataframe.head()


# In[6]:



# In[7]:


dataframe.ph.plot(kind='hist')


# In[8]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=6174)


# In[9]:


from sklearn.neighbors import KNeighborsClassifier 
knn = KNeighborsClassifier(n_neighbors = 7)
knn.fit(X_train, y_train) 


# In[10]:


predictions = knn.predict(X_test)
print(accuracy_score(y_test, predictions))


# In[11]:


import pickle
filename = 'finalized_model.sav'
pickle.dump(knn, open(filename, 'wb'))


# In[ ]:




