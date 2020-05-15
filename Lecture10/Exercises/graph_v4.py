# Add a vertex

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
g.add_vertex('f')
print(g.get_vertices())
