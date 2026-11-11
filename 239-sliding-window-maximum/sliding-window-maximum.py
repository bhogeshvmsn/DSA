class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        n=len(nums)
        res=[0]*(n-k+1)
        deque_=deque()

        for right in range(n):
            while deque_ and deque_[0]<=right-k:
                deque_.popleft()
            while deque_ and nums[deque_[-1]]<nums[right]:
                deque_.pop()
            deque_.append(right)

            if right>=k-1:
                res[right-k+1]=nums[deque_[0]]
        return res