class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_counts=collections.Counter(nums1)
        num2_counts=collections.Counter(nums2) 
        
        intersect=[]
        
        for key in num1_counts.keys():
            if(key in num2_counts.keys()):
                for _ in range(min(num1_counts[key], num2_counts[key])):
                    intersect.append(key)
                    
        return intersect
