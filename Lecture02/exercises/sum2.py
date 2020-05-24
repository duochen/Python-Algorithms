# Measure the time
# python -m timeit "import sum2; sum1.sum2(10)"
def sum2(n):
    return (n*(n+1))/2

#########################
print(sum2(10))