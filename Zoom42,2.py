import matplotlib.pyplot as plt
import numpy as np
import random

# Traffic Task
hours = np.arange(0,25,1)
traffic_count = []
for value in hours:
    traffic_count.append(random.randint(20,50))

plt.bar(hours,traffic_count, width=0.8)
plt.title("Traffic Count throughout the Day")
plt.xlabel("Hours")
plt.ylabel("Number of Cars on street")
plt.xticks(range(25))
plt.show()

plt.plot(hours,traffic_count,"r-o")
plt.title("Traffic Count throughout the Day")
plt.xlabel("Hours")
plt.ylabel("Number of Cars on street")
plt.xticks(range(25))

highest_value = max(traffic_count)
corresponding_index = hours[traffic_count.index(highest_value)]

plt.annotate(
    f"Busiest Hour: {highest_value} cars!",
    xy=(corresponding_index,highest_value),
    xytext=(corresponding_index,highest_value-3),
    arrowprops=dict(facecolor="black",arrowstyle="->",lw=1.5),
    fontsize=11,
    fontweight="bold",
    color="darkred"
)

plt.show()

