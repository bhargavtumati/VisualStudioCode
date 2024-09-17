from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph=[[] for _ in range(n+1)]
        for did in dislikes:
            graph[did[0]].append(did[1])
            graph[did[1]].append(did[0])
        colour=[-1]*(n+1)
        def bfs(graph,colour,queue):
          
            colour[queue[0]]=0
            while queue:
                
                for neigh in graph[queue[0]]:
                    if colour[queue[0]]==colour[neigh]:
                        return False
                    elif colour[neigh]==-1:
                        colour[neigh]=1-colour[queue[0]]
                        queue.append(neigh)
                    

                del(queue[0])
            return True
 
        for i in range(1,n+1):
          if colour[i]==-1:

              if not bfs(graph,colour,[i]):
                  return False
            
        return True
    
