class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res=[0]*(rowIndex+1)
        res[0]=res[len(res)-1]=1
        if(rowIndex>=2):
            for i in range(1,len(res)-1):
                res[i]=self.getElement(rowIndex,i)
             
        return res
            
        
        
        
    def getElement(self,rowIndex, colIndex):
        if rowIndex<2:
            return 1
        if(colIndex==0 or colIndex==rowIndex):
            return 1
        else:
            return self.getElement(rowIndex-1,colIndex-1)+self.getElement(rowIndex-1,colIndex)
        
        
        
