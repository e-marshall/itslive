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

# ### Two streams of velocity data
# 
# This notebook is going to contain an example of something you might run into: the same (or similar) data is hosted from different sources, meaning it is accessed in different ways and may be in slightly different formats. In this case, we have ITS_LIVE velocity data that can be accessed from an S3 bucket and from the NSIDC DAAC. You'll see that while this is the same underlying dataset, the formatting varies significantly between the two and in this case, the data are in two different file types (Geotiff and netcdf). In the [Tutorial content](new_velocity_data.ipynb) page, you will see sections on ingesting and working with both types of data. 

# In[ ]:




