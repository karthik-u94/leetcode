class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res=[None]*len(A)
        
        i,j=0,1
        
        for v in A:
            if v%2==0:
                res[i]=v
                i+=2
            else:
                res[j]=v
                j+=2
        return res
