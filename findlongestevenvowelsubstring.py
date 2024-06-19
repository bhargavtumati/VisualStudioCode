class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        n = len(s)
        dp={0:-1}  # creating dictionary 
        parity = 0
        ans = 0
        vowels = 'aeiou'
        for i,c in enumerate(s):  # getting index of each letter 
            if c in vowels:
                index = vowels.index(c)
                parity^=1<<index   #xor of 1 left shift index
            if parity in dp:
                ans=max(ans,i-dp[parity])
            else:
                dp[parity]=i
        return ans
if __name__=="__main__":
    s="eleetminicoworoep"
    f=Solution()
    print(f.findTheLongestSubstring(s))