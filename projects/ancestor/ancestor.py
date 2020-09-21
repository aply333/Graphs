
def first_att_earliest_ancestor(ancestors, starting_node):
    storage = {}
    path_storage = {}

    def rec_func(node, currpath = []):
        if node not in storage:
            print(f"--|  EndCase: {node}")
            final_path = currpath
            final_path.append(node)
            path_storage[len(final_path)] = final_path
        else:
            for point in storage[node]:
                print(f"pointer {point}")
                newPath = currpath
                print(f"new path : {newPath}")
                newPath.append(node)
                print(f"new path after {newPath}")
                rec_func(point, newPath)

    for parent in ancestors:
        if parent[1] not in storage: 
            storage[parent[1]] = [parent[0]]
        else: 
            storage[parent[1]].append(parent[0])

    rec_func(starting_node)
    result = path_storage[max(path_storage)][-1]
    print(f"ALL PATHS ARE:{path_storage}")
    print(f"RESULT: {result}")
    if result == starting_node:
        return -1
    else: 
        return result

# END OF FIRST ATTEMPT

from collections import deque

class Graph:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]

def earliest_ancestor(ancestors, starting_node):
    ancestory_graph = Graph()
    for point in ancestors:
        ancestory_graph.add_vertex(point[0])
        ancestory_graph.add_vertex(point[1])
        ancestory_graph.add_edge(point[1], point[0])
    visited = set()
    stack = deque()
    stack.append([starting_node])
    storage = {}
    if len(ancestory_graph.vertices[starting_node])==0:
        return -1
    while len(stack) > 0:
        currPath = stack.pop()
        currNode = currPath[-1]
        if len(ancestory_graph.vertices[currNode]) == 0:
            if len(currPath) not in storage:
                storage[len(currPath)]=[currPath]
            else:
                storage[len(currPath)].append(currPath)
        if currNode not in visited:
            visited.add(currNode)
            for neighbor in ancestory_graph.get_neighbors(currNode):
                newPath = list(currPath)
                newPath.append(neighbor)
                stack.append(newPath)
    storMax = max(storage)
    if len(storage[storMax]) == 1:
        return storage[storMax][-1][-1]
    else:
        endpoints = []
        for path in storage[storMax]:
            endpoints.append(path[-1])
        return min(endpoints)


