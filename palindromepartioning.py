from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(substring: str) -> bool:
            return substring == substring[::-1]

        def dfs(index: int, path: List[str]):
            if index == len(s):
                ans.append(path[:])
                return
            for end in range(index, len(s)):
                if is_palindrome(s[index:end + 1]):
                    path.append(s[index:end + 1])
                    dfs(end + 1, path)
                    path.pop()

        ans = []
        dfs(0, [])
        return ans

# Example usage
s = "abb"
solution = Solution()
result = solution.partition(s)
for partition in result:
    print(*partition)
