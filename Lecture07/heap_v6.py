import heapq

L = []
heapq.heappush(L, 20)
heapq.heappush(L, 14)
heapq.heappush(L, 5)
heapq.heappush(L, 15)
heapq.heappush(L, 10)
heapq.heappush(L, 2)

print(L)
print(heapq.heappop(L))
print(L)
heapq.heappushpop(L, 18)
print(L)

L1 = heapq.nlargest(3, L)
print(L1)
L2 = heapq.nsmallest(3, L)
print(L2)

L3 = [20,14,2,15,10,21]
heapq.heapify(L3)
print(L3)