#!/usr/bin/env python
# coding: utf-8

# # Tutorial Content
# 
# ***Still need to clean up comments, add text and things like that***
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


# In[2]:


gen_path = '/Users/emmamarshall/Desktop/phd_research/siparcs/'


# The velocity data we are using is broken into individual velocity components. That means that for the same spatial footprint, we have a file containing ice movement in the x direction and a file containing ice movement in the y direction. We need information from both of these files so we write a function to bring both files into the jupyter notebook, then organize them so that we can see the movement of ice in both the x and y directions as well as the magnitude of the ice velocity (speed). 
# 
# 

# In[3]:


def components_to_speed(vx_path, vy_path):
    '''this function reads in x,y components of velocity, generates speed variable. return xarray
    dataset w/ x,y, speed variables. function will break if vx,vy objects don"t have same x,y coords'''
    
    vy_da = rxr.open_rasterio(vy_path, masked=False).squeeze()
    vx_da = rxr.open_rasterio(vx_path, masked=False).squeeze()
    
    ds_gen = xr.Dataset()
    ds_gen['vx'] = vx_da
    ds_gen['vy'] = vy_da
    sp = np.sqrt((ds_gen['vx'].data**2) + ds_gen['vy'].data**2)
    ds_gen['sp'] = (['x','y'], sp.T)
    
    return ds_gen


# Let's break down what exactly the above function is doing:
# 
# First, we see that it takes two inputs: vx_path and vy_path. These paths point to where on our computer the different files are stored. 
# 
# In the first two lines of the function we use rioxarray to read in the x- and the y-component files as **xarray.DataArrays**
# 
# After that, we initialize a new object, *ds_gen*, which is a **xarray.DataSet**. We then add a variable to ds_gen called 'vx' and assign the vx_da object to that variable. We do the same for vx_da. Now, we have made a dataset that is composed of the two data arrays that we read in from file. 
# 
# We are also interested in speed, so we take the equation for computing magnitude of velocity and add a third variable (DataArray) to our Dataset. 
# 
# This will add a variable defined by the equation:
# 
#             vv = (vx^2 + vy^2)^1/2

# Let's execute the function and take a look at the object it returns
# 
# First, define the inputs to your function. These are the paths to the x and the y data on your computer:

# In[4]:


n45_vy_path = gen_path + '/mynewbook/gardner_data/N45_0240m_vy.tiff'
n45_vx_path = gen_path + 'mynewbook/gardner_data/N45_0240m_vx.tiff'


# And run the function: 

# In[5]:


ds_45n = components_to_speed(n45_vx_path, n45_vy_path)


# In[6]:


ds_45n


# In[7]:


print(ds_45n.dims)
print('---')
print(ds_45n.coords)
print('---')
print(ds_45n.variables)
print('---')
print(ds_45n.attrs)


# In[8]:


#read in vector data 
se_asia = gpd.read_file('/Users/emmamarshall/Downloads/15rgi60SouthAsiaEast/15_rgi60_SouthAsiaEast.shp')




# In[9]:


len(se_asia['RGIId'])


# In[10]:


def rasterize_vector(gpdf, utm_code, raster_obj): 
    
    #read in gpdf from shp file
    #gpdf = gpd.read_file(vector_path)
    #project to local utm
    gpdf_utm = gpdf.to_crs(f'EPSG:{utm_code}')
    #use index as a unique key for each glacier
    gpdf_utm['Integer_ID'] = gpdf_utm.index.astype(int)
    #print(gpdf_utm['Integer_ID'])
    
    #rasterize glacier vector by unique id 

    out_grid = make_geocube(
            vector_data = gpdf_utm,
            measurements = ['Integer_ID'],
            like = raster_obj['sp'] #need to specify a var here, not sure best way to do that
            )
    
    #now merge the rasterized vector and the original raster togehter into a geocube
    out_grid['speed'] = (raster_obj.dims, raster_obj.sp.values, raster_obj.attrs, raster_obj.encoding)
    
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


# In[11]:


rasterize_vector_seasia = rasterize_vector(se_asia, 32645, ds_45n)
rasterize_vector_seasia


# In[12]:


len(rasterize_vector_seasia.Integer_ID)


# In[13]:


#project to utm
se_asia_utm = se_asia.to_crs('EPSG:32645')
#make a col in df that is a unique integer ID (from index) for each glacier
se_asia_utm['Integer_ID'] = se_asia_utm.index.astype(int)
#double checking that all glaciers are assigned an ID
se_asia_utm.plot.scatter(x='Integer_ID', y='Area')


# The plot above shows the mean ice speed of every glacier in the geodataframe object, **se_asia**, that lies within the spatial extent the velocity object.

# In[14]:


#rasterize glacier vector by unique id 
#
out_grid_se_asia = make_geocube(
            vector_data = se_asia_utm,
            measurements = ['Integer_ID'],
            like = ds_45n['sp']
)


# In[15]:


#now merge the rasterized vector and the original raster togehter into a geocube
out_grid_se_asia['speed'] = (ds_45n.dims, ds_45n.sp.values, ds_45n.attrs, ds_45n.encoding)
out_grid_se_asia


# In[16]:


#trying to figure out why 1300 glaciers or so get dropped
print(len(out_grid_se_asia.Integer_ID))


# In[17]:


#now, get velocity statistics of each 'region' (integer) using the mask
grouped_ID = out_grid_se_asia.drop('spatial_ref').groupby(out_grid_se_asia.Integer_ID)
grouped_ID


# In[29]:


grid_mean_sp = grouped_ID.mean().rename({'speed': 'speed_mean'})
grid_median_sp = grouped_ID.median().rename({'speed': 'speed_median'})
grid_min_sp = grouped_ID.min().rename({'speed': 'speed_min'})
grid_max_sp = grouped_ID.max().rename({'speed': 'speed_max'})
grid_std_sp = grouped_ID.max().rename({'speed': 'speed_std'})


# In[30]:


zonal_stats = xr.merge([grid_mean_sp, grid_median_sp, grid_min_sp, grid_max_sp, grid_std_sp]).to_dataframe()
zonal_stats = zonal_stats.reset_index()
zonal_stats


# In[31]:


#now, trying to merge zonal stats df back with original glacier df on integer_ID col
se_asia_glacier_data = se_asia_utm.merge(zonal_stats, on='Integer_ID')


# In[32]:


zonal_stats['speed_mean']

fig, ax = plt.subplots()
se_asia_glacier_data.plot.scatter(x='Integer_ID',y = 'speed_mean', c = 'darkblue', ax=ax)


# In[33]:


zonal_stats['speed_mean'].min()


# In[34]:


se_asia_glacier_data.plot(column='speed_mean', legend=True)


# In[ ]:





# In[ ]:




