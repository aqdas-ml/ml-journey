import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv("Student.csv")

plt.hist(dataset["Marks"].dropna(), bins=5)
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()
