class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        all_nums=[v for row in nums for v in row ]
        if(len(all_nums)!=r*c):
            return nums
        res=[]
        k=0
        for i in range(r):
            res.append([])
            for j in range(c):
                res[i].append(all_nums[k])
                k+=1
        return res
