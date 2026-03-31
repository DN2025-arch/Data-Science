import matplotlib.pyplot as plt
import numpy as np

# Histogram - frequency chart
bins = [0,10,20,30,40,50,60,70,80,90,100]
ages = [30,40,52,64,54,87,69,58,67,99,88]

plt.hist(ages,bins, histtype="bar", rwidth=0.8)
plt.xlabel("Age Interval")
plt.ylabel("Frequency")
plt.title("Histogram")
plt.show()

# Pie Chart

activities = ["Football","Basketball","Swimming","Volleyball","Tennis"]
slices = [71,60,24,25,6] # How many people are doing the activities
colors = ["r","g","b","m","c"]

plt.pie(slices, labels=activities,colors=colors, startangle=90)
plt.title("Daily Activity Chart")
plt.show()

# Stack Plot

days    = [2,3,4,5,6     ]
eating  = [30,29,39,50,43]
playing = [42,12,30,56,78]
dancing = [98,54,67,83,24]
working = [90,79,59,87,65]
plt.plot([],[],color="r",label='eating',linewidth=3)
plt.plot([],[],color="g",label='playing',linewidth=3)
plt.plot([],[],color="b",label='dancing',linewidth=3)
plt.plot([],[],color="m",label='working',linewidth=3)

plt.stackplot(days,eating,playing,dancing,working,colors=["g","b","r","m"]) # Border Colours
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("Stack Plot")

plt.show()
