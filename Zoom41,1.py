import matplotlib.pyplot as plt
import numpy as np

# Make The Data
x=[1,2,3,4,5]
y=[1,2,3,4,5]

plt.plot(x,y)
plt.show()

# Formatting
plt.plot(x,y,"b--") # ro= red circles, go= green circles, g^=green triangles, b--=blue dashes etc.
plt.show()

# Limit the graph on each axis
plt.plot(x,y)
plt.axis([0,10,0,200]) #From x0 to x10, and from y0 to y200
plt.show()

# Making the graph visual better
plt.plot(x,y,"r-", label="age to years", linewidth="5")
plt.axis([0,10,0,10])
plt.xlabel("Age")
plt.ylabel("Time (Years)")
plt.title("Age Linked to Time")
plt.legend()
plt.show()

# Multiple graphs on a single plot
plt.plot(x,y,"r--", label="Y=X^2",linewidth=3)
plt.plot([1,3,5,7,9],[1,9,25,49,81])
plt.axis([0,10,0,100])
plt.xlabel("x")
plt.ylabel("y")
plt.title("y=x^2")
plt.legend()
plt.show()

plt.show()

# Task - Ask the user for input m and c and plot the line y = mx + c using matplotlib
print("y=mx+c")
m = int(input("m= "))
c = int(input("c= "))
x = np.arange(1,11,1)
y = []
for xval in x:
    y.append(m*xval + c)
print(y)
plt.plot(x,y)
plt.title("y=mx+c")
plt.axis([0,100,0,100])
plt.show()

# Bar plot
x = np.arange(1,11,1)
y = np.arange(1,40,4)
z = np.arange(1,30,3)
plt.bar(x,y)
plt.bar(x,z)
plt.show()

# Categorical data on bar plots
plt.bar(["Male","Female"],[90,87])
plt.show()

# HW: use numpy arange to generate x values from -5 to 5 with step 0.1. Then plot y=x, y=x^2,y=x^3

x = np.arange(-5,5.1,0.1)
y1 = []
y2 = []
y3 = []
for value in x:
    y1.append(value)
    y2.append(value**2)
    y3.append(value**3)

plt.plot(x,y1,"ro")
plt.plot(x,y2,"go")
plt.plot(x,y3,"bo")

plt.title("Linear, Quadratic and Cubic Graphs")
plt.xlabel("x")
plt.ylabel("y")

plt.show()
