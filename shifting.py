# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 19:21:41 2020

@author: Krishnapriya
"""

#%%

###Visualizatio of the shifted geometric distribution
# Import geom, matplotlib.pyplot, and seaborn
from scipy.stats import geom
import matplotlib.pyplot
import seaborn as sns

# Create the sample
sample = 1+geom.rvs(p=0.5, size=10000, random_state=13)

# Plot the sample
sns.distplot(sample, bins = np.linspace(0,20,21), kde=False)
plt.show()
