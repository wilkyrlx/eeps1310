import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# extent = [-82, -72, 38, 45]     # New York and Pennsylvania, zoomed out
# lats = [40, 40.796, 40.445]
# lons = [-80.108333, -75.3110556, -75.250278]

# extent of maine and new hampshire
extent = [-72, -68, 42, 46]    
lats = [44.7172222, 44.0372222, 43.3861111]
lons = [-70.4233333, -70.3422222, -70.6591667]

colors = ['blue', 'orange', 'green']

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(extent)
ax.coastlines()
ax.add_feature(cfeature.STATES, edgecolor='black', linewidth=0.5)
ax.scatter(lons, lats, transform=ccrs.PlateCarree(), marker='o', color=colors)
plt.show()