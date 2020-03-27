#!/usr/bin/env python
# coding: utf-8

# In[9]:


from plotly import __version__
from plotly.offline import init_notebook_mode
from plotly.offline import download_plotlyjs
init_notebook_mode, plot
init_notebook_mode(connected=True)
print (__version__)
import plotly.graph_objs as go
plot([go.Scatter(x=[95, 77, 84], y=[75, 67, 56])])

