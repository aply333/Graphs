# bfs attemtps
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = deque()
        queue.append(starting_vertex)
        visited = set()
        currPath = []
        routes = {}
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                currPath.append(currNode)
                if currNode == destination_vertex:
                    routes[len(currPath)] = currPath 
                else:
                    for neighbor in self.get_neighbors(currNode):
                        queue.append(neighbor)            
            if currNode == starting_vertex:
                currPath.clear()
                currPath.append(currNode)
        return routes[min(routes)]

#  another attempt
        queue = deque()
        queue.append(starting_vertex)
        visited = set()
        currPath = []
        routes = {}
        while len(queue) > 0:
            currNode = queue.popleft()
            if currNode not in visited:
                visited.add(currNode)
                currPath.append(currNode)
                if currNode == destination_vertex:
                    print("triggered")
                    routes[len(currPath)] = currPath 
                else:
                    for neighbor in self.get_neighbors(currNode):
                        queue.append(neighbor)            
            if currNode == starting_vertex:
                print("cleared")
                currPath.clear()
                currPath.append(currNode)
        return routes[min(routes)]