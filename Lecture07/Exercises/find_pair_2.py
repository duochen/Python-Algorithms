# # https://www.techiedelight.com/find-pair-with-given-sum-array/

# Function to find a pair in an array with a given sum using hashing
def findPair(A, sum):
 
    # create an empty dictionary
    dict = {}
 
    # do for each element
    for i, e in enumerate(A):
 
        # check if pair `(e, sum - e)` exists
 
        # if the difference is seen before, print the pair
        if sum - e in dict:
            print("Pair found", (A[dict.get(sum - e)], A[i]))
            return
 
        # store index of the current element in the dictionary
        dict[e] = i
 
    # No pair with the given sum exists in the list
    print("Pair not found")
 
 
if __name__ == '__main__':
 
    A = [8, 7, 2, 5, 3, 1]
    sum = 10
 
    findPair(A, sum)