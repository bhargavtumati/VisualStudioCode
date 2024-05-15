from typing import List
class findErrorNums:
    def Solution(self, nums: List[int]) -> List[int]:
          nums.sort()
    
          num2=[]
          for i in range(len(nums)):
            if nums[i]!=i+1:
              num2=[nums[i],i+1]
              break
              
          return num2 

if __name__ == "__main__":
    image = [1,1]
    fm = findErrorNums()
    print(fm.Solution(image))