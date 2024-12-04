def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))  # Output: 120

try:
    print(factorial(-1)) # Output: ValueError: Factorial is not defined for negative numbers.
except ValueError as e:
    print(e) 