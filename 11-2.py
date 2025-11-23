from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import warnings
import matplotlib.cbook

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)

# Create Figure
fig = plt.figure(num=None, figsize=(12, 8))

# Create Basemap Object
m = Basemap(
    projection='merc',
    llcrnrlat=-80,
    urcrnrlat=80,
    llcrnrlon=-180,
    urcrnrlon=180,
    resolution='c'
)

# Draw coastlines
m.drawcoastlines()

# Fill continents
m.fillcontinents(color='tan', lake_color='lightblue')

# Draw parallels (latitude lines)
m.drawparallels(
    np.arange(-90, 91, 30),
    labels=[True, True, False, False],
    dashes=[2, 2]
)

# Draw meridians (longitude lines)
m.drawmeridians(
    np.arange(-180, 181, 60),
    labels=[False, False, False, True],
    dashes=[2, 2]
)

# Draw map boundary
m.drawmapboundary(fill_color='lightblue')

# Title
plt.title("Mercator Projection")

# Show output
plt.show()
