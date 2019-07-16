# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        def helper(low, high):
            print(low,high)
            if high-low==0:
                return low
            mid=(high+low)//2
            print("Mid is")
            print(mid)
            if isBadVersion(mid):
                print("Mid is bad")
                res= helper(low,mid)
            else:
                print("Mid is good")
                res= helper(mid+1,high)
            return res
            
        return helper(1,n)
        
        
