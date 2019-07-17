class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res=[]
        counts=collections.Counter(arr1)
        
        for n in arr2:
            i=counts[n]
            for c in range(i):
                res.append(n)
                arr1.remove(n)
        return res+sorted(arr1)
