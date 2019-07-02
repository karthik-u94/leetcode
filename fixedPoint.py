class Solution(object):
    def fixedPoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        l, r = 0, len(A)-1
        
        while l <= r:
            mid = (l+r) //2 
            if A[mid] == mid:
                return mid
            elif A[mid] < mid:
                l = mid + 1
            else:
                r = mid - 1  
        return -1
