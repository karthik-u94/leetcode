class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        idx={}
        for i in range(len(B)):
            idx[B[i]]=i
        
        res=[-1]*len(B)
        
        for i in range(len(A)):
            res[i]=idx[A[i]]
            
        return res
