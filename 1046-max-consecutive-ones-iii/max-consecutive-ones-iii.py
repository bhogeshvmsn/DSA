class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        l=0
        zc=0
        n=len(nums)

        for r in range(n):
            if nums[r]==0:
                zc+=1
            if zc>k:
                if nums[l]==0:
                    zc-=1
                l+=1

        return n-l