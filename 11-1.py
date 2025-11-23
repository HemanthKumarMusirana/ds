from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

# Create Figure
fig = plt.figure(num=None, figsize=(12, 8))

# Create Basemap
m = Basemap(
    projection='merc',
    llcrnrlat=-80,
    urcrnrlat=80,
    llcrnrlon=-180,
    urcrnrlon=180,
    resolution='c'
)

# Draw Coastlines
m.drawcoastlines()

# Title
plt.title("Mercator Projection")

# Show Output
plt.show()
