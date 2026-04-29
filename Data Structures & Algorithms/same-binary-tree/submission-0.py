# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 1) Both empty
        if not p and not q:
            return True

        # 2) One empty OR values don't match
        if not p or not q or p.val != q.val:
            return False

        # 3) Recursively check the rest of the trees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)