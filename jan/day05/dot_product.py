import numpy as np
a = np.array([2,3,4])
b = np.array([5,6,7])
dot = np.dot(a,b)
print("vectors dot product:",dot)

m1 = np.array([
    [1,2],
    [3,4]
])
m2 = np.array([
    [5,6],
    [7,8]
])

multiply = np.dot(m1,m2)
print("matrix Multiplication:\n",multiply)
