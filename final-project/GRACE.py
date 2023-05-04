import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# !!! CONTROL VARIABLES !!!
# bounding box for map [min_longitude, max_longitude, min_latitude, max_latitude]
# extent = [-125, -65, 24, 50]  # United States
extent = [-82, -72, 38, 45]     # New York and Pennsylvania, zoomed out
# !!! CONTROL VARIABLES !!!

grace_path1 = 'final-project\\data-penn\\GRACEDADM_CLSM025GL_7D.A20220606.030.nc4'
grace_path2 = 'final-project\\data-penn\\GRACEDADM_CLSM025GL_7D.A20030602.030.nc4'


grace_path = [grace_path1, grace_path2]
grace = xr.open_mfdataset(grace_path)['gws_inst']

# Compute the difference between the two datasets
grace_diff = grace.sel(time='2022-06-06')  - grace.sel(time='2003-06-02')


# Plot the data
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(extent)
ax.coastlines()
ax.add_feature(cfeature.STATES, edgecolor='black', linewidth=0.5)
grace_diff.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='RdBu', cbar_kwargs={'label': 'Groundwater Storage Percentile', 'shrink': 0.6})
# plt.title('GRACE Groundwater Storage Change from 2022 to 2003, July')
plt.show()

