class Solution:
    def min(self, a: int, b: int) -> int:
        return a if a < b else b

    def solve(self, floor: str, i: int, numCarpets: int, carpetLen: int, prefix: list) -> int:
        if i >= len(floor) or numCarpets == 0:
            return 0
        if dp[i][numCarpets] != -1:
            return dp[i][numCarpets]
        if floor[i] == '0':
             dp[i][numCarpets] = self.solve(floor, i + 1, numCarpets, carpetLen, prefix)
             return dp[i][numCarpets]
        x = self.min(i + carpetLen, len(floor)) - 1
        white = prefix[x]
        if i != 0:
            white -= prefix[i - 1]
        ans1 = white + self.solve(floor, i + carpetLen, numCarpets - 1, carpetLen, prefix)
        ans2 = self.solve(floor, i + 1, numCarpets, carpetLen, prefix)
        dp[i][numCarpets] = max(ans1, ans2)
        return dp[i][numCarpets]

    def minimumWhiteTiles(self, floor: str, numCarpets: int, carpetLen: int) -> int:
        global dp
        dp = [[-1] * (numCarpets + 1) for _ in range(len(floor))]
        prefix = [0] * len(floor)
        if floor[0] == '1':
            prefix[0] = 1
        else:
            prefix[0] = 0
        for i in range(1, len(floor)):
            prefix[i] = prefix[i - 1] + (floor[i] == '1')
        if prefix[len(floor) - 1] == 0:
            return 0
        return prefix[len(floor) - 1] - self.solve(floor, 0, numCarpets, carpetLen, prefix)
if __name__ == "__main__":
         floor = "10110101"
         numCarpets = 2
         carpetLen = 2

         sol = Solution()
         result = sol.minimumWhiteTiles(floor, numCarpets, carpetLen)
         print(f"Maximum white tiles uncovered: {result}")