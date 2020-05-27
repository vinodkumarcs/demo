#------------------------------------------#
# Exercise on Creating Standard Graphics
#------------------------------------------#
import numpy as np
from numpy.random import randn
import pandas as pd
from pandas import Series, DataFrame

import matplotlib.pyplot as plt
from matplotlib import rcParams

#========================================#
#     Generating Line Charts
#========================================#
x=range(1,10)
y=[1,2,3,4,0,4,3,2,1]
plt.plot(x,y)

# Please note you need to execute show() method to display the graph in IDLE environment
# unlike in some other ENV like Jupyter Notes etc.
plt.show()

#-------------------------------------------------#
# Lets generate Line Plot for mpg of Cars object  #
#-------------------------------------------------#
address='C:\VINOD\Technical\SourceCode\Python\DATA\mtcars.csv'
cars=pd.read_csv(address)
print (cars.head())

mpg=cars['mpg']
# Note that mpg assigned as above becomes an array of 32 elements.
# We can simply Line Plot the mpg where the indices 0 thru 31 is taken as x-cordinate and the corresponding
# element value as y-cordinate
print (mpg)
mpg.plot()
plt.show()


#---------------------------------------------------------#
#  Lets draw Line chart for 3 variables wt,cyl,mpg        #
#---------------------------------------------------------#
df=cars[ ['cyl','wt','mpg'] ]
df.plot()
plt.show()

#============================================#
#       Generating BAR Graphs
#============================================#

x=range(1,10)
y=[1,2,3,4,0,4,3,2,1]
plt.bar(x,y)
plt.show()

# Lets draw Bar Graph from our Pandas mpg variable
mpg.plot(kind="bar")
plt.show()

# Lets do horizontal Bars
mpg.plot(kind="barh")
plt.show()

#============================================#
#       Generating Pie Charts
#============================================#
x=[1,2,5.6,5,3]
plt.pie(x)
plt.show()

#===========================================#
#          Saving the Plots
#-------------------------------------------#
x=[1,2,5.6,5,3]
plt.pie(x)
plt.savefig('C:\VINOD\Technical\SourceCode\Python\DATA\pie.png')
plt.show()












