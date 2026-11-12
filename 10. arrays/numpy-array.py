import numpy as np

# 1D NumPy array
numbers = np.array([1, 2, 3, 4, 5])
print(numbers)

# 2D NumPy array
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)
print(matrix[0, 1])

# Mathematical operations
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
sum_array = array1 + array2
print(sum_array)