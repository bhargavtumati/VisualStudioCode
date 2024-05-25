from collections import defaultdict


class countPoints:
    def Solution(self, s: str) -> int:
        ans = 0
        r = defaultdict(str)
        print(r)
        for rod in range(1,len(s),2):
            ring = rod-1
            r[s[rod]] += s[ring]
            print(r)

        for key in r:
            if len(set(r[key])) >= 3:
                ans +=1

        return ans

if __name__ =="__main__":
     cp=countPoints()
     rings="B0B6G0R6R0R6G9"
     print(cp.Solution(rings))
