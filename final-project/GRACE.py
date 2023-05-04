import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# !!! CONTROL VARIABLES !!!
# bounding box for map [min_longitude, max_longitude, min_latitude, max_latitude]
selector = 0                # 0 for New York and Pennsylvania, 1 for Maine and New Hampshire
# extent = [-125, -65, 24, 50]  # United States
extent1 = [-82, -72, 38, 45]     # New York and Pennsylvania, zoomed out
extent2 = [-75.3, -66.8, 42.4, 47.2]     # Maine and New Hampshire, zoomed out
extent = [extent1, extent2][selector]
title_lables = ['NY/PA', 'ME/NH']

grace_path1 = 'final-project\\data-penn\\GRACEDADM_CLSM025GL_7D.A20200601.030.nc4'
grace_path2 = 'final-project\\data-penn\\GRACEDADM_CLSM025GL_7D.A20030609.030.nc4'
# !!! CONTROL VARIABLES !!!


grace_path = [grace_path1, grace_path2]
grace = xr.open_mfdataset(grace_path)['gws_inst']

# Compute the difference between the two datasets
# make negative because we want to see the change in groundwater storage, inversed
grace_diff = -(grace.sel(time='2020-06-01')  - grace.sel(time='2003-06-09'))


# Plot the data
ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(extent)
ax.coastlines()
ax.add_feature(cfeature.STATES, edgecolor='black', linewidth=0.5)
grace_diff.plot(ax=ax, transform=ccrs.PlateCarree(), cmap='RdBu', cbar_kwargs={'label': 'Groundwater Storage Percentile', 'shrink': 0.6})
plt.title(f'GRACE Groundwater Storage Change {title_lables[selector]} 2003-2020, July')
plt.show()

