str1 = "machine learning"
print("Uppercase: ", str1.upper())

vowels = "aeiou"
count = 0
for i in str1.lower():
    if i in vowels:
        count += 1
 
print("Vowel count:", count)
print("Reversed:", str1[::-1])
