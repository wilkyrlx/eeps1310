# DISCLAIMER: This code was written by John Wilkinson, and should not be copied or used without citation.
# Please adhere to university policy 

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr   # to read netcdf files
import cartopy.crs as ccrs  # to add maps

# Reads evaporation data from NOAA database, returns the dataset
def read_evaporation_file():
    file_loc="https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis2.derived/LTMs/gaussian_grid/"
    file1="lhtfl.sfc.mon.ltm.nc"
    ds1 = xr.open_dataset(file_loc+file1)
    return ds1

# TODO: change these graphs to only show monthly data
# Plots a basic evaporation map
def basic_evaporation():
    ds1 = read_evaporation_file()
    ds1.lhtfl.mean("time").plot()   

# Plots a prettier evaporation map with a cartographic overlay
def mapped_evaporation():
    ds1 = read_evaporation_file()

    cmap1=plt.cm.gist_earth_r     # color table
    lev1=np.arange(-10,255,5)
    proj = ccrs.PlateCarree()

    fig = plt.figure(figsize=(9,5))
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    (ds1.lhtfl).mean("time").plot.contourf(ax=ax, transform=ccrs.PlateCarree(),levels=lev1, cmap=cmap1)
    ax.coastlines()
    plt.title("Annual mean surface latent heat flux (W/m2)")

read_evaporation_file()