import numpy as np

my_list = [1,2,3,4,5,6]

my_array = np.array(my_list)

print(my_list)  # [1,2,3,4,5,6]
print(my_array) # [1 2 3 4 5 6]

"""
Numpy Operations: Dimensions and Shape
Dimensions: Number of dimensions/axes in the array. Use ndim function to find out the dimension.
Shape: Size of the array in each dimension/axis.
"""

my_array = np.array([[1,2],[3,4]])
print(my_array.ndim)
print(my_array.shape) # Columns then Rows

# Multidimensional Numpy Array
multi_array = np.array([[[1,2],[3,4]],
                        [[5,6],[7,8]]])
# An array in an array.
print(multi_array)
print(multi_array.ndim)
print(multi_array.shape)

# Accessing elements inside an Array
# First Row Number, Then Column Number, Both start with 0.
print(my_array[0][1]) # 1st Row, 2nd Column

# Creating an Array using a range of values:
arr = np.arange(0,10,2) #Start,End,Step
print(arr) # Prints [0 2 4 6 8] -> Last number excluded

# Reshaping an Array without chaing the items in it
# Example: 2x2 Matrix into a 1x4 Matrix or 4x1 Matrix.

my_array = np.array([[1,2,3],[4,5,6]])
reshape = my_array.reshape(1,6) # Into one row, six columns
print(reshape)
reshape = my_array.reshape(3,2) # Into three rows, two columns
print(reshape)
reshape = my_array.reshape(6,1) # Into six rows, one column
print(reshape)

# Random Shuffling
perm = np.random.permutation(arr) # Shuffles values around
print(perm)
# Sorting
sorted_arr = np.sort(perm)
print(sorted_arr)