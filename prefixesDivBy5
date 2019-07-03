class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        output = list()
        outputBool = list([True] if A[0]==0 else [False])
        if A==None: return output;
        output.extend([A[0]]);
        for i in range(1,len(A)):
            if A[i]==1:
                output.extend([output[i-1]*2+1])
            else:
                output.extend([output[i-1]*2])
                
            if output[i]%5==0:
                outputBool.extend([True]);
            else:
                outputBool.extend([False]);
        return outputBool
