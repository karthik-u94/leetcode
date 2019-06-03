class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        res=set()
        print nums
        for i in range(len(nums)):
            target=-nums[i]
            begin,end=i+1,len(nums)-1
            while(begin<end):
                sum=nums[begin]+nums[end]
                if(sum<target):
                    begin+=1
                elif(sum>target):
                    end-=1
                else:
                    res.add((nums[i],nums[begin],nums[end]))
                    begin+=1
                    end-=1
        return res

        
