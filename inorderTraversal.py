# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res=[]
        def inorder(root):
            if root is None:
                return
            if root.left:
                inorder(root.left)
            res.append(root.val)
            if root.right:
                inorder(root.right)
                
        inorder(root)
        
        return res
