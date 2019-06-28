class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counts=collections.Counter(nums)
        
        for key in counts.keys():
            if counts[key]==1:
                return key
