# DISCLAIMER: This code was written by John Wilkinson, and should not be copied or used without citation.
# Please adhere to university policy 

import matplotlib.pyplot as plt
import numpy as np
import xarray as xr   # to read netcdf files
import pandas as pd
import cartopy.crs as ccrs  # to add maps

# Returns the name of a month, given its integer value
def get_month(month_int):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month_int]

# Reads evaporation data from NOAA database, returns the dataset
def read_evaporation_file():
    file_loc="https://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis2.derived/LTMs/gaussian_grid/"
    file1="lhtfl.sfc.mon.ltm.nc"
    ds1 = xr.open_dataset(file_loc+file1)

    # convert time to datetime64
    ds1["time"] = ds1["time"].astype("datetime64[ns]")
    print(ds1)
    return ds1

# Plots a basic evaporation map
def basic_evaporation(month_int):
    ds1 = read_evaporation_file()
    ds1.lhtfl.isel(time=month_int).plot()   
    plt.title(f"Evaporation in {get_month(month_int)}")
    plt.show()

# Plots a prettier evaporation map with a cartographic overlay
def mapped_evaporation(month_int):
    ds1 = read_evaporation_file()

    cmap1=plt.cm.gist_earth_r     # color table
    lev1=np.arange(-10,255,5)
    proj = ccrs.PlateCarree()

    fig = plt.figure(figsize=(9,5))
    ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    (ds1.lhtfl).isel(time=month_int).plot.contourf(ax=ax, transform=ccrs.PlateCarree(),levels=lev1, cmap=cmap1)
    ax.coastlines()
    plt.title(f"{get_month(month_int)} surface latent heat flux (W/m2)")
    plt.show()

# Generates plots for January and July. Note - mapped evaporation is a bit slow
basic_evaporation(0)
basic_evaporation(6)

mapped_evaporation(0)
mapped_evaporation(6)