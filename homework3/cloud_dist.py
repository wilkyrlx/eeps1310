import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs

path='eeps1310\\homework3\\'
datapath=path + 'data\\ISCCP.cloud.clim.nc'
generatedpath=path + 'generated\\'
ds1=xr.open_dataset(datapath)
ds1.close()

# print(ds1)

def plot_cloud_low():
    cmap1=plt.cm.Spectral_r
    fig1 = plt.figure(figsize=(9,5))
    ax1 = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    cs1=ds1.cloud_low.plot.pcolormesh(ax=ax1, transform=ccrs.PlateCarree(), cmap=cmap1, vmax=100, vmin=0)
    ax1.coastlines()
    plt.title('ISCCP cloud_low')
    plt.savefig(generatedpath + 'cloud_low.png')
    plt.show()

def plot_cloud_mid():
    cmap1=plt.cm.Spectral_r
    fig1 = plt.figure(figsize=(9,5))
    ax1 = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    cs1=ds1.cloud_mid.plot.pcolormesh(ax=ax1, transform=ccrs.PlateCarree(), cmap=cmap1, vmax=100, vmin=0)
    ax1.coastlines()
    plt.title('ISCCP cloud_mid')
    plt.savefig(generatedpath + 'cloud_mid.png')
    plt.show()

def plot_cloud_high():
    cmap1=plt.cm.Spectral_r
    fig1 = plt.figure(figsize=(9,5))
    ax1 = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    cs1=ds1.cloud_high.plot.pcolormesh(ax=ax1, transform=ccrs.PlateCarree(), cmap=cmap1, vmax=100, vmin=0)
    ax1.coastlines()
    plt.title('ISCCP cloud_high')
    plt.savefig(generatedpath + 'cloud_high.png')
    plt.show()

def plot_cloud_total():
    cmap1=plt.cm.Spectral_r
    fig1 = plt.figure(figsize=(9,5))
    ax1 = plt.axes(projection=ccrs.PlateCarree(central_longitude=180))
    cs1=ds1.cloud_tot.plot.pcolormesh(ax=ax1, transform=ccrs.PlateCarree(), cmap=cmap1, vmax=100, vmin=0)
    ax1.coastlines()
    plt.title('ISCCP cloud_total')
    plt.savefig(generatedpath + 'cloud_total.png')
    plt.show()

plot_cloud_low()
plot_cloud_mid()
plot_cloud_high()
plot_cloud_total()