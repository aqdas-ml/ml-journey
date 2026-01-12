with open("sample.txt", "r") as file:
    lines = file.readlines()

line_count = len(lines)
word_count = 0

for line in lines:
    words = line.split()
    word_count += len(words)
    
print("Number of lines",line_count)
print("Number of words",word_count)
