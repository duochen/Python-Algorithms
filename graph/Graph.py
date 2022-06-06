class Graph:
    def __init__(self, gdict=None):
        if gdict == None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)

customDict = {
    "a": ["b", "c"],
    "b": ["a", "d", "e"],
    "c": ["a", "e"],
    "d": ["b", "e", "f"],
    "e": ["b", "d", "f"],
    "f": ["d", "e"]
}

graph = Graph(customDict)
graph.addEdge("e", "c")
print(graph.gdict["e"])
