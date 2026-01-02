num = int(input("Enter a Number: "))
if num < 0:
    print("Negative Number")
elif num > 0:
    print("Positive Number")
else:
    print("zero")

year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")
