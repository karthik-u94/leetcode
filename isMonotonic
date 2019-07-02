class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        flag=None
        for i in range(1,len(A)):
            if flag is None:
                if   A[i]<A[i-1]:
                    flag=-1
                elif A[i]>A[i-1]:
                    flag=1
                continue
            if flag ==1 and A[i]<A[i-1]:
                return False
            if flag ==-1 and A[i]>A[i-1]:
                return False
        return True
