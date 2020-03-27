#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df=pd.DataFrame({'April':np.random.randn(1000)+1,'May':np.random.
randn(1000),'June': np.random.randn(1000) - 1}, columns=['April','May', 'June'])
df.hist(bins=20)


# In[ ]:




