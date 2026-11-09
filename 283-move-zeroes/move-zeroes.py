class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
       left=0
       n=len(nums)
       for right in range(n):
        if nums[right]!=0:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
        