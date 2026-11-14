class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n=len(nums)
        res=inf

        for i in range(n):
            cur=0
            count=0
            for j in range(i,n):
                count+=1
                cur+=nums[j]
                if count<l: continue
                if count>r:break
                if cur>0: res=min(res,cur)
        return res if res!=inf else -1

        