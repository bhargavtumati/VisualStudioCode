class Solution:
    def longestValidParentheses(self,s: str) -> int:
        max_length = 0
        stack = [-1]

        for i, char in enumerate(s):
            if char == '(':
                 stack.append(i)
            else:
                 stack.pop()
                 if not stack:
                     stack.append(i)
                 else:
                     max_length = max(max_length, i - stack[-1])

        return max_length
if __name__ == "__main__":
    # Create an instance of the Solution class
    solution = Solution()
    
    # Test cases
    test_cases = [
        "(()",          # 2
        ")()())",       # 4
        "",             # 0
        "()(())",       # 6
        "(()))())(",    # 4
    ]
    
    # Test the longestValidParentheses method with the test cases
    for test in test_cases:
        result = solution.longestValidParentheses(test)
        print(f"The longest valid parentheses in '{test}' is {result} characters long.")
