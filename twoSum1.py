class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        congugate={}
        
        for i,v in enumerate(nums):
            if(target-v in congugate.keys()):
                return [i, congugate[target-v]]
           
            congugate[v]=i
