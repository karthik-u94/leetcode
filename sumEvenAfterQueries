class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        even_sum=sum(v for v in A if v%2==0)
        res=[]
        for q in queries:
            if A[q[1]]%2==0:
                if q[0]%2==0:
                    even_sum+=q[0]
                else:
                    even_sum-=A[q[1]]
            else:
                if q[0]%2!=0:
                    even_sum+=A[q[1]]+q[0]
            res.append(even_sum)
            A[q[1]]+=q[0]
        return res
