# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        elif len(nums) == 1:
            root = TreeNode(nums[0])
            return root
        else:
            if len(nums)%2 == 1:
                h = len(nums)//2
            else:
                h = (len(nums)//2)-1
                
            root = TreeNode(nums[h])
            
            l_subtree = self.sortedArrayToBST(nums[:h])
            r_subtree = self.sortedArrayToBST(nums[h+1:])
            
            root.left = l_subtree
            root.right = r_subtree
            
            return root
