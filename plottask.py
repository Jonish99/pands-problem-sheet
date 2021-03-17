'''
A program that plots the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.



'''

#Author: Jon Ishaque

#imports
import matplotlib.pyplot as plt
import numpy as np 

#create f(x)=x arrays
#x inputs for funciton range 0 - 4
#Range funcitons includes starts at first parameter and upto but not including 2nd parameter -(numpy.arange — NumPy v1.20 Manual, 2021)
xPoints =np.array(range(0,5))
yPointsf = xPoints 

#create g(x)=x2 - 'g'
yPointsg = xPoints * xPoints

#create h(x)=x3 - 'h'
yPointsh = xPoints * xPoints * xPoints

#create plotss with labels for legend and defined colors, labels and defined width.
#plot function f
plt.plot(xPoints,yPointsf, label="f(x)=x", color='blue', linewidth = 2)

#plot function g
plt.plot(xPoints,yPointsg, label="g(x)=x2", color='green', linewidth = 2)


#plot function h
plt.plot(xPoints,yPointsh, label="h(x)=x3", color='red', linewidth = 2 )

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

#xaxes upto 4
plt.xlim(0, 4)
#y axes max should be upto 64
plt.ylim(0, 64)


#show the plot
plt.show()

#save the plot
plt.savefig("Three functions.png")