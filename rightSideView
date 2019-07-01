# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        res=[]
        levels=[]
        if not(root):
            return []
        def rec(node, level):
            if len(levels)==level:
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                rec(node.left, level+1)
            if node.right:
                rec(node.right, level+1)
        rec(root,0)
        for lev in levels:
            res.append(lev[-1])
        return res
