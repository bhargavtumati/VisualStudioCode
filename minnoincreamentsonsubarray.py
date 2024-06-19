from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        prev = target[0]
        
        for i in range(1, len(target)):
            if target[i] > prev:
                ans += target[i] - prev
            prev = target[i]
        
        return ans

if __name__ == "__main__":
         target=[3,1,5,4,2]
         d=Solution()
         print(d.minNumberOperations(target))