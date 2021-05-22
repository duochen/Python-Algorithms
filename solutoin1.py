def findPair(A, sum):
    # consider each element except that lastt
    for i in range(len(A) - 1):
        # start from ith element until the last element
        for j in range(i + 1, len(A)):
            # if the desired sum is found, print it
            if A[i] + A[j] == sum:
                print("Pair found", (A[i], A[j]))
                return

    print("Pair not found")
            


A = [8, 7, 2, 5, 3, 1]
sum = 10
 
findPair(A, sum)