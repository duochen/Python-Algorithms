# Measure the time
# python -m timeit "import sum1; sum1.sum1(10)"
def sum1(n):
    final_sum = 0

    for x in range(n+1):
        final_sum += x

    return final_sum

###############################
print(sum1(10))