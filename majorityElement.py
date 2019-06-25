class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts=collections.Counter(nums)
        maxKey=0
        maxValue=0
        for key,value in counts.items():
            if(value>maxValue):
                maxValue=value
                maxKey=key
        return maxKey
