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
filename2="uwnd.10m.mon.ltm.nc"
filename3="vwnd.10m.mon.ltm.nc"
with xr.open_dataset(file_loc2+filename2) as ds2:      
    print(ds2)
with xr.open_dataset(file_loc2+filename3) as ds3:      
    print(ds3)

sst=ds1.sst.sel(time=slice('1980','2020'))

def plot_avg_wind(month):
    cmap1=plt.cm.Spectral_r
    fig1 = plt.figure(figsize=(9,5))
    ax1 = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    cs1=sst.isel(time=month).plot.pcolormesh(ax=ax1, transform=ccrs.PlateCarree(), cmap=cmap1, vmax=40, vmin=-10)
    ax1.coastlines()

    # and add wind vectors
    q1=ax1.quiver(ds2.isel(time=month).lon[::4], ds2.isel(time=month).lat[::4], ds2.uwnd[month,0,::4,::4], ds3.vwnd[month,0,::4,::4]) # (lon,lat,u,v) 
    # arrows at every 4th points

    plt.quiverkey(q1, 0.70, 0.8, 10, '10 m/s', labelpos='E', coordinates='figure') # (Q,X,Y,U,label)
    plt.title(f'{get_month(month)} avg SST and wind')
    plt.savefig(f'homework2/generated/avg-wind-{get_month(month)}.png')
    plt.show()

plot_avg_wind(0)
plot_avg_wind(6)