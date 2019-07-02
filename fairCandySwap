class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sum_A=sum(A)
        sum_B=sum(B)
        target=(sum_A+sum_B)/2
        sA,sB =set(A),set(B)
        for a in sA:
            b=target-sum_A+a
            if b in sB:
                return [a,b]
            
