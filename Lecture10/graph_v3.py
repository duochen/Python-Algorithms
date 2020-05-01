class graph:
    def __init__(self, dict = None):
        if dict is None:
            dict = {}
        self.dict = dict
    
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
print(g.get_edges())
