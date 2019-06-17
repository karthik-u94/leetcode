class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        out = 0
        while n>=5**i:
            out+=n//5**i
            
            i+=1
        return out
