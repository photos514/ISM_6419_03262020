#!/usr/bin/env python
# coding: utf-8

# In[15]:


import plotly.offline
from plotly.offline import plot

import plotly.graph_objs as go
import numpy as np
x = np.random.randn(2000)
y = np.random.randn(2000)

plot([go.Histogram2dContour(x=x, y=y,
contours=dict (coloring='heatmap')),
go.Scatter(x=x, y=y, mode='markers',
marker=dict(color='white', size=3, opacity=0.3))], show_link=False)


# In[16]:


import plotly.offline as offline
import plotly.graph_objs as go
offline.plot({'data': [{'y': [14, 22, 30,44]}],'layout': {'title': 'Offline Plotly', 'font':dict(size=16)}}, image='png')


# In[ ]:




