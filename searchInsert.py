class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        pos=0
        for i in range(len(nums)):
            if nums[i]==target:
                return i
            elif nums[i]<target:
                pos=i+1
            
        return pos
