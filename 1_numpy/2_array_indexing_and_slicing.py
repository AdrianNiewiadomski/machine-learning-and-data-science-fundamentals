import numpy as np

print("Let's say I have an array")
my_array = np.arange(11)
print("np.arange(11): ", np.arange(11))

print("\nTo get a single element you can use indexing.")
print("my_array[0]: ", my_array[0])

print("\nTo get a slice use notation known from slicing in python:")
print("my_array[:3]: ", my_array[:3])

print("\nNow let su create a matrix:")
my_matrix = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]])
print("my_matrix:\n", my_matrix)

print("\nWe can get a single element by:")
print("my_matrix[1][0]:", my_matrix[1][0])
print("As you can see the number in the first bracket is a number of the row, while the second number is a column.")

print("\nWe can get a numpy array by:")
print("my_matrix[:2][:2]: \n", my_matrix[:2][:2])
print("type(my_matrix[:2][:2]): ", type(my_matrix[:2][:2]))
