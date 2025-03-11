def factorial_iterative(n):
    if n < 0:
        return "Factorial does not exist for negative numbers"
    elif n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
number = 5
print(f"The factorial of {number} is {factorial_iterative(number)}")
