def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

###############################################

number = input('Enter number: ')
n = int(number)
f = factorial(n)
print(f'Factorial({n}): {f}')