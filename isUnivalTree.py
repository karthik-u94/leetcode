# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return False
        val=root.val
        
        def helper(node):
            if not node:
                return True
            if node.val!=val:
                return False
            return helper(node.left) and helper(node.right)
        
        return helper(root)
