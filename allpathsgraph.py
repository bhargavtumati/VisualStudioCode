class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adjList = [[] for _ in range(vertices)]

    def addEdge(self, u, v):
        self.adjList[u].append(v)

    def printAllPaths(self, s):
        visited = [False] * self.v
        pathList = [s]
        self.printAllPathsUtil(s, visited, pathList)

    def printAllPathsUtil(self, u, visited, localPathList):
        visited[u] = True
        for i in self.adjList[u]:
            if not visited[i]:
                localPathList.append(i)
                #if i==2:   #for destination
                print(localPathList)
                self.printAllPathsUtil(i, visited, localPathList)
                localPathList.pop()

        visited[u] = False

# Example usage
g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(0, 3)


source = 0
print(f"Paths from source {source} to all vertices:")
g.printAllPaths(source)
