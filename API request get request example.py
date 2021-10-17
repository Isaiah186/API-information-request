#!/usr/bin/env python
# coding: utf-8

# In[4]:


import requests

#Endpoint to be accessed
url = "http://api.open-notify.org/astros.json"


response = requests.get(url)


#.json() is a function that converts byte code to a json format
data = response.json()

print(data)


# In[ ]:




