from itertools import permutations
from typing import List


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        m = len(students)
        
        score = [[0]* m for _ in range(m)]
        for i in range(m): 
            for j in range(m): 
                score[i][j] = sum(x == y for x, y in zip(students[i], mentors[j]))
        
        ans = 0 
        for perm in permutations(range(m)): 
            ans = max(ans, sum(score[i][j] for i, j in zip(perm, range(m))))
        return ans 
if __name__=="__main__":
    students = [[1,1,0],[1,0,1],[0,0,1]]
    mentors = [[1,0,0],[0,0,1],[1,1,0]]
    v=Solution()
    print(v.maxCompatibilitySum(students,mentors))
