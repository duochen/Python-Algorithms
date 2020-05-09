from LinkedQueue import LinkedQueue 
import numpy as np

class Graph:
    def __init__(self, vertices):
        self.matrix = np.zeros((vertices, vertices))
        self.vertices = vertices

    def insert_edge(self, u, v, w = 1):
        self.matrix[u][v] = w

    def delete_edge(self, u, v):
        self.matrix[u][v] = 0

    def get_edge(self, u, v):
        return self.matrix[u][v]

    def vertices_count(self):
        return self.vertices

    def edges_count(self):
        count = 0
        for i in range(self.vertices):
            for j in range(self.vertices):
                if not self.matrix[i][j] == 0:
                    count += 1

        return count

    def indegree(self, u):
        count = 0
        for i in range(self.vertices):
            if not self.matrix[i][u] == 0:
                count += 1
        return count

    def outdegree(self, u):
        count = 0
        for i in range(self.vertices):
            if not self.matrix[u][i] == 0:
                count += 1
        return count

    def display(self):
        print(self.matrix)

    def BFS(self, source):
        i = source
        q = LinkedQueue()
        visited = [0] * self.vertices
        print(i, end= ' - ')
        visited[i] = 1
        q.enqueue(i)

        while not q.is_empty():
            i = q.dequeue()
            for j in range(self.vertices):
                if self.matrix[i][j] == 1 and visited[j] == 0:
                    print(j, end=' - ')
                    visited[j] = 1
                    q.enqueue(j)

#####################################
G = Graph(7)
G.insert_edge(0,1)
G.insert_edge(0,5)
G.insert_edge(0,6)
G.insert_edge(1,0)
G.insert_edge(1,2)
G.insert_edge(1,5)
G.insert_edge(1,6)
G.insert_edge(2,3)
G.insert_edge(2,4)
G.insert_edge(2,6)
G.insert_edge(3,4)
G.insert_edge(4,2)
G.insert_edge(4,5)
G.insert_edge(5,2)
G.insert_edge(5,3)
G.insert_edge(6,3)
print('Graph Matrix')
G.display()
G.BFS(0)



