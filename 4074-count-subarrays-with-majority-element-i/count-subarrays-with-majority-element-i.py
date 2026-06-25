class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        res=0

        for i in range(n):
            tc=0
            for j in range(i,n):
                if nums[j]==target: tc+=1
                if tc > (j-i+1)//2: res+=1

        return res