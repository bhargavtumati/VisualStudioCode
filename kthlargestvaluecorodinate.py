from typing import List


class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        
        for r in range(1,len(matrix)):
            matrix[r][0]^=matrix[r-1][0]
        for c in range(1,len(matrix[0])):
            matrix[0][c]^=matrix[0][c-1]
        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[0])):
                matrix[r][c]^=matrix[r-1][c]^matrix[r][c-1]^matrix[r-1][c-1]
        res=[]
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                res.append(matrix[r][c])
        res.sort(reverse=True)

        return res[k-1]
if __name__=="__main__":
       matrix=[[5,2],[1,6]]
       k=3
       s=Solution()
       print(s.kthLargestValue(matrix,k))
