from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # building our root list
        l1 = [0]*len(isConnected[0])
        for i in range(len(l1)):
            l1[i] = i
        
        # returns root of existing vertex
        def get_root(x):
            return l1[x]
        
        # update root of existing index
        def union(x,y):
            Rx = get_root(x)
            Ry = get_root(y)

            if(Rx != Ry):
                for i in range(0,len(l1)):
                    if l1[i] == Ry:
                        l1[i] = Rx

        # traversing only the upper traingular matrix to save time
        for i in range(0,len(isConnected)):
            for j in range(i+1,len(isConnected[0])):
                if isConnected[i][j] == 1:
                    union(i,j)
            
        return len(set(l1))

if __name__=="__main__":
    s=Solution()
    isConnected=[[1,1,0],[1,1,0],[0,0,1]]
    print(s.findCircleNum(isConnected))

"""
547. Number of Provinces
Solved
Medium
Topics
Companies
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

 

Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3
 

Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""