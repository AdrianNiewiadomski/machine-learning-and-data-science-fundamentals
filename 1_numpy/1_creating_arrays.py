import numpy as np

my_list = [1, 2, 3]
print("my_list: ", my_list)

# We can create a numpy array from the ordinary list by:
my_numpy_array = np.array(my_list)
print("my_numpy_array: ", my_numpy_array)
print("type(my_numpy_array): ", type(my_numpy_array))

my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("my_matrix: ", my_matrix)

# The same is true for matrices:
my_numpy_matrix = np.array(my_matrix)
print("my_numpy_matrix: \n", my_numpy_matrix)
print("type(my_numpy_matrix: ", type(my_numpy_matrix))

# To create an array, we may use a range function
print("np.array(range(1, 7, 2)): ", np.array(range(1, 7, 2)))
# or, we may use np.arange:
print("np.arange(1, 7, 2): ", np.arange(1, 7, 2))

# To create an array full of zeros, simply use the following:
print("np.zeros(3): ", np.zeros(3, int))
# The first argument of method zeros is shape. To specify shape you can pass an integer or tuple:
print("np.zeros((3, 2)): \n", np.zeros((3, 2)))

# Similarly, you can create an array full of ones:
print("np.ones((1, 1), float): ", np.ones((1, 1), float))

# To create an identity matrix use:
print("np.eye(3): \n", np.eye(3))

# To create an array with linearly changing values you may use:
print("np.linspace(1, 2, 11): ", np.linspace(1, 2, 11))
