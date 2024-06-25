from typing import List

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        d = {}
        ans = 0
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        matrix[i][j] = 1
                    elif matrix[i][j] == 1:
                        matrix[i][j] = 0
            if tuple(matrix[i]) in d:
                d[tuple(matrix[i])] += 1
            else:
                d[tuple(matrix[i])] = 1
        return max(d.values())
if __name__=="__main__":
    matrix=[[0,1],[1,0]]
    d=Solution()
    print(d.maxEqualRowsAfterFlips(matrix))