#!/usr/bin/env python
# coding: utf-8

# In[33]:


import pandas as pd
import matplotlib.pyplot as plt
import descartes
import geopandas as gpd
from shapely.geometry import Point, Polygon

get_ipython().run_line_magic('matplotlib', 'inline')

data = pd.read_excel("C:/Users/edwinbeka/Documents/Interview Challenge.xlsx")

crs = {'init': 'espg:4326'}
data = data.rename(columns = {"longitudes/0":"longitudes", "latitudes/0":"latitudes"})


geometry = [Point(xy) for xy in zip (data["longitudes"], data["latitudes"])]
data.head()
BBox = ((data.longitudes.min(), data.longitudes.max(),data.latitudes.min(), data.latitudes.max()))


#geometry.append[geometry]
plt.plot(data["longitudes"], data["latitudes"])
fig, ax = plt.subplots(figsize = (8,7))
ax.scatter(data["longitudes"], data["latitudes"])


# In[ ]:





# In[ ]:





# In[ ]:




