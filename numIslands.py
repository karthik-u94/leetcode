class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands=0
        if len(grid)==0:
            return 0
        r,c=len(grid),len(grid[0])
        def help(l,m):
            if(l>=r or l<0 or m>=c or m<0 or grid[l][m]=='0'):
                return
            grid[l][m]='0'
            help(l+1,m)
            help(l-1,m)
            help(l,m+1)
            help(l,m-1)
            return
        for i in range(0,r):
            for j in range(0,c):
                if grid[i][j]=='1':
                    num_islands+=1
                    grid[i][j]=0
                    help(i,j)
        
        return num_islands
            
