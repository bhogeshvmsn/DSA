class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        n=len(nums)
        count=0
        prefix_sum=0
        map={0:1}

        for num in nums:
            prefix_sum+=num
            remainder=prefix_sum%k
            if remainder<0:
                remainder+=k
            if remainder in map:
                count+=map[remainder]
            map[remainder]=map.get(remainder,0)+1
        return count
        