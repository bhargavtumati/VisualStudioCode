from collections import deque
from typing import List, Optional

from binaryTreePaths import TreeNode


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        VAL_TO_INORDER_IDX = {inorder[i]: i for i in range(len(inorder))}

        def buildTreePartition(preorder, inorder_start, inorder_end):
            if not preorder or inorder_start < 0 or inorder_end > len(inorder):
                return None

            root_val = preorder[0]
            root_inorder_idx = VAL_TO_INORDER_IDX[root_val]
            if root_inorder_idx > inorder_end or root_inorder_idx < inorder_start:
                return None
            
            root = TreeNode(preorder.pop(0))
            root.left = buildTreePartition(preorder, inorder_start, root_inorder_idx - 1)
            root.right = buildTreePartition(preorder, root_inorder_idx + 1, inorder_end)

            return root

        return buildTreePartition(preorder, 0, len(inorder) - 1)
if __name__ == "__main__":    
   preorder=[3,9,20,15,7]
   inorder=[9,3,15,20,7]
   v=Solution()
   head=v.buildTree(preorder,inorder)
   
   def level_order_traversal(root):
        # Formalities/Edge Cases
        if root is None:
            return []

        result = []

        # Main logic
        q = deque()
        q.append(root)

        while q:
            level_nodes = []
            level_size = len(q)

            for _ in range(level_size):
                curr = q.popleft()
                # This is the place where you edit your elements
                level_nodes.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            # This is the place where level shift happens
            result.append(level_nodes)

        return result
   print(level_order_traversal(head))
