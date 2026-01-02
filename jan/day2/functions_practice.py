def is_even(num):
    if num % 2 == 0:
        return "number is Even"
    else:
        return "number is Odd"

def factorial(num):
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

def max_of_three(a, b, c):
    return max(a, b, c)

print(is_even(5))
print(factorial(4))
print(max_of_three(10,50,20))
