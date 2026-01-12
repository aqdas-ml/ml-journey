with open("sample.txt","w") as file:
    file.write("Machine Learning starts with strong Python basics.\n")
    file.write("This is Day 3 practice.\n")

with open("sample.txt","r") as file:
    Content = file.read()
    
print("File Content:")
print(Content)
