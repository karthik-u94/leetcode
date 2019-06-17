class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        begin=0
        end=len(numbers)-1
        while(begin!=end):
            
            sum=numbers[begin]+numbers[end]
         
            if(sum==target):
                return [begin+1, end+1]
            elif(sum<target):
                begin=begin+1
            else:
                end=end-1
