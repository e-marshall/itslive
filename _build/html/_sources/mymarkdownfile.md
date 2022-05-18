# Exploring glacier surface velocity data

In this notebook, we'll go over steps to access glacier surface velocity data, organize it into a format that's easier to work with, and then calculate mean velocities for individual glaciers within a region.

(section-label)=
#### First, let's take a look at the different datasets we'll be using

The velocity data that we'll be using is from the  [ITS_LIVE dataset](https://its-live.jpl.nasa.gov/#access). This dataset contains global coverage of land ice velocity data at various temporal freuencies and in various formats. Follow the link to explore the data that's available for a particular region you may be interested in. 

The ITS_LIVE velocity data is accessed in a raster format and the data covers a large swath of terrain covering land that is glaciated and non-glaciated. We want to select just the pixels that cover glaciated surfaces; to do this, we use glacier outlines from the [Randolph Glacier Inventory](https://www.glims.org/RGI/). 

Head to the next page to see how we start working with this data 
