from typing import List, Optional

from binaryTreePaths import TreeNode


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def construct_tree_util(pre, pre_index, low, high):
             if pre_index[0] >= len(pre) or low > high:
                  return None

             root = TreeNode(pre[pre_index[0]])
             pre_index[0] += 1

             i = low
             while i <= high:
                 if pre[i] > root.val:
                     break
                 i += 1

             root.left = construct_tree_util(pre, pre_index, pre_index[0], i - 1)
             root.right = construct_tree_util(pre, pre_index, i, high)

             return root

        pre_index = [0]
        return construct_tree_util(preorder, pre_index, 0, len(preorder) - 1)
    
if __name__=="__main__":    
   preorder = [8,5,1,7,10,12]
   c=Solution()
   root_node = c.bstFromPreorder(preorder)

   def level_order_traversal(root):
    if not root:
        return

    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.val, end=' ')

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

   level_order_traversal(root_node)