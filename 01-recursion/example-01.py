def factorial(n):
    """Factorial of a number is the product of multiplication of
    all integers from 1 to that number. Factorial of 0 equals 1.
    e.g. 6! = 1 * 2 * 3 * 4 * 5 * 6
    """
    print(f"Calculating {n}!")
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(f"6! = {factorial(6)}")
