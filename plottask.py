'''
A program that plots the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.



'''

#Author: Jon Ishaque

#imports
import matplotlib.pyplot as plt
import numpy as np 

#create f(xa)=x arrays -'f'
xpoints1 =np.array(range(0,4))
ypoints1 = xpoints1 

#create g(x)=x2
xpoints2 =np.array(range(0,4))
ypoints2 = xpoints2 *2

#create h(x)=x3
xpoints3 =np.array(range(0,4))
ypoints3 = xpoints3 * 3


#create a plot with lists as coordinates
plt.plot(xpoints,ypoints)
#add a title
#plt.title(label="y = x*x")
#add label to y axis
plt.ylabel=("Y axis")
#add label to x axis
plt.ylabel=("X axis")
#show the plot
plt.show()