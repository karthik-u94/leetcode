class Solution(object):
    def sumOfDigits(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        x=sorted(A)[0]
        sum=0
        for s in str(x):
            sum+=int(s)
            
        return 1 if sum%2==0 else 0
