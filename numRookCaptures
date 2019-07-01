class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        captures=0
        i,j=0,0
        for row in board:
            print(row)
            if "R" not in row:
                i+=1
            else:
                j=row.index("R")
                break
        print(i,j)
        top,bottom=i-1,i+1
        left,right=j-1,j+1
        while top>=0:
            if(board[top][j]!=board[top][j].lower()):
                break
            elif board[top][j]!=".":
                captures+=1
                break
            top-=1
        while bottom<8:
            if(board[bottom][j]!=board[bottom][j].lower()):
                break
            elif board[bottom][j]!=".":
                captures+=1
                break
            bottom+=1
        while left>=0:
            if(board[i][left]!=board[i][left].lower()):
                break
            elif board[i][left]!=".":
                captures+=1
                break
            left-=1
        while right<len(board[0]):
            if(board[i][right]!=board[i][right].lower()):
                break
            elif board[i][right]!=".":
                captures+=1
                break
            right+=1
        return captures
