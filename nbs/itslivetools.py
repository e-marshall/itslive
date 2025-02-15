from typing import Union

import geopandas as gpd
import xarray as xr
from shapely.geometry import Point, Polygon


def read_in_s3(http_url: str, chunks: Union[None, str, dict] = "auto") -> xr.Dataset:
    """
    Reads a zarr datacube given an S3 URL using
    xarray and returns it as a xr.Dataset.

    Parameters
    ----------
    http_url : str
        The HTTP URL of the dataset to be read.
    chunks : str or dict, optional
        The chunk size for dask. Default is 'auto'.
        If None, the dataset will be loaded without chunking.

    Returns
    -------
    xarray.Dataset
        The dataset loaded from the given URL.
    """
    return xr.open_dataset(http_url, chunks=chunks, engine="zarr", decode_coords="all", decode_timedelta=False)


def get_bounds_polygon(input_xr: xr.Dataset) -> gpd.GeoDataFrame:
    """
    Generate a GeoDataFrame containing a polygon that represents the bounding box of the input xarray Dataset.
    Parameters
    ----------
    input_xr : xr.Dataset
        An xarray Dataset containing 'x' and 'y' coordinates.
    Returns
    -------
    gpd.GeoDataFrame
        A GeoDataFrame with a single polygon geometry representing the bounding box of the input dataset.
    """

    xmin = input_xr.coords["x"].data.min()
    xmax = input_xr.coords["x"].data.max()

    ymin = input_xr.coords["y"].data.min()
    ymax = input_xr.coords["y"].data.max()

    pts_ls = [(xmin, ymin), (xmax, ymin), (xmax, ymax), (xmin, ymax), (xmin, ymin)]

    crs = f"epsg:{input_xr.mapping.spatial_epsg}"

    polygon_geom = Polygon(pts_ls)
    polygon_gdf = gpd.GeoDataFrame(index=[0], crs=crs, geometry=[polygon_geom])

    return polygon_gdf


def find_granule_by_point(input_point: list) -> str:
    """
    Returns the URL for the granule (zarr datacube) containing a specified point.

    Parameters
    ----------
    input_point : list
        A list containing the [lon,lat] coordinates of the point in EPSG:4326 format.

    Returns
    -------
    str
        The URL of the granule containing the specified point.
    """
    catalog = gpd.read_file("https://its-live-data.s3.amazonaws.com/datacubes/catalog_v02.json")

    # make shapely point of input point
    p = gpd.GeoSeries([Point(input_point[0], input_point[1])], crs="EPSG:4326")
    # make gdf of point
    gdf = gdf = gpd.GeoDataFrame({"label": "point", "geometry": p})
    # find row of granule
    granule = catalog.sjoin(gdf, how="inner")

    url = granule["zarr_url"].values[0]
    return url
