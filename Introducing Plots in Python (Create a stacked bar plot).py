#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(20,5), columns=['Jan','Feb','March','April', 'May']) 
df.plot.bar(stacked=True,figsize=(20, 10)).legend(bbox_to_anchor=(1.1, 1))


# In[ ]:




