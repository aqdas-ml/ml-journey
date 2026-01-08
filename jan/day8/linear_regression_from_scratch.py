import numpy as np

# Sample data (hours studied vs score)
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 6, 8, 10])

# Mean of X and y
x_mean = np.mean(x)
y_mean = np.mean(y)

# Calculate slope (m) and intercept (c)
m = np.sum((y - y_mean)* (x - x_mean)) / np.sum((x - x_mean)**2)
c = y_mean - (m * x_mean)

print("Slope (m):", m)
print("Intercept (c):", c)

# Prediction
y_pred = m * x + c
print("Predicted values:", y_pred)
