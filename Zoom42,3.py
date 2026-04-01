import matplotlib.pyplot as plt
import numpy as np
import random

# check document for hw

monthly_expenses = ["Rent","Food","Transport","Entertainment","Savings"]
expenses = [1000,100,50,200,650]
colors=["g","r","b","m","c"]

plt.pie(expenses,labels=monthly_expenses,colors=colors,startangle=90,shadow=True)
plt.title("Personal Finance")

peak_expense = max(expenses)
peak_index = monthly_expenses[expenses.index(peak_expense)]

print(f"Highest Expense Category: {peak_index}")

plt.show()
