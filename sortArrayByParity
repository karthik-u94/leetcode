class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        oddPtr=0
        evenPtr=len(A)-1
        while evenPtr>oddPtr:
            if A[oddPtr]%2==0:
                oddPtr+=1
            if A[evenPtr]%2!=0:
                evenPtr-=1 
            # print(evenPtr,oddPtr)
            if(evenPtr>oddPtr):
                A[evenPtr],A[oddPtr]=A[oddPtr],A[evenPtr]
                
        return A
