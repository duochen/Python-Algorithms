def findPair(A, sum):
    # create an empty dictionary
    dict = {}

    # do for each element
    for i, e in enumerate(A):
        # Check if pair `(e, sum - e)` exists

        # if the difference is seen before, print the pair
        if sum - e in dict:
            print("Pair found", (A[dict.get(sum-e)], A[i]))
            return

        # store index of the current element in the dictionary
        dict[e] = i

    print("Pair not found")
            


A = [8, 7, 2, 5, 3, 1]
sum = 10
 
findPair(A, sum)