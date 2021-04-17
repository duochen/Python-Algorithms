def compute(n):
    val = 0
    for i in range(n):
        for j in range(i):
            val += 1

    return val

print(compute(5))