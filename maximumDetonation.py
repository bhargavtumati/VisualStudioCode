from math import sqrt
import collections
from typing import List


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj=collections.defaultdict(list)
        for i in range(len(bombs)):   # for each bomb no of bombs inside its radius creates a directed graph
            for j in range(i+1,len(bombs)):
                x1,y1,r1= bombs[i]
                x2,y2,r2= bombs[j]
                d=sqrt((x1-x2)**2+(y1-y2)**2)
                if d <=r1:
                    adj[i].append(j)
                if d <=r2:
                    adj[j].append(i)
        def dfs(i,visit):  #depth first search:creates a list of neighbours who are in range of their radii and dismisses the already added ones
            if i in visit:
                return 0
            visit.add(i)
            for nei in adj[i]:    # for each neighbour of ith defaultdict 
                dfs(nei,visit) 
            return len(visit)       # returns the length of maximum neighbours
        res=0
        for i in range(len(bombs)):
            res = max(res,dfs(i,set()))    # create new hashset everytime
            
        return res
    
if __name__ =="__main__":
    bombs=[[1,2,3],[2,3,1],[3,4,2],[4,5,3],[5,6,4]]
    al=Solution()
    print(al.maximumDetonation(bombs))