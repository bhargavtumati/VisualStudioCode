from json import loads
from sys import stdin
from typing import List


class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n=len(cars)
        answer=[-1.0]*n 
        car_stack=[]  
        for i in range(n - 1, -1, -1):
            position, speed = cars[i]

            while car_stack and (cars[car_stack[-1]][1] >= speed or (cars[car_stack[-1]][0] - position)/(speed - cars[car_stack[-1]][1]) >= answer[car_stack[-1]] >= 0):
                car_stack.pop()
            if car_stack:
                answer[i] = (cars[car_stack[-1]][0] - position)/(speed - cars[car_stack[-1]][1])
            car_stack.append(i)
        return answer
"""
with open("user.out", "w") as f:
    inputs = map(loads, stdin)
    for nums in inputs:
        print(str(Solution().getCollisionTimes(nums)).replace(" ", ""), file=f)
exit(0)"""
if __name__=="__main__":
   cars=[[1,2],[2,1],[4,3],[7,2]]
   s=Solution()
   print(s.getCollisionTimes(cars))