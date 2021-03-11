'''
A program that plots the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.



'''

#Author: Jon Ishaque

#imports
import matplotlib.pyplot as plt
import numpy as np 

#create f(xa)=x arrays -'f'
#x inputs constant for 3 functions
xpoints =np.array(range(0,4))
ypoints1 = xpoints 

#create g(x)=x2 - 'g'
ypoints2 = xpoints * 2

#create h(x)=x3 - 'h'

ypoints3 = xpoints * 3


#create s, add label so legend and line colors are synched

#plot function f
plt.plot(xpoints,ypoints1, label="f(x)=x")

#plot function g
plt.plot(xpoints,ypoints2,label="g(x)=x2")

#plot function h
plt.plot(xpoints,ypoints3,label="h(x)=x3")
#add legend with best location
plt.legend(loc="best")
#
#add a title
plt.title(label="Plot showing 3 functions")
#add label to y axis
plt.ylabel=("Y axis")
#add label to x axis
plt.xlabel=("X axis")
#show the plot
print (ypoints3)
plt.plot(range(5))

#axes upto 8
plt.xlim(0, 8)
plt.ylim(0, 8)


#show the plot
plt.show()

#save the plot
plt.savefig("Three functions.png")