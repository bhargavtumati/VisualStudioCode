from typing import List


class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # super brute force: DFS + backtracking
        # smarter: pattern

        # wlog we can make the permutation of 0..2^n-1 starting with zero, then cycle through to start at `start`

        # n = 1: 0, 1
        # n = 2: 00, 01, 11, 10
        # so take 0S_{n-1} and 1rev(S_{n-1}) (?)
        # because we know S_{n-1} has the right property, and same with rev(S_{n-1})
        # so S + rev(S) has that property, EXCEPT
        #   the outer two: same element
        #   and the inner two: same element
        #   so if we put a 1 in front of rev(S) then we're good

        if n == 1:
            if start == 0: return [0, 1]
            else: return [1, 0]

        S = [0, 1]
        for m in range(2, n+1):
            # existing S is S_{n-1}; we leave it as-is ("prepend 0")
            # then we append elements in reverse with a 1 in front, for m=2 we want to add 10 == 1 << (m-1)
            p = 1 << (m-1)
            S.extend(p + S[k] for k in range(len(S)-1, -1, -1))

        i = S.index(start)
        if i: return S[i:] + S[:i]
        else: return S

if __name__ =="__main__":
     cp=Solution()    
     n=2
     start=3
     print(cp.circularPermutation(n,start))