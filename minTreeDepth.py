# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        def check(root):
            if root is None:
                return 0
            left=check(root.left)
            right=check(root.right)
            if(root.left==None):
                return 1+right
            if(root.right==None):
                return 1+left
            return 1+min(left,right)
        return check(root)
