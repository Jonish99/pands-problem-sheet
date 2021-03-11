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


#create a plot with lists as coordinates
#plot function f
plt.plot(xpoints,ypoints1)
#plot function g
plt.plot(xpoints,ypoints2)
#plot function h
plt.plot(xpoints,ypoints3)
plt.legend(["f(x)=x", "g(x)=x2","h(x)=x3"])
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

#axes upt to 12 to account for you = 4 * 3 on h function
plt.xlim(0, 12)
plt.ylim(0, 12)


#show the plot
plt.show()

#save the plot
plt.savefig("Three functions.png")