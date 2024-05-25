class longestNiceSubstring:
    def Solution (self, s: str) -> str:
        N = len(s)
        best = ""
        def good(start,end):
            t=set(s[start:end])

            for x in t:
               if(x.lower() in t) != (x.upper() in t):
                  return False
            return True
        for start in range(N):
            for end in range(start +1,N+1):
                    if good(start,end) and end-start >len(best):
                          best = s[start:end]
        return best
if __name__ == "__main__":
     s="aArRk"
     ls=longestNiceSubstring()
     print(ls.Solution(s))