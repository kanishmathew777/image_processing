import seaborn as sns
import matplotlib.pyplot as plt
import cv2
import numpy as np
import pandas as pd
from scipy.ndimage.filters import gaussian_filter
from scipy.interpolate import griddata

# create data
# x = np.random.rand(80) - 0.5
# y = x + np.random.rand(80)
# z = x + np.random.rand(80)
# df = pd.DataFrame({'x': x, 'y': y, 'z': z})
#
# # Plot with palette
# sns.lmplot(x='x', y='y', data=df, fit_reg=False, hue='x', legend=False, palette="Blues")
#
# # reverse palette
# sns.lmplot(x='x', y='y', data=df, fit_reg=False, hue='x', legend=False, palette="Blues_r")

img = cv2.imread("/home/kanish/Documents/ICR_advanced_forms/Advanced handwritting samples/scan/vandana_1.jpg", 0)

df2 = pd.DataFrame(img)

df3_smooth = gaussian_filter(df2, sigma=2)

# grid_z0 = griddata(points, values, (grid_x, grid_y), method='nearest')
# print(df2)

# flights = sns.load_dataset("flights")
# print(flights)
# flights = flights.pivot("month", "year", "passengers")
# ax = sns.heatmap(df3_smooth, xticklabels=False, yticklabels=False,
#                  cbar=False, robust=False, square=True, vmin=0, vmax=1)

plt.contour(df2, cmap='RdGy')

plt.colorbar()

# pixel_data_set =
plt.savefig("output.png", bbox_inches='tight', transparent=False)


plt.show()