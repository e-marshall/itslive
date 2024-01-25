import geopandas as gpd
import os
import numpy as np
import xarray as xr
import rioxarray as rxr

from shapely.geometry import Polygon
from shapely.geometry import Point
import hvplot.pandas
import hvplot.xarray

import json
import s3fs

def read_in_s3(http_url, chunks = 'auto'):

    #s3_url = http_url.replace('http','s3')   <-- as of Fall 2023, can pass http urls directly to xr.open_dataset()
    #s3_url = s3_url.replace('.s3.amazonaws.com','')

    datacube = xr.open_dataset(http_url, engine = 'zarr',
                                #storage_options={'anon':True},
                                chunks = chunks)

    return datacube

def get_bounds_polygon(input_xr):
    
    xmin = input_xr.coords['x'].data.min()
    xmax = input_xr.coords['x'].data.max()

    ymin = input_xr.coords['y'].data.min()
    ymax = input_xr.coords['y'].data.max()

    pts_ls = [(xmin, ymin), (xmax, ymin),(xmax, ymax), (xmin, ymax), (xmin, ymin)]

    crs = f"epsg:{input_xr.mapping.spatial_epsg}"

    polygon_geom = Polygon(pts_ls)
    polygon = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom]) 
    
    return polygon

def find_granule_by_point(input_point):
    '''returns url for the granule (zarr datacube) containing a specified point. point must be passed in epsg:4326
    '''
    catalog = gpd.read_file('https://its-live-data.s3.amazonaws.com/datacubes/catalog_v02.json')

    #make shapely point of input point
    p = gpd.GeoSeries([Point(input_point[0], input_point[1])],crs='EPSG:4326')
    #make gdf of point
    gdf = gdf = gpd.GeoDataFrame({'label': 'point', 
                                  'geometry':p})
    #find row of granule 
    granule = catalog.sjoin(gdf, how='inner')

    url = granule['zarr_url'].values[0]
    return url
