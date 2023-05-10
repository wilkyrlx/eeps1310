import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as cfeature

selector = 1               # 0 for New York and Pennsylvania, 1 for Maine and New Hampshire

# when adding new longitudes, remember to slap on a negative because the converters don't
if selector == 0:
    # extent, coords of NY and Penn
    extent = [-82, -72, 38, 45]     # New York and Pennsylvania, zoomed out
    lats = [40, 39.979167, 40.796, 40.445]
    lons = [-80.108333, -77.069167, -75.3110556, -75.250278]
else:
    # extent, coords of maine and new hampshire
    extent = [-73, -67, 42, 46]    
    lats = [44.7172222, 44.300278, 44.0372222, 43.3861111]
    lons = [-70.4233333, -69.765278, -70.3422222, -70.6591667]

colors = ['blue', 'orange', 'green', 'red']

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent(extent)
ax.coastlines()
ax.add_feature(cfeature.STATES, edgecolor='black', linewidth=0.5)
ax.scatter(lons, lats, transform=ccrs.PlateCarree(), marker='o', color=colors)
plt.show()