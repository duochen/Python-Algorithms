# Breadth first search

import collections

class graph:
    def __init__(self, dict = None):
        if dict is None:
            dict = {}
        self . dict = dict

def breadth_first_search(graph, start):
    # Track the visited and unvisited nodes using queue
    seen, queue = set([start]), collections.deque([start])
    while queue:
        vertex = queue.popleft()
        print(vertex)
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)

#######################################################

dict = {"a" : set(["b", "c"]),
        "b" : set(["a", "d"]),
        "c" : set(["a", "d"]),
        "d" : set(["e"]),
        "e" : set(["a"])
}

breadth_first_search(dict, "a")

