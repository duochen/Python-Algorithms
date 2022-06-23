class Graph:
    def __init__(self, gdict=None):
        if gdict == None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

    def bfs(self, vertex):
        visited = [vertex]
        queue = [vertex]
        while queue:
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)

    def dfs(self, vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    stack.append(adjacentVertex)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.g

customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "g"],
    "c": ["a", "d", "e"],
    "d": ["b", "c", "f"],
    "e": ["c", "f"],
    "f": ["d", "e", "g"],
    "g": ["b", "f"]
}

graph = Graph(customDict)
# graph.addEdge("e", "c")
# print(graph.gdict["e"])
graph.dfs('a')
graph.bfs('a')