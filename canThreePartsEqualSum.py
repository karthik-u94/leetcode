class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        target=sum(A)/3
        total=0
        count=0
        for a in A:
            total+=a
            if total==target:
                total=0
                count+=1
            if count==2:
                return True
        return False
        
