#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 16:58:01 2023

@author: tomthomas
"""
import numpy as np
import matplotlib.pyplot as plt

# read data from file
rawinput = np.genfromtxt('data0.csv', delimiter=',')

# derive the distribution of values by binning them into 32 bins with equal widths in the range from 2.0 to 5.0
# ohist contains numbers of entries in each bin, oedge contains bin boundaries
ohist, oedge = np.histogram(rawinput, bins=32, range=[2.0, 5.0])

# calculate bin centre locations and bin widths
xdst = 0.5*(oedge[1:]+oedge[:-1])
wdst = oedge[1:]-oedge[:-1]

# To normalise the distribution
# ydist is a discrete PDF
ydst = ohist/np.sum(ohist)

# Cumulative distribution
cdst = np.cumsum(ydst)


# plotting the probability density function
plt.figure(figsize=(11, 8))
plt.bar(xdst, ydst, width=0.9*wdst, color='green', label='75% of newborn')

plt.xlabel('Weights', fontsize=15)
plt.ylabel('Probability', fontsize=15)

# To find Mean value
mean = np.sum(xdst*ydst)
# And plot it
plt.plot([mean, mean], [0.0, max(ydst)], c='purple', label='Mean')
text = ''' Mean value: {}'''.format(mean.astype(float))
plt.text(x=3.3, y=0.106, s=text, fontsize=12, c='purple')

# Find the value of X such that 75% of new-borns from the distribution are born with a weight above X
indx = np.argmin(np.abs(cdst-.25))
xlow = oedge[indx]
plt.bar(xdst[0:indx], ydst[0:indx], width=0.9*wdst[0:indx])
plt.plot([xlow, xlow], [0.0, max(ydst)], c='red', label='X')
text = ''' 75% of newborns are\n born above weight{}'''.format(
    xlow.astype(float))
plt.text(x=2.3, y=0.1, s=text, fontsize=12, c='red')
plt.title("Weight distributions in newborns.")

plt.legend(loc='upper right')
plt.savefig("Weight distributions in newborns.png")
print("Mean =", mean)
print("Value of X =", xlow)
