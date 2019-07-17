"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        res=[]
        
        def helper(node):
            if not node:
                return 
            res.append(node.val)
            if node.children is not None:
                for child in node.children:
                    helper(child)
            
            
        helper(root)
        
        return res
