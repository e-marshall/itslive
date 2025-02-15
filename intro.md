# Introduction

```{important}
Feb 5, 2025
This tutorial is currently undergoing revisions. Please check back soon
```

This tutorial will demonstrate how to access and work with multi-dimensional remote sensing data using the open-source Python package `xarray`. We will use a glacier surface velocity dataset called [ITS_LIVE](https://its-live.jpl.nasa.gov/) to demonstrate scientific analysis that uses both raster data and vector geometries.

## Overview

This tutorial contains a number of Jupyter notebooks demonstrating various steps of a typical workflow for accessing, processing and analyzing remote sensing data:
1) Data access,
    - Accessing ITS_LIVE data stored in s3 buckets on Amazon Web Services (AWS),
2) Manipulation and organization of a larger-than-memory dataset,
2) Processing and analysis at the scale of an individual glacier:
    - a. Clipping large raster to a smaller area of interest and preliminary dataset inspection
    - b. Using xarray for data analysis and visualization
3) Processing and analysis of a group of glaciers within a sub-region using vector data cubes

## Learning objectives
This tutorial demonstrates how to use xarray for scientific investigation of remote sensing data. The learning goals include **high-level science goals** as well as specific *python and xarray techniques*.

* **Load ITS_LIVE data from AWS S3 buckets**
*Lazily load cloud datasets using xarray, dask and zarr*

* **Convert vector polygons to raster**
*Data manipulation with [GeoPandas](https://geopandas.org/en/stable/), [Xarray](https://docs.xarray.dev/en/stable/), [rioxarray](https://corteva.github.io/rioxarray/stable/), and [Xvec](https://xvec.readthedocs.io/en/stable/)*

* **Inspect large, multi-dimensional dataset**
*Use xarray label-based and index-based selection methods*

* **Analyze glacier surface velocity data at multiple spatial scales**
*Use rioxarray's .clip() to subset data to scale of individual glacier*
*Use Xvec, xarray's `.groupby()` and pandas dataframes to compute reductions on groups of glaciers*

* **Examine dense time series of surface velocity data**
*Leverage xarray tools such as `.resample()`, and `.reduce()`*

## Tutorial structure
Navigate to the other pages in this jupyter book to find out more about this tutorial. You can check out the data and open source python tools we'll be using before we get started with the notebook in the [Software and Data](software_and_data.ipynb) page.

```{tableofcontents}
```
