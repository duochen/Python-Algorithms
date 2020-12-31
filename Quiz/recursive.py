def my_recursive_function(n):
    if n == 0:
        return
    print(n)
    my_recursive_function(n-1)

my_recursive_function(4)