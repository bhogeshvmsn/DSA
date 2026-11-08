class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        n,m=len(grid),len(grid[0])

        r=defaultdict(set)
        c=defaultdict(set)

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    r[i].add(j)
                    c[j].add(i)
        
        res=0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and (len(r[i])>1 or len(c[j])>1):
                    res+=1
        return res
