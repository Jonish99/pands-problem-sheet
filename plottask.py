'''
A program that plots the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
'''

#Author: Jon Ishaque

#imports
import matplotlib.pyplot as plt
import numpy as np 

#create f(x)=x arrays
#x inputs for funciton range 0 - 4
#Range function includes starts at first parameter and upto but not including 2nd parameter -(numpy.arange — NumPy v1.20 Manual, 2021)

#create f(x)=x
xPoints =np.array(range(0,5)) # x array is the same for the 3 functions.
yPoints_f = xPoints 

#create g(x)=x2 - 'g'
yPoints_g = xPoints * xPoints

#create h(x)=x3 - 'h'
yPoints_h = xPoints * xPoints * xPoints

#create plotss with labels for legend and defined colors, labels and defined width.

#plot function f
plt.plot(xPoints,yPoints_f, label="f(x)=x", color='blue', linewidth = 2)

#plot function g
plt.plot(xPoints,yPoints_g, label="g(x)=x2", color='green', linewidth = 2)


#plot function h
plt.plot(xPoints,yPoints_h, label="h(x)=x3", color='red', linewidth = 2 )

#add legend with best location
plt.legend(loc="best")

#add a title
plt.title(label="Plot Showing 3 Functions")
#add label to y axis
plt.ylabel=("Y axis")
#add label to x axis
plt.xlabel=("X axis")
#show the plot

plt.plot(range(5))

#xaxes up to 4
plt.xlim(0, 4)
#y axes max should be up to 64
plt.ylim(0, 64)


#show the plot
#plt.show()

#save the plot
plt.savefig("Three_functions.png")