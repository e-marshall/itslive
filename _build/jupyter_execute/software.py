#!/usr/bin/env python
# coding: utf-8

# # Software and Data
# 
# On this page you'll find information about the computing environment and datasets that we'll be using in this tutorial. 
# 
# 
# ## Computing environment
# 
# Below, you'lll see a list of the python libraries we'll be using in this example:

# In[1]:


import geopandas as gpd
import os
import numpy as np
import xarray as xr
import rioxarray as rxr
import matplotlib.pyplot as plt
from geocube.api.core import make_geocube


# ## Data
# 
# The velocity data that we'll be using is from the  [ITS_LIVE dataset](https://its-live.jpl.nasa.gov/#access). This dataset contains global coverage of land ice velocity data at various temporal freuencies and in various formats. Follow the link to explore the data that's available for a particular region you may be interested in. 
# 
# The ITS_LIVE velocity data is accessed in a raster format and the data covers a large swath of terrain covering land that is glaciated and non-glaciated. We want to select just the pixels that cover glaciated surfaces; to do this, we use glacier outlines from the [Randolph Glacier Inventory](https://www.glims.org/RGI/). 
# 
# Head to the next page to see how we start working with this data 
# 

# In[ ]:




