"""
Palindrome Op2
You are given a string s containing lowercase letters and an integer k.
You need to :

First, change some characters of s to other lowercase English letters.
Then divide s into k non-empty disjoint substrings such that each substring is a palindrome.
Return the minimal number of characters that you need to change to divide the string.

Example 1
Input
 s = "abc", k = 2
Output
1
Explanation:
You can split the string into "ab" and "c", and change 1 character in "ab" to make it palindrome.

Example 2
Input
s = "aabbc", k = 3
Output
0
Explanation:
You can split the string into "aa", "bb" and "c", all of them are palindrome.

Constraints:
1 <= k <= s.length <= 100.
s only contains lowercase English letters."""

from cmath import inf


class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        n = len(s)
        g = [[0] * n for _ in range(n)]   #len(s)*len(s) matrix
        for i in range(n - 1, -1, -1):  #reverse n-1 to 0
            for j in range(i + 1, n):  # i+1 to n
                g[i][j] = int(s[i] != s[j])  #!= means 1 , == means 0
                if i + 1 < j:  
                    g[i][j] += g[i + 1][j - 1]

        f = [[0] * (k + 1) for _ in range(n + 1)]  #k+1 * n+1 matrix
        for i in range(1, n + 1):
            for j in range(1, min(i, k) + 1):
                if j == 1:
                    f[i][j] = g[0][i - 1]
                else:
                    f[i][j] = inf
                    for h in range(j - 1, i):
                        f[i][j] = min(f[i][j], f[h][j - 1] + g[h][i - 1])
        return f[n][k]
    
if __name__=="__main__":
       s="abc"
       k=2
       f=Solution()
       print(f.palindromePartition(s,k))

                
