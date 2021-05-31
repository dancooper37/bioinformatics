def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        n = fibonacci(n - 1) + fibonacci(n - 2)
    return n


print(fibonacci(20))