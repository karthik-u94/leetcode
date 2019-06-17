class Solution:
    def isHappy(self, n: int) -> bool:
        l=list()
        while(n!=1):
            sm=0
            for i in str(n):
                i=int(i)
                sm=sm+ i*i 
                n=sm
            if sm not in l:
                l.append(sm)
            else:
                return False
        return True
