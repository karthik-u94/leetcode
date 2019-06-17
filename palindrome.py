class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if(x<0):
            return False
        
        xs=str(x)
        begin=0
        end=len(xs)-1
        while begin<end:
            
            if xs[begin]!=xs[end]:
                return False
            begin+=1
            end-=1
        
        return True
