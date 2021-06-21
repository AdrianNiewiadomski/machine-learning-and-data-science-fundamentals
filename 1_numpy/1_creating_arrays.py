import numpy as np

print("Let us say that we have a list.")
my_list = [1, 2, 3]
print("my_list: ", my_list)

print("We can create a numpy array from the ordinary list by:")
my_numpy_array = np.array(my_list)
print("np.array(my_list): ", my_numpy_array)
print("type(np.array(my_list)): ", type(my_numpy_array))

print("\nThe same is true for matrices:")
my_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print("my_matrix: ", my_matrix)

my_numpy_matrix = np.array(my_matrix)
print("np.array(my_matrix): \n", my_numpy_matrix)
print("type(np.array(my_matrix)): ", type(my_numpy_matrix))

print("\nBe careful with matrices, however, because the lengths of the nested lists have to be equal.")
my_new_matrix = [[1], [4, 5], [7, 8, 9]]
print("my_new_matrix: ", my_new_matrix)
print("An attempt to call np.array(my_new_matrix) will result in an exception:")
print("VisibleDeprecationWarning: Creating an ndarray from ragged nested sequences (which is a list-or-tuple of "
      "lists-or-tuples-or ndarrays with different lengths or shapes) is deprecated. ...")

print("\nTo create a numpy array with lists of different lengths, you must specify a data type as an object.")
print("np.array(my_new_matrix, object): ", np.array(my_new_matrix, object))

print("\nTo create an array, we may use a range function:")
print("np.array(range(1, 7, 2)): ", np.array(range(1, 7, 2)))
print("or, we may use np.arange:")
print("np.arange(1, 7, 2): ", np.arange(1, 7, 2))

print("\nTo create an array full of zeros, simply use the following:")
print("np.zeros(3): ", np.zeros(3, int))
print("The first argument of method zeros is shape. To specify shape you can pass an integer or tuple:")
print("np.zeros((3, 2)): \n", np.zeros((3, 2)))

print("\nSimilarly, you can create an array full of ones:")
print("np.ones((1, 1), float): ", np.ones((1, 1), float))

print("\nTo create an identity matrix use:")
print("np.eye(3): \n", np.eye(3))

print("\nTo create an array with linearly changing values you may use:")
print("np.linspace(1, 2, 11): ", np.linspace(1, 2, 11))

print("\nTo create an array with random values:")
print("np.random.rand(3): ", np.random.rand(3))
print("This creates an array of a given shape "
      "and populates it with numbers of uniform distribution from [0, 1) interval.")

print("\nTo create an array with random values but with normal distribution N(0,1):")
print("np.random.rand(3): ", np.random.randn(3))
