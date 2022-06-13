# Introduction

In this this tutorial, we will demonstrate how to access and work with with multi-dimensional remote sensing data using the python package and open source project `xarray`. This example will use an ice velocity dataset called [ITS_LIVE](https://its-live.jpl.nasa.gov/). 

## Structure

This tutorial contains a number of jupyter notebooks demonstrating various steps of a typical workflow for accessing, processing and analyzing remote sensing data. 



## Background 
Frequently when working with geospatial data, we want to accomplish tasks that force us to work with raster and vector data together. Vector data (points, lines, polygons) often represent physical features and areas of interest. Raster data are gridded objects where individual pixels are assigned different values. Data such as temperature, elevation, layer thickness and velocit are represented in raster format. Two-dimensional, gridded raster data can often cover large spatial extents. Vector data help us to identify features and locations of interest on the ground. This tutorial will demonstrate an example of using vector data to extract regions of interest from within a raster dataset. 

There are different tools in python for handling vector and raster data: **xarray** is a great way to work with raster data while **geopandas** handles vector data well. During various stages of data processing and analysis, it may be useful to switch between these two formats for certain tasks. The tutorial in this chapter will demonstrate accessing and exploring data using both **xarray** and **geopandas**, using **geopandas** to query raster data in **xarray** format, and various analytical steps using both **xarray** and **geopandas**. 

The example we'll be working with in this chapter is glacier velocity data. We will start with polygons representing glacier outlines and glacier surface velocity raster data. At the end of the notebook, we will have both raster and vector objects representing the data we have manipulated. You'll see that they will both be useful for conveying different types of information.

## Learning objectives
- data access (downloading and cloud-based)
- basic raster manipulation and organizing in **xarray**
- examining shp files using **geopandas**
- aggregating using xarray groupby
- xarray to pandas/geopandas


Navigate to the other pages in this jupyter book to find out more about this tutorial. You can check out the data and open source python tools we'll be using before we get started with the notebook. 

```{tableofcontents}
```
