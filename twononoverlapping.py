from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        
        mx, ans = 0, 0

        beg, end, val = zip(*events)
        beg2ndMtg = sorted(zip(beg, val))
        end1stMtg = iter(sorted(zip(end, val)))

        end1st, val1st = next(end1stMtg)

        for beg2nd, val2nd in beg2ndMtg:

            while end1st < beg2nd:
                mx = max(mx, val1st)
                end1st, val1st = next(end1stMtg)

            ans = max(ans, mx + val2nd)

        return ans  
if __name__=="__main__":
    events=[[1,5,3],[1,5,1],[6,6,5]]
    s=Solution()
    print(s.maxTwoEvents(events))