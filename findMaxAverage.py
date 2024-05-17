from calendar import c
from cmath import inf
from typing import List

class findMaxAverage:
    def Solution(self, nums: List[int], k: int) -> float:
        s=0
        l=k
        max=float(-inf)
        while l<=len(nums):
            sum=0
            i=s
            while i<l:
                sum+=nums[i]
                i+=1;
            s+=1
            l+=1 
            print(sum)
            avg=sum/k
            if max<avg:
               max=avg
            
        return max
    
if __name__=="__main__":
   c=findMaxAverage() 
   nums = [5]
   k=1

   print(c.Solution(nums,k))

        
