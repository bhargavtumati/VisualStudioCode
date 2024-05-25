from collections import defaultdict
from typing import List


class numSubarraysWithSum:
    def Solution(self, nums: List[int], goal: int) -> int:
        prefix_sum = [0] * (len(nums) + 1)  # creating array of nums length+1
        count = 0  
        sum_map = defaultdict(int)  # dict empty
        sum_map[0] = 1  # Initialize with one occurrence of prefix sum 0

        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            if prefix_sum[i + 1] - goal in sum_map:  #if in map
                count += sum_map[prefix_sum[i + 1] - goal]   #count+
            sum_map[prefix_sum[i + 1]] += 1

        return count
if __name__ == "__main__":
    ns= numSubarraysWithSum()
    nums=[1,0,1,0,1]
    k=2
    print(ns.Solution(nums,k))
    