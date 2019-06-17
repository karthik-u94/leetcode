class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        map=set(nums)
        for num in range(0,len(nums)+1):
            if not num in map.keys():
                return num
