class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        fm=defaultdict(int)
        for num in nums: fm[num]+=1

        o=fm[1]
        res=o if o%2==1 else max(0,o-1)

        for num in fm:
            if num==1: continue

            total=0
            cur=num

            while cur in fm and fm[cur]>=2:
                total+=2
                cur*=cur
            if cur in fm: total+=1
            elif not cur in fm: total-=1
            res=max(res,total)
        return res