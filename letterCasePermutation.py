from typing import List

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        lnth=len(s)
        if lnth==1:
            return [s] if s.isnumeric() else [s.lower(),s.upper()]
        else:
            ans=[]
            for i in self.letterCasePermutation(s[1:]):
                if s[0].isnumeric():
                    ans.append(s[0]+i)
                else:
                    ans.extend([s[0].lower()+i,s[0].upper()+i])
            return ans
if __name__=="__main__":
       v=Solution()
       s="mQe"
       print(v.letterCasePermutation(s))