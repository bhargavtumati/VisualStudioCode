from typing import List


class Solution:
    def maximizeXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xorSum = 0
        result = []
        
        # Calculate the cumulative XOR of all elements in nums
        for num in nums:
            xorSum ^= num  #same means zero, diff means max of diff.
        
        # Process queries in reverse order
        for _ in range(len(nums)):
            # Calculate the answer for the current query
            answer = xorSum ^ ((1 << maximumBit) - 1)   #or you can use 2** maximumBit
            result.append(answer)
            
            # Update xorSum by removing the last element
            xorSum ^= nums.pop() #pop removes element and xorSum XOR nums.pop() i.e 3 XOR 3 i.e 0
        
        # Reverse the result list
        return result

# Example usage
if __name__ == "__main__":
    solution = Solution()
    nums1 = [0, 1, 1, 3]
    maximumBit1 = 2
    print(solution.maximizeXor(nums1, maximumBit1))  # Expected output: [0, 3, 2, 3]
"""
    nums2 = [2, 3, 4, 7]
    maximumBit2 = 3
    print(solution.maximizeXor(nums2, maximumBit2))  # Expected output: [5, 2, 6, 5]

    nums3 = [0, 1, 2, 2, 5, 7]
    maximumBit3 = 3
    print(solution.maximizeXor(nums3, maximumBit3))  # Expected output: [4, 3, 6, 4, 6, 7]
"""