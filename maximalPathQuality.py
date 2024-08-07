import collections
from typing import List


class Solution:
    def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, t in edges :
            graph[u].append((v,t))
            graph[v].append((u,t))

        queue = collections.deque([(0, 0, values[0], [0])]) # (node, time, totalVal, path)
        valList = [(-1,-1)]*len(values)
        valList[0] = (values[0], 0)
        output = 0
        while queue :
            node, curTime, curVal, visited = queue.popleft()
            if node == 0 :
                output = max(output, curVal)
            for nxt, t in graph[node] :
                if curTime + t > maxTime :
                    continue
                nxtVal = curVal
                if nxt not in visited:
                    nxtVal += values[nxt]
                #This is the condition that significantly reduces the runtime
                if curTime+t >= valList[nxt][1] and nxtVal < valList[nxt][0] :
                    continue
                queue.append((nxt, curTime+t, nxtVal, visited + [nxt]))
                valList[nxt] = (nxtVal, curTime+t)
        return output

if __name__=="__main__":
    values=[5,10,15,20]
    edges=[[0,1,10],[1,2,10],[0,3,10]]
    maxTime=30
    s=Solution()
    print(s.maximalPathQuality(values,edges,maxTime))