class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counts=collections.Counter(nums)
        
        for k in counts.values():
            if k>1:
                return True
        return False
