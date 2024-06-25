# NumPy
# NumPy (Numerical Python) is a powerful library for numerical computing in Python.
# It provides support for arrays, mathematical functions, random number generation, and more.
# NumPy is the foundation of many other scientific computing libraries in Python, such as SciPy, Pandas, and Matplotlib.

# Installing
# NumPy can be installed using pip:
# pip install numpy

import numpy as np

# Creating Arrays
array_1d = np.array([1, 2, 3, 4, 5])
print("1D Array:", array_1d)

# Multi-dimensional Arrays
array_2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Array:\n", array_2d)

array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("3D Array:\n", array_3d)

# Arrays with Zeros, Ones, or a Range of Values
zeros_array = np.zeros((3, 3))
print("Array of Zeros:\n", zeros_array)

ones_array = np.ones((2, 4))
print("Array of Ones:\n", ones_array)

range_array = np.arange(10, 20)
print("Array with Range of Values:", range_array)

linspace_array = np.linspace(0, 1, 5)
print("Array with Evenly Spaced Values:", linspace_array)

# Indexing and Slicing
array = np.array([10, 20, 30, 40, 50])

# Indexing: Accessing individual elements
first_element = array[0]
print("First Element:", first_element)

# Slicing: Accessing a range of elements
slice_array = array[1:4]
print("Sliced Array:", slice_array)

# Multi-dimensional array slicing
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
slice_2d = array_2d[1:, 1:]
print("2D Array Slicing:\n", slice_2d)

# Boolean indexing
boolean_indexed_array = array[array > 20]
print("Boolean Indexed Array:", boolean_indexed_array)

# Aggregation Functions
# 1. Sum, mean, max, min:
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))
print(np.mean(arr))
print(np.max(arr))
print(np.min(arr))

# 2. Axis-specific operations:
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr_2d, axis=0))  # Output: [5 7 9]
print(np.sum(arr_2d, axis=1))  # Output: [ 6 15]

# Broadcasting
# 1. Broadcasting example
arr = np.array([1, 2, 3])
arr_2d = np.array([[1], [2], [3]])

result = arr + arr_2d
print(result)

# Linear Algebra
# 1. Dot product:
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

dot_product = np.dot(a, b)
print(dot_product)

# 2. Transpose:
a = np.array([[1, 2], [3, 4]])
print(a.T)

# Random Numbers
# 1. Generating random numbers:
rand_arr = np.random.rand(2, 3)
rand_int = np.random.randint(0, 10, (2, 3))
print("Random Float Array:\n", rand_arr)
print("Random Integer Array:\n", rand_int)
