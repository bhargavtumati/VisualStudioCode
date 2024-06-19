from typing import List


class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
       left,right =k,k
       min_val=nums[k]
       max_score=min_val
       while left>0 or right<len(nums)-1:
              if left==0 or (right<len(nums)-1 and nums[right+1]>nums[left-1]):
                  right+=1
              else:
                  left-=1
              min_val=min(min_val,nums[left],nums[right])
              max_score=max(max_score,min_val*(right-left+1))
       return max_score
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        ([1, 4, 3, 7, 4, 5], 3),   # Expected score would be based on the subarray [4, 3, 7]
        ([5, 5, 4, 5, 4, 1, 1, 1], 2), # Expected score would be based on the subarray [5, 5, 4]
        ([1, 2, 3, 4, 5], 2),      # Expected score would be based on the subarray [1, 2, 3]
        ([5, 4, 3, 2, 1], 1),      # Expected score would be based on the subarray [5, 4]
    ]
    
    # Test the maximumScore method with the test cases
    for nums, k in test_cases:
        result = solution.maximumScore(nums, k)
        print(f"The maximum score for nums={nums} with k={k} is {result}.")
