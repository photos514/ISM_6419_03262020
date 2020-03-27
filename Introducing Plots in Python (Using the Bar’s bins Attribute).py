#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May'])
df.plot.hist(bins= 20, figsize=(10,8)).legend 
bbox_to_anchor=(1.2, 1)


# In[ ]:




