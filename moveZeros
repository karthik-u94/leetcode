class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeros=[]
        for i in range(len(nums)):
            if(nums[i]!=0):
                non_zeros.append(nums[i])
        for i in range(len(non_zeros)):
            nums[i]=non_zeros[i]
        for i in range(len(non_zeros), len(nums)):
            nums[i]=0
