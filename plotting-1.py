# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 17:53:34 2016

@author: jnason
"""

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponential = []

for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponential.append(1.5**i)
    
#print(mySamples)

import pylab as plt

#both lists MUST be the same length, x values and y values
#plt.plot(mySamples, myExponential)    
#plt.plot(mySamples, myCubic)    
"""
plt.figure('lin')
plt.clf
plt.title('Linear')
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.plot(mySamples, myLinear)

plt.figure('quad')
plt.clf
plt.ylim(0, 30)
plt.plot(mySamples, myQuadratic)

"""
plt.figure('lin quad')
plt.clf
plt.title('Linear vs. Quadratic')
plt.xlabel('X Label')
plt.ylabel('Y label')
plt.ylim(0, 100)
plt.plot(mySamples, myLinear, 'b-', label = 'linear', linewidth = 2.0)
plt.plot(mySamples, myQuadratic, 'ro', label = 'quadratic', linewidth = 3.0)
plt.legend(loc = 'upper right')

plt.figure('cube exp')
plt.clf()
plt.plot(mySamples, myCubic, 'g^', label = 'cubic', linewidth = 4.0)
plt.plot(mySamples, myExponential, 'r--', label = 'exponential', linewidth = 5.0)
plt.legend(loc = 'upper left')
plt.title('Cubic vs. Exponential')






