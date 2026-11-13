class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        leftsum=0
        totalsum=sum(nums)

        for i in range(n):
            rightsum=totalsum-leftsum-nums[i]
            if leftsum==rightsum:
                return i
            leftsum+=nums[i]
        return -1