class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res=[]
        dict=set(nums)
        
        for num in range(1,len(nums)+1):
            if num not in dict:
                res.append(num)
        return res
