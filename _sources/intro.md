# Introduction

This tutorial will demonstrate how to access and work with with multi-dimensional remote sensing data using the python package and open source project `xarray`. This example will use a glacier surface velocity dataset called [ITS_LIVE](https://its-live.jpl.nasa.gov/). 

## Overview

This tutorial contains a number of jupyter notebooks demonstrating various steps of a typical workflow for accessing, processing and analyzing remote sensing data. The structure is as follows:  
&nbsp;&nbsp;&nbsp;&nbsp; 1. Data access (accessing ITS_LIVE data stored in s3 buckets on Amazon Web Services (AWS))  
&nbsp;&nbsp;&nbsp;&nbsp; 2. Processing and analysis at the scale of an individual glacier  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; a. Clipping large raster to a smaller area of interest and preliminary dataset inspection  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b. Using xarray for data analysis and visualization  
&nbsp;&nbsp;&nbsp;&nbsp; 3. Processing and analysis of a group of glaciers within a sub-region  

## Learning objectives
This tutorial demonstrates how to use xarray for scientific investigation of remote sensing data. The learning goals include **high-level science goals** as well as specific *python and xarray techniques*. 

* **Load ITS_LIVE data from AWS S3 buckets**
*Lazily load cloud datasets using xarray, dask and zarr*

* **Convert vector polygons to raster**
*Data manipulation with geopandas, xarray and geocube*

* **Inspect large, multi-dimensional dataset**
*Use xarray label-based and index-based selection methods*

* **Analyze glacier surface velocity data at multiple spatial scales**
*Use rioxarray's .clip() to subset data to scale of individual glacier*
*Use geocube, xarray's `.groupby()` and pandas dataframes to compute reductions on groups of glaciers*

* **Examine dense time series of surface velocity data**
*Leverage xarray tools such as `.resample()`, `.map()` and `.reduce()`*

* **Construct seasonal averages of glacier velocity**
*Use's xarray's groupby and functionality*

## Tutorial structure
Navigate to the other pages in this jupyter book to find out more about this tutorial. You can check out the data and open source python tools we'll be using before we get started with the notebook in the [Software and Data](software.ipynb) page. 

```{tableofcontents}
```
