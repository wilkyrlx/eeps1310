import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

grace_path1 = 'final-project\\data-small\\GRACEDADM_CLSM025GL_7D.A20030203.030.nc4'
grace_path2 = 'final-project\\data-small\\GRACEDADM_CLSM025GL_7D.A20221226.030.nc4'

grace_path = [grace_path1, grace_path2]
grace = xr.open_mfdataset(grace_path)['gws_inst']

# Compute the difference between the two datasets
grace_diff = grace.sel(time='2022-12-26') - grace.sel(time='2003-02-03')


# Plot the data
ax = plt.axes(projection=ccrs.PlateCarree())
extent = [-125, -65, 24, 50]  # [min_longitude, max_longitude, min_latitude, max_latitude]
ax.set_extent(extent)
ax.coastlines()
ax.add_feature(cfeature.STATES, edgecolor='white', linewidth=0.5)
grace_diff.plot(ax=ax, transform=ccrs.PlateCarree())
plt.show()

