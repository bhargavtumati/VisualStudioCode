# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional

from binaryTreePaths import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = root.val

        def dfs(node):
            nonlocal res
            if not node: return 0

            leftMax = dfs(node.left)
            rightMax = dfs(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res = max(res, node.val + leftMax + rightMax)
            
            return node.val + max(leftMax , rightMax)

        dfs(root)
        return res
if __name__ == "__main__":
    # Example usage: Create a sample binary tree
    #       1
    #      / \
    #     2   3
         
          
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    s = Solution()
    print(s.maxPathSum(root))
    