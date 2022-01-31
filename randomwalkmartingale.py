# -*- coding: utf-8 -*-
"""
Created on Fri Jan 3 14:41:03 2020

@author: Krishnapriya
"""

#%%
# Python code for 1-D random walk. 
import random 
import numpy as np 
import matplotlib.pyplot as plt 
  
# Probability to move up or down 
prob = [0.05, 0.95]   
  
# statically defining the starting position 
start = 0  
positions = [start] 
  
# creating the random points 
rr = np.random.random(1000) 
downp = rr < prob[0] 
upp = rr > prob[1] 
  
  
for idownp, iupp in zip(downp, upp): 
    down = idownp and positions[-1] > 1
    up = iupp and positions[-1] < 4
    positions.append(positions[-1] - down + up) 
  
# plotting down the graph of the random walk in 1D 
plt.plot(positions) 
plt.show() 
#%%
#%%
p = 0.5
success = 0
counter = 0
log = []
rw =[]
c = 0
while counter < 1000 :
  toss = np.random.binomial(1,p)
  if toss == 1 :
      c = toss +c
  if toss != 1 :
      c =c-1
      
  log.append( toss)
  rw.append(c)
  counter = counter +1
  if toss == 1 :
        success =success +1
        
print("number of heads i.e successes =", success)
#%%
def calc_Expectation(a, n): 
      
    # variable prb is for probability  
    # of each element which is same for 
    # each element  
    prb = 1/n
      
    # calculating expectation overall 
    sum = 0
    for i in range(0, n): 
        sum += (a[i] * prb)  
          
    # returning expectation as sum 
    return float(sum)
#%%
expect = calc_Expectation(log, 1000 ) 
  
# Display expectation of given array 
print( "Expectation of array E(X) is : ", 
                                 expect ) 
#%%
conproblist =[]
conexp =[]
h=[]

for i in range (0,1000):
    
    g= list(filter(lambda x:x == rw[i], rw[0:i]))
    prob = len(g) / len(rw)
    exp = prob * rw[i]
    conexp.append(exp)
    conproblist.append(prob)
    
    h.append(g)
#%%
diffexp =[]
for i in range (0,999):
    k = conexp[i+1] - conexp[i]
    diffexp.append(k)

#%%
    k = conexp[999] - conexp[998]
    diffexp.append(k)

  #%%
  g= list(filter(lambda x:x == rw[170], rw))
  
  #%%
axes = plt.gca()
axes.set_xlim([0,1000])
axes.set_ylim([-5,5])

plt.plot(diffexp)
  #%%
  len(h[180])/len(rw)
  
  #%%
    
import random
from itertools import groupby
import statistics
import matplotlib.pyplot as plt
import numpy as np

# Function for biased coin
def flip(p): return 'H' if random.random() < p else 'T'

# Simulation
def simulate_three(X, N, Y, Z):
    Outcome = [] # List of results
    for i in range(X): # For loop for the X number of iterations
        flips = [flip(0.6) for j in range(N)] # For loop for N number of coin flips
        #print len(list(groupby(flips))), flips
        if len(list(groupby(flips))) > Z: # If group condition is met
           Outcome.append(len(list(groupby(flips)))) # store to list
    prob = (1.0*len((lambda x:x == 6, Outcome))) / len(Outcome) # conditional probability
    expval = (1.0*sum(Outcome))/(len(Outcome)) # conditional expectation
    zscore = (Y - expval) / statistics.stdev(Outcome) # by CLT, assuming IID variables, compute the z score
    print (prob)
    print (expval)
    print (zscore)
    weights = (1.0*np.ones_like(Outcome))/len(Outcome)
    plt.hist(Outcome, weights=weights, facecolor='green', alpha=0.75)
    plt.xlabel('#Groups')
    plt.ylabel('Conditional Probability of Groups | (> 5 groups)')
    plt.title('Conditional Probability Distribution')
    plt.grid(True)
    plt.show()

simulate_three(1000,10,6,5)
# 0.551198257081 : this is the conditional probability
# 6.64052287582  : this is the conditional expectation
# -0.773961977708 : this is the z-score
