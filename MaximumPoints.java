/*Maximize Points
You're an adventurous spelunker exploring a treasure-filled cavern. Each chamber holds a precious gem marked with an integer value. Your goal? Maximize your haul by strategically collecting these gems!

Explore the cave, represented by an integer array nums. Each element nums[i] represents the value of a gem in the chamber i. You can claim a gem (delete nums[i]) and earn points equal to its value. But there's a catch! When you claim a gem: All gems in other chambers with values one less than your chosen gem (i.e., nums[j] = nums[i] - 1) crumble instantly and disappear. All gems in other chambers with values one more than your chosen gem (i.e., nums[j] = nums[i] + 1) also crumble and vanish. Your mission is to maximize the total points you earn by strategically claiming gems. You can claim any gem any number of times (until it's gone!).

Input/Output Format Examples:
Input:
[3, 4, 2] (Cave chambers with gem values)

Output:
6 (Maximum points earned by strategically claiming gems)

Explanation:
You can claim:

Gem 4 from chamber 1, earning 4 points and causing chambers 2 and 3 (containing gems 3 and 5) to crumble.
Gem 2 from the remaining chamber, earning 2 points.

Input:1
A single line containing an integer array nums separated by spaces or commas. Each element in nums is an integer between 1 and 10^4 (inclusive). The length of nums (n) must be between 1 and 2 * 10^4 (inclusive).

Output:
return a single integer representing the maximum number of points you can earn by claiming gems in the cave according to the described rules.

Constraints:
1 <= n <= 2 * 10^4

1 <= nums[i] <= 10^4 for all i in [0, n-1]*/

import java.util.HashMap;
import java.util.Map;

 class SpecialArrangements {
    public int deletePoints(int[] nums) {
        // Create a frequency map to store the count of each gem value
        Map<Integer, Integer> freqMap = new HashMap<>();
        for (int num : nums) {
            freqMap.put(num, freqMap.getOrDefault(num, 0) + 1);
        }

        // Initialize dp array to store the maximum points for each gem value
        int[] dp = new int[10001]; // Considering gem values up to 10^4

        // Base case: dp[i] = i * freqMap.getOrDefault(i, 0)
        for (int i = 1; i <= 10000; i++) {
            dp[i] = i * freqMap.getOrDefault(i, 0);
           
        }

        // Dynamic programming to compute maximum points
        for (int i = 2; i <= 10000; i++) {
            dp[i] = Math.max(dp[i] + dp[i - 2], dp[i - 1]);
            
        }

        // Return the maximum points
        return dp[10000];
    }
    public static void main(String args[]){
   SpecialArrangements sp=new SpecialArrangements();
   int nums[]={3,4,2};

   System.out.println(sp.deletePoints(nums));


    }
}
