# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Optional
from binaryTreePaths import TreeNode


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo = {}

        def _allPossibleFBT(n):
            if n in memo:
                return memo[n]

            list = []
            if n == 1:
                list.append(TreeNode(0))
            else:
                for i in range(1, n - 1, 2):
                    lTrees = _allPossibleFBT(i)
                    rTrees = _allPossibleFBT(n - i - 1)

                    for lt in lTrees:
                        for rt in rTrees:
                            list.append(TreeNode(0, lt, rt))

            memo[n] = list
            return list

        return _allPossibleFBT(n)
if __name__ == "__main__":
    n = 3
    s=Solution()
    Li=s.allPossibleFBT(n)
    def treetraversal(root=Optional[TreeNode]):
        if not root:
            return
        print(root.val,end='')
        if root.left or root.right:
             print(" -> ",end='')
        if root.left:
            treetraversal(root.left)
        if root.right:
            treetraversal(root.right)
    for c in Li:
        print()
        treetraversal(c)