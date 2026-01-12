items = ["Apple", "Banana", "Apple", "Orange", "Banana", "Apple"]

frequency = {}
for i in items:
    if i in frequency:
        frequency[i] += 1
      
    else:
        frequency[i] = 1

print("Frequency count:")
print(frequency)
