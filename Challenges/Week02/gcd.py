def gcd_naive(a, b):
    m = max(a,b)
    n = min(a,b)
    if m%n ==0 :
        return n
    
    return gcd_naive(n,m%n)
    
#     current_gcd = 1
#     for d in range(2, min(a, b) + 1):
#         if a % d == 0 and b % d == 0:
#             if d > current_gcd:
#                 current_gcd = d

#     return current_gcd

if __name__ == "__main__":
    numbers = input("Enter two numbers:")
    a, b = map(int, numbers.split())
    print(gcd_naive(a, b))