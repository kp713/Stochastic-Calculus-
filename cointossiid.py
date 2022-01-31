# -*- coding: utf-8 -*-
"""
Created on Wed Jan 1 10:21:45 2020

@author: Krishnapriya
"""
###Experiment and visualization that a coin toss (fair) is independently and identically distributeds
#%%
import numpy as np
import pandas as pd
import random
import matplotlib.pyplot as plt 
np.random.seed(42)
n = 1
p = 0.5
np.random.binomial(n,p)
#%%
success = 0
counter = 0
log = []
while counter < 1000 :
  toss = np.random.binomial(1,p)
  log.append( toss)
  counter = counter +1
  if toss == 1 :
        success =success +1
        
print("number of heads i.e successes =", success)
l =[]
for i in range (0,1000) :
    if log[i] == 1:
        l.append(i)
plt.hist(l, 20, (0,1000), 
      histtype = 'bar', rwidth = 1) 
#%%
randint(toss)
#%%
m
#%%
l =[]
for i in range (0,1000) :
    if log[i] == 1:
        l.append(i)
        #%%
        coinflips =np.zeros(1000)
        #%%
        coinflips[l] =1
        #%%
plt.hist(l, 20, (0,1000), 
        histtype = 'bar', rwidth = 1) 
#%%
plt.show()
