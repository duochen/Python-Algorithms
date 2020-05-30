import time

def method1(numbers):
    start = time.perf_counter()
    n = len(numbers)
    #just find biggest two numbers
    num1 = max(numbers)
    numbers.remove(num1)
    num2 = max(numbers)
    result = num1 * num2
    end = time.perf_counter()
    print(end-start)
    return result

def method2(numbers):
    start = time.perf_counter()
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])
    end = time.perf_counter()
    print(end-start)    
    return max_product

def max_pairwise_product(numbers):
    # method1(numbers)
    method2(numbers)
    
if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))