class solution():
    def dfsvisit(self,adj,u,visited): #traverse a single component
        stack=[]
        stack.append(u)
        visited[u]=True
        while stack:
             u=stack[-1]
             print(u,end='->')
             del(stack[-1])
             for v in adj[u]:
                 if not visited[v]:
                     stack.append(v)
                     visited[v]=True

    def dfs(self,adj):   
       visited=[False]*len(adj)
       for i in range(len(adj)):
           if not visited[i]:
               self.dfsvisit(adj,i,visited)
               visited[i]=True

if __name__=="__main__":
    adj=[[1,2],[3,4],[],[],[0]]   #create adjacency if edges given
    s=solution()
    print(s.dfs(adj))
