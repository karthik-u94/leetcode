class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pow=len(digits)-1
        num=0
        for i in digits:
            num+=i*(10**pow)
            pow-=1
        res=num+1
        nums=list(str(res))
        nums=[int(x) for x in nums]
        return nums
