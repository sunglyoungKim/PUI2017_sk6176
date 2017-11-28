
# coding: utf-8

# In[1]:


#read a variable from a file
import json


# In[2]:


get_ipython().system('head apidef.json')


# In[3]:


json_data = open("apidef.json").read()
myAPI = json.loads(json_data)
myAPI["myAPI"]

