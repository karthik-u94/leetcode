class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix)==0:
            return False
        if  len(matrix[0])==0:
            return False
        r,c=len(matrix),len(matrix[0])
        row,col=r-1,0
        while row>=0 and col<c:
            print(row,col)
            if matrix[row][col]==target:
                return True
            if matrix[row][col]>target:
                row-=1
            else:
                col+=1
        return False
        
