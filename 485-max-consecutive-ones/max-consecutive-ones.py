class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        n=len(nums)
        mc,mx=0,0
        for i in range(n):
            if nums[i]==1:
                mc+=1
            else:
                mx=max(mc,mx)
                mc=0
        return max(mx,mc)
