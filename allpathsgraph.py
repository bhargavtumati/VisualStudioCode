class Graph:
    def __init__(self, vertices):
        self.v = vertices
        self.adjList = [[] for _ in range(vertices)]
        self.path=[]

    def addEdge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def printAllPaths(self, s):
        visited = [False] * self.v
        localPathList = [s]
        
        self.printAllPathsUtil(s, visited, localPathList)

    def printAllPathsUtil(self, u, visited, localPathList):
        visited[u] = True
        for i in self.adjList[u]:
            if not visited[i]:
                localPathList.append(i)
                #if i==2:   #for destination
                appe=True
                for c in self.adjList[i]:
                    if not visited[c]:
                       appe=False
                       
                if appe:
                    print(localPathList)
                self.printAllPathsUtil(i, visited, localPathList)
                localPathList.pop()

        visited[u] = False
        
# Example usage
g = Graph(5)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(4, 2)




source = 1
print(f"Paths from source {source} to all vertices:")
g.printAllPaths(source)

