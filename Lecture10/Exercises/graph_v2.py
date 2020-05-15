# Display graph vertices

class graph:
    def __init__(self, dict = None):
        if dict is None:
            dict = []
        self.dict = dict
    
    def get_vertices(self):
        return list(self.dict.keys())


#####################################

dict = {
    "a": ["b", "c"],
    "b" : [ "a" , "d" ],
    "c" : [ "a" , "d" ],
    "d" : [ "e" ],
    "e" : [ "d" ]
}

g = graph(dict)
print(g.get_vertices())
