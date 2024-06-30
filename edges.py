from typing import List


class Solution:
    def dfs(self,source,edges,visited)-> set:
        if source not in visited:
            visited.add(source)      
        for neighbour in edges[source]:
            if neighbour not in visited:
                self.dfs(neighbour,edges,visited)
        return visited
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited=set()
        if destination in self.dfs(source,edges,visited):
            print(visited)
            return True
        return False
    
if __name__=="__main__":
    edges=[[0,1],[1,2],[2,0]]
    source=0
    destination=2
    v=Solution()
    print(v.validPath(3,edges,0,2))