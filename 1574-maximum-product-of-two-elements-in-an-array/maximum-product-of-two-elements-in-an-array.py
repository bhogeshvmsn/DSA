class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        m=0
        sm=0

        for i in nums:
            if i>m:
                sm=m
                m=i
            else:
                sm=max(sm,i)
        return (m-1)*(sm-1)
