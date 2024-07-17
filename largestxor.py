import math
class Solution:
    def largestXOR(self, nums):
        # Write Code Here 
        res=0
        for i in nums:
            res=res|i
        return res
if __name__=="__main__":
    r=Solution()
    s=[5,55,4,9,8]
    print(r.largestXOR(s))
"""
Solution : Maximize XOR
Initially, the question seems to be very brainstorming but when you closely look at the table below, you can actually find the solution like anybody:

image

The Real Trick:
So, we know that we need to maximize the XOR of all elements of the array.
In order to do so, we must try to include as many as odd 1’s possible in the sequence at every place.
Incase there are even 1's at any position they can be made odd. (by making that position 0 of any one number, see the table.)
But incase there are no 1s at a position it can't be generated.
To check if any position contains 1 or not, OR is the answer.
"""




"""
Largest XOR
You are given a 0-indexed integer array nums. In one operation, select any non-negative integer x and an index i, then update nums[i] to be equal to (nums[i] AND (nums[i] XOR x)).

Note that AND is the bitwise AND operation and XOR is the bitwise XOR operation.

Return the maximum possible bitwise XOR of all elements of nums after applying the operation any number of times.

Example 1
Input
nums = [3,2,4,6]
Output
7
Explanation:
Apply the operation with x = 4 and i = 3, num[3] = 6 AND (6 XOR 4) = 6 AND 2 = 2. Now, nums = [3, 2, 4, 2] and the bitwise XOR of all the elements = 3 XOR 2 XOR 4 XOR 2 = 7. It can be shown that 7 is the maximum possible bitwise XOR. Note that other operations may be used to achieve a bitwise XOR of 7.

Example 2
Input
nums = [1,2,3,9,2]
Output
11
Explanation:
Apply the operation zero times. The bitwise XOR of all the elements = 1 XOR 2 XOR 3 XOR 9 XOR 2 = 11. It can be shown that 11 is the maximum possible bitwise XOR.

Constraints:
1 <= nums.length <= 10^5
0 <= nums[i] <= 10^8"""