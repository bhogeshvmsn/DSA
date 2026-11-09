class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        avaliable=SortedList([i for i in range(k)])
        using=SortedList()
        res=[0]*k
        n=len(arrival)

        for i in range(n):
            while using and using[0][0]<=arrival[i]:
                s=using.pop(0)[1]%k
                avaliable.add(s)
            if avaliable:
                idx=avaliable.bisect_left(i%k)
                if idx==len(avaliable):idx=0
                s=avaliable.pop(idx)
                using.add((arrival[i]+load[i],s))
                res[s]+=1
        mx=max(res)
        out=[]
        for i in range(k):
            if res[i]==mx: out.append(i)
        return out