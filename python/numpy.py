import numpy as np

# Create a 1-dimensional array
arr = np.array([1, 2, 3, 4, 5])

# Perform iteration over the array
print("Array elements:")
for num in arr:
    print(num)

# Perform slicing operation
print("\nSliced array:")
sliced_arr = arr[1:4]  # Slicing from index 1 to index 3 (exclusive)
print(sliced_arr)
