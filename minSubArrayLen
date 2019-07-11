class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        # Initialize current sum and minimum length 
        curr_sum = 0
        min_len = len(nums) + 1
  
        # Initialize starting and ending indexes 
        start = 0
        end = 0
        while (end < len(nums)): 
      
        # Keep adding array elements while current 
        # sum is smaller than x 
            while (curr_sum < s and end < len(nums)): 
                curr_sum += nums[end] 
                end+= 1
  
        # If current sum becomes greater than x. 
            while (curr_sum >= s and start < len(nums)): 
          
                # Update minimum length if needed 
                if (end - start < min_len): 
                    min_len = end - start  
  
                # remove starting elements 
                curr_sum -= nums[start] 
                start+= 1
        if min_len > len(nums):
            return 0
        return min_len  
  
