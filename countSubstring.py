class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        ans = 0
        for i in range(n):
            for j in range(m):
                p = i
                l = j
                c = 0
                while p < n and l < m:
                    if s[p] != t[l]:
                        c+=1
                        if c > 1:
                            break
                    ans += c
                    l += 1
                    p += 1
        return ans
if __name__=="__main__":
    h=Solution()
    s="aba"
    t="baba"
    #s=input("enter s: ")
    #t=input("enter t: ")
    print(h.countSubstrings(s,t))