class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res=[]
        
        for x in range(left,right+1):
            flag=True
            str_x=str(x)
            for i in str_x:
                int_i=int(i)
                if int_i==0 or x%int_i!=0:
                    flag=False
                    break
            if flag:
                res.append(x)
        return res
