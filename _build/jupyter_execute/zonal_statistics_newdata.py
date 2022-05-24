#!/usr/bin/env python
# coding: utf-8

# # Tutorial Content
# 
# This notebook will walk you through steps to read in and organize velocity data in a raster format using xarray and rioxarray tools
# 
# First, lets install the python libraries that were listed on the [Software](software.ipynb) page:

# In[1]:


import geopandas as gpd
import os
import numpy as np
import xarray as xr
import rioxarray as rxr
import matplotlib.pyplot as plt
from geocube.api.core import make_geocube
import xarray as xr
import numpy as np
import pandas as pd
import packaging
import pyproj


# In[2]:


gen_path = '/Users/emmamarshall/Desktop/phd_research/siparcs/'


# In[3]:


#data
itslive = rxr.open_rasterio('/Users/emmamarshall/Desktop/phd_research/siparcs/HMA_G0120_0000.nc').squeeze()


# In[4]:


itslive.v


# In[5]:


itslive.rio.crs.from_wkt


# In[6]:


type(itslive)
itslive.rio.crs


# In[7]:


#read in vector data 
se_asia = gpd.read_file('/Users/emmamarshall/Downloads/15rgi60SouthAsiaEast/15_rgi60_SouthAsiaEast.shp')
#sw_asia = gpd.read_file('/Users/emmamarshall/Desktop/phd_research/nisar_prepwork/rgi_1km/sw_asia_1km.shp')
#c_asia = gpd.read_file('/Users/emmamarshall/Desktop/phd_research/nisar_prepwork/rgi_1km/central_asia_1km.shp') 

#se_asia_path = '/Users/emmamarshall/Desktop/phd_research/nisar_prepwork/rgi_1km/se_asia_1km.shp'
#sw_asia_path = '/Users/emmamarshall/Desktop/phd_research/nisar_prepwork/rgi_1km/sw_asia_1km.shp'
#c_asia_path = '/Users/emmamarshall/Desktop/phd_research/nisar_prepwork/rgi_1km/central_asia_1km.shp'




# In[8]:


se_asia_prj = se_asia.to_crs('+proj=lcc +lat_1=15 +lat_2=65 +lat_0=30 +lon_0=95 +x_0=0 +y_0=0 +ellps=WGS84 +datum=WGS84 +units=m no_defs'
                             )


# In[9]:


se_asia_prj.plot()


# In[10]:


fig, ax = plt.subplots()

itslive.v.plot.imshow(ax=ax, alpha = 0.1)
se_asia_prj.plot(ax=ax, color='red')


# In[11]:


se_asia_prj['Unique_ID'] = se_asia_prj.index.astype(int)
se_asia_prj


# In[12]:


def rasterize_vector(gpdf_prj, raster_obj):  #for now, project objects outside of fn
    
    #use index as a unique key for each glacier
    gpdf_prj['Integer_ID'] = gpdf_prj.index.astype(int)
    #print(gpdf_utm['Integer_ID'])
    
    #rasterize glacier vector by unique id 

    out_grid = make_geocube(
            vector_data = gpdf_prj,
            measurements = ['Integer_ID'],
            like = raster_obj['v'] #need to specify a var here, not sure best way to do that
            )
    
    #now merge the rasterized vector and the original raster togehter into a geocube
    out_grid['speed'] = (raster_obj.dims, raster_obj.v.values, raster_obj.attrs, raster_obj.encoding)
    
    #now, get velocity statistics of each 'region' (integer) using the mask
    #grouped_ID = out_grid.drop('spatial_ref').groupby(out_grid.Integer_ID)

    #compute zonal stats groupedd by ID
    #grid_mean_sp = grouped_ID.mean().rename({'speed': 'speed_mean'})
    #grid_min_sp = grouped_ID.min().rename({'speed': 'speed_min'})
    #grid_max_sp = grouped_ID.max().rename({'speed': 'speed_max'})
    #grid_std_sp = grouped_ID.max().rename({'speed': 'speed_std'})
    
    #merge each zonal stat xr obj into a single xr obj, convert to pandas df
    #zonal_stats = xr.merge([grid_mean_sp, grid_min_sp, grid_max_sp, grid_std_sp]).to_dataframe()
    #zonal_stats = zonal_stats.reset_index()
    
   # return zonal_stats
    return out_grid


# In[13]:


outgrid_seasia = rasterize_vector(se_asia_prj, itslive)


# In[15]:


outgrid_seasia


# In[14]:


outgrid_seasia.Integer_ID.plot.imshow()


# In[16]:


grouped_ID = outgrid_seasia.drop('spatial_ref').groupby(outgrid_seasia.Integer_ID)


# In[ ]:





# In[22]:


grid_mean_sp = grouped_ID.mean().rename({'speed': 'speed_mean'})
grid_median_sp = grouped_ID.median().rename({'speed': 'speed_median'})
grid_min_sp = grouped_ID.min().rename({'speed': 'speed_min'})
grid_max_sp = grouped_ID.max().rename({'speed': 'speed_max'})
#grid_std_sp = grouped_ID.max().rename({'speed': 'speed_std'})


# In[19]:


zonal_stats = xr.merge([grid_mean_sp, grid_median_sp, grid_min_sp, grid_max_sp, grid_std_sp]).to_dataframe()
zonal_stats = zonal_stats.reset_index()
zonal_stats


# In[20]:


#now, trying to merge zonal stats df back with original glacier df on integer_ID col
se_asia_glacier_data = se_asia_prj.merge(zonal_stats, on='Integer_ID')


# In[21]:


zonal_stats['speed_mean']

fig, ax = plt.subplots()
se_asia_glacier_data.plot.scatter(x='Integer_ID',y = 'speed_mean', c = 'darkblue', ax=ax)


# In[33]:


zonal_stats['speed_mean'].min()


# In[34]:


se_asia_glacier_data.plot(column='speed_mean', legend=True)


# In[ ]:





# In[ ]:




