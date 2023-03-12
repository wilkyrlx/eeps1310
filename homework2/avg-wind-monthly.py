import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import pandas as pd

# Returns the name of a month, given its integer value
def get_month(month_int):
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return months[month_int]

filename='homework2\\files\\HadISST_sst.nc'
ds1=xr.open_dataset(filename)
ds1.close()

file_loc2="http://psl.noaa.gov/thredds/dodsC/Datasets/ncep.reanalysis2.derived/LTMs/gaussian_grid/"
filename2="uwnd.10m.mon.ltm.nc"    # files are different
filename3="vwnd.10m.mon.ltm.nc"    # files are different
with xr.open_dataset(file_loc2+filename2) as ds2:      
    print(ds2)
with xr.open_dataset(file_loc2+filename3) as ds3:      
    print(ds3)

sst=ds1.sst.sel(time=slice('1980','2020'))
sst_clim = sst.groupby('time.month').mean(dim='time')
sst_anom = sst.groupby("time.month") - sst_clim


def plot_avg_wind_m(month):
    # Make a prettier plot.
    cmap1=plt.cm.RdBu_r
    proj = ccrs.PlateCarree()
    fig1 = plt.figure(figsize=(9,5))
    ax1 = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    cs1=sst_anom.sel(time=f'2016-12').squeeze().plot.pcolormesh(ax=ax1, transform=proj, cmap=cmap1, vmax=3, vmin=-3)
    ax1.coastlines()
    plt.title('SST anomaly December 1982 (degreeC)')

    # and add wind vectors
    q1=ax1.quiver(ds2.isel(time=month).lon[::4], ds2.isel(time=month).lat[::4], ds2.uwnd[month,0,::4,::4], ds3.vwnd[month,0,::4,::4]) # (lon,lat,u,v) 
    # arrows at every 4th points

    plt.quiverkey(q1, 0.70, 0.8, 10, '10 m/s', labelpos='E', coordinates='figure') # (Q,X,Y,U,label)
    plt.title(f'{get_month(month)} avg SST and wind')
    plt.savefig(f'homework2/generated/avg-wind-{get_month(month)}-m.png')
    plt.show()

# plot_avg_wind_m(0)
plot_avg_wind_m(11)