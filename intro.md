# Introduction

In this this tutorial, we will demonstrate how to access and work with with multi-dimensional remote sensing data using the python package and open source project `xarray`. This example will use an ice velocity dataset called [ITS_LIVE](https://its-live.jpl.nasa.gov/). 

## Overview

This tutorial contains a number of jupyter notebooks demonstrating various steps of a typical workflow for accessing, processing and analyzing remote sensing data. The structure is as follows:
    1. Data access (Two examples of accessing ITS_LIVE velocity data)
    2. Processing and analysis at the scale of an individual glacier
    3. Processing and analysis of a group of glaciers at a sub-regional to regional scale

## Learning objectives
- data access (downloading and cloud-based)
- basic raster manipulation and organizing in **xarray**
- using **geopandas** to query raster data in **xarray**-format
- aggregating using xarray groupby
- xarray to pandas/geopandas


Navigate to the other pages in this jupyter book to find out more about this tutorial. You can check out the data and open source python tools we'll be using before we get started with the notebook. 

```{tableofcontents}
```
