# Introduction

This tutorial will demonstrate how to access and work with with multi-dimensional remote sensing data using the python package and open source project `xarray`. This example will use a glacier surface velocity dataset called [ITS_LIVE](https://its-live.jpl.nasa.gov/). 

## Overview

This tutorial contains a number of jupyter notebooks demonstrating various steps of a typical workflow for accessing, processing and analyzing remote sensing data. The structure is as follows:
    1. Data access (accessing ITS_LIVE data stored in s3 buckets on Amazon Web Services (AWS))
    2. Processing and analysis at the scale of an individual glacier
        a. Clipping large raster to a smaller area of interest and preliminary dataset inspection
        b. Using xarray for data analysis and visualization
    3. Processing and analysis of a group of glaciers within a sub-region

## Learning objectives
- accessing cloud-based data with **xarray**
- using **dask** with **xarray**
- raster manipulation and organizing with **xarray**
- using **geopandas** to query raster data in **xarray**-format
- xarray functionality including groupby, reductions and visualization
- xarray to pandas/geopandas


Navigate to the other pages in this jupyter book to find out more about this tutorial. You can check out the data and open source python tools we'll be using before we get started with the notebook. 

```{tableofcontents}
```
