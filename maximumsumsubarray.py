from typing import List

class Solution:
  def maxSubarraySumCircular(self,nums: List[int]) -> int:
    complete_sum = sum(nums)
    
    min_so_far = 10e5
    max_so_far = -1 * 10e5
    min_ending_here = max_ending_here = 0
    for num in nums:
        max_ending_here += num
        min_ending_here += num
        max_so_far = max(max_so_far, max_ending_here)
        min_so_far = min(min_so_far, min_ending_here)
        max_ending_here = max(0, max_ending_here)
        min_ending_here = min(0, min_ending_here)
    if complete_sum == min_so_far:
        return max_so_far
    return max(max_so_far, complete_sum - min_so_far)

if __name__ == "__main__":
    nums = [5, -3, 5]
    c = Solution()
    print(c.maxSubarraySumCircular(nums))
