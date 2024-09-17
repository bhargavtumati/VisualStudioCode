class Solution:
    def minDifference(self, arr, n):
        # Calculate the total sum of the array
        total_sum = sum(arr)
        
        # Initialize a boolean array dp[i][j] where dp[i][j] represents whether
        # it's possible to achieve a sum of j using the first i elements of the array
        dp = [[False] * (total_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # Populate the dp array
        for i in range(1, n + 1):
            for j in range(total_sum + 1):
                dp[i][j] = dp[i - 1][j] or (j >= arr[i - 1] and dp[i - 1][j - arr[i - 1]])

        # Find the minimum positive value of |2 * j - total_sum| for all j
        min_diff = float('inf')
        for j in range(total_sum // 2 + 1):
            if dp[n][j]:
                min_diff = min(min_diff, abs(2 * j - total_sum))

        return min_diff
if __name__=="__main__":
    arr=[2,4,7,11]
    n=4
    s=Solution()
    print(s.minDifference(arr,n))

    #https://www.youtube.com/watch?v=FB0KUhsxXGY&t=297s