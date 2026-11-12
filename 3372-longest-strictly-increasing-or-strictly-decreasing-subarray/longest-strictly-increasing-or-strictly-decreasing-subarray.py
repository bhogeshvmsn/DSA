class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            cur=[]
            for j in range(i,len(nums)):
             cur.append(nums[j])
             if (
                all(cur[idx]>cur[idx-1] for idx in range(1,len(cur))) or
                all(cur[idx]<cur[idx-1] for idx in range(1,len(cur)))
             ): res=max(res,j-i+1)

        return res
