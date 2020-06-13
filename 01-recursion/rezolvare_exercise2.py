def fibonacci(n):
    if n < 0:
        return ''
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


sir = ''
for i in range(20):
    sir += str(fibonacci(i)) + ' '
print(sir)