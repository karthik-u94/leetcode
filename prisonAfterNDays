class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        
        def helper(lst):
            res=[0]*len(lst)
            res[0]=res[-1]=0
            for i in range(1,len(lst)-1):
                if lst[i-1]==lst[i+1]:
                    res[i]=1
                else:
                    res[i]=0
            return res
        seen={}
        while N > 0:
            c = tuple(cells)
            if c in seen:
                print(N, seen[c])
                N %= seen[c] - N
            seen[c] = N

            if N >= 1:
                N -= 1
                cells = helper(cells)

        return cells
