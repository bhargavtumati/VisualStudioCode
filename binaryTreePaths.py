# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import List, Optional

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(root: Optional[TreeNode], current_path: str, result: List[str]):
            current_path += "->" + str(root.val)
            if not root.left and not root.right:
                result.append(current_path)
            if root.left:
                dfs(root.left, current_path, result)
            if root.right:
                dfs(root.right, current_path, result)

        result = []
        if not root:
            return result
        current_path = str(root.val)
        if not root.left and not root.right:
            result.append(current_path)
        if root.left:
            dfs(root.left, current_path, result)
        if root.right:
            dfs(root.right, current_path, result)
        return result

if __name__ == "__main__":
    # Example usage: Create a sample binary tree
    #       1
    #      / \
    #     2   3
    #      \
    #       5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)

    solution = Solution()
    paths = solution.binaryTreePaths(root)
    for i in range(len(paths)):
        if i==0:
            print("["+paths[i],end='')
        if i>0 and i<len(paths)-1:
            print(","+paths[i],end='')
        if i==len(paths)-1:
            print(","+paths[i]+"]",end='')

