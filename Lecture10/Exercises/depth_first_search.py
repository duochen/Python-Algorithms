# Depth first search

class graph:
    def __init__(self, dict = None):
        if dict is None :
            dict = {}
        self . dict = dict

def depth_first_search(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print (start)
    for next in graph[start] - visited:
        depth_first_search(graph, next, visited)
    return visited

##########################################    

dict = {"a" : set(["b" , "c"]),
        "b" : set(["a", "d"]),
        "c" : set(["a", "d"]),
        "d" : set(["e"]),
        "e" : set(["a"])
}

depth_first_search( dict, 'a' )