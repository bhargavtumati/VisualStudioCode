import java.util.Arrays;

public class findnooflis {
    public int Solution(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n]; // Length of LIS ending at index i
        int[] count = new int[n]; // Number of LIS of length i
        Arrays.fill(dp, 1);
        Arrays.fill(count, 1);

        int maxLen = 1; // Length of the longest increasing subsequence

        for (int i = 1; i < n; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j]) {
                    if (dp[j] + 1 > dp[i]) {
                        dp[i] = dp[j] + 1;
                        count[i] = count[j];
                    } else if (dp[j] + 1 == dp[i]) {
                        count[i] += count[j];
                    }
                }
            }
            maxLen = Math.max(maxLen, dp[i]);
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            if (dp[i] == maxLen) {
                result += count[i];
            }
        }

        return result;
    }
    public static void main(String args[]){
        int[] nums={1,3,5,4,7};
findnooflis fs =new findnooflis();
        System.out.println(fs.Solution(nums));
        
    }
}


