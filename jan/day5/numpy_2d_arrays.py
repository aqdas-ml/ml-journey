import numpy as np
array_2d = np.array([
    [2,3,5],
    [7,8,6]
])
print("Matrix:\n",array_2d)
print("Shape",array_2d.shape)
print("First Row:",array_2d[0])
print("First Column:\n", array_2d[:,:1])
print("Reshape:\n", array_2d.reshape(3,2))
