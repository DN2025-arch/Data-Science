import numpy as np

# Slicing is cutting down a list/array into smaller lists/arrays without copying it.

# Lists: start_index:end_index+1:steps
# end_index us exclusive

linear_array = np.array([1,2,3,4,5,6,7,8,9])
print(linear_array[0:6])
print(linear_array[::2])
print(linear_array[0:8:2])
print(linear_array[::-1])

multi_array = np.array([[1,2,3],[4,5,6],[7,8,9]]) #3x3 Matrix
print(multi_array[0:1,0:1]) # Row Slicing, Column Slicing
print(multi_array[0:2,0:1])
print(multi_array[0:1,0:2])
print(multi_array[0:2,0:2])
print(multi_array[0:2,1:2]) # Gets the values that are common in both row and column.


values = np.arange(1,50,1) # 7^2
task_array = np.array(values)
task_array = task_array.reshape(7,7)
print(task_array)

cross_section = task_array[2:5,2:5]
print(cross_section)

# Conditional Selections
k = np.array([1,2,3,4,5,6,7,8,9])

even_array = k[k%2==0] # Even Numbers
n = k[k==5]            # Certain Values

print(even_array)
print(n)


simple_array = np.array([1,2,3,4,5,6,7,8,9,10])
m = simple_array[simple_array<5] # Numbers under a certain value.
print(m)

#Increment each value in an array by 1.
#Method 1
for value in range(0,len(simple_array)):
    simple_array[value] += 1

#Method 2
simple_array += 1

print(simple_array)

#Array Math
array1 = np.array([[1,2],[3,4]])
array2 = np.array([[5,6],[7,8]])
print(array1+array2)
print(array1*array2) #Element-Wise
print(array1@array2) #Dot Multiplication

#Custom Function
def solve(l):
    return 2*l +3
lx = np.array([1,2,3,4,5])
ly = solve(lx)
print(ly)

# HW

"""
Build a choice-based program where the user will give the input for the type of equation (Linear/Quadratic)
 and take inputs for coefficients accordingly. Display the output values of the equation for x=0 to x=10. 
 Example: y=6x+3
"""
print("ax^2 + bx + c")
print("For linear expression, set a to 0.")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

expression_array = np.array([np.arange(1,11,1)])
print(expression_array)
def output_values(ar):#
    return a*ar**2 + b*ar + c
print(output_values(expression_array))

