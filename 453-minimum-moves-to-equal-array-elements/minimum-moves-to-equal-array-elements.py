class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_value = min(nums)
        total_sum = sum(nums)
        return total_sum - min_value * len(nums)