class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        
        wrong=0
        for (x,y) in zip(sorted(heights),heights):
            if x!=y:
                wrong+=1
        return wrong
