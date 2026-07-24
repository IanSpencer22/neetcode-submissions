# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def traverse(node, remaining):
            if node is None:
                return False
            
            remaining -= node.val

            if node.left is None and node.right is None:
                return remaining == 0
            
            return traverse(node.left, remaining) or traverse(node.right, remaining)

        return traverse(root, targetSum)
            
