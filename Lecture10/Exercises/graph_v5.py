# Add an edge

class graph:
    def __init__(self, dict = None):
        if dict is None:
            dict = {}
        self.dict = dict

    def add_vertex(self, vertex):
        if vertex not in self.dict:
            self.dict[vertex] = []

    def get_vertices(self):
        return list(self.dict.keys())

    def add_edge(self, edge):
        edge = set(edge)
        (v1, v2) = tuple(edge)
        if v1 in self.dict:
            self.dict[v1].append(v2)
        else:
            self.dict[v1] = v2

    def get_edges(self):
        edges = []
        for key in self.dict:
            for value in self.dict[key]:
                if {value, key} not in edges:
                    edges.append({key, value})
        return edges 

#####################################

dict = {
    "a": ["b", "c"],
    "b" : [ "a" , "d" ],
    "c" : [ "a" , "d" ],
    "d" : [ "e" ],
    "e" : [ "d" ]
}

g = graph(dict)
g.add_edge({'a', 'e'})
g.add_edge({'a', 'c'})
print(g.get_edges())
