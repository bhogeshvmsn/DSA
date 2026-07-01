class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if grid[0][0]==1 or grid[-1][-1]==1: return 0
        n,m=len(grid),len(grid[0])
        dis=[[inf]*m for _ in range(n)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    dis[i][j]=0
                    q.append((i,j))
        
        while q:
            i,j=q.popleft()
            cd=dis[i][j]
            for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if ni<0 or ni>=n or nj<0 or nj>=m: continue
                if cd+1<dis[ni][nj]:
                    dis[ni][nj]=cd+1
                    q.append((ni,nj))
        h=[(-dis[0][0],0,0)]
        seen=set({(0,0)})
        while h:
            w,i,j=heapq.heappop(h)
            w=-w
            for ni,nj in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                if ni<0 or ni>=n or nj<0 or nj>=m or (ni,nj) in seen: continue
                seen.add((ni,nj))
                small=min(w,dis[ni][nj])
                dis[ni][nj]=small
                heapq.heappush(h,(-small,ni,nj))
        return dis[-1][-1]        