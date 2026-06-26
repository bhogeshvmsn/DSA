class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n=len(nums)

        f=[0]*(2*n+1)
        a=[0]*(2*n+1)
        f[n],a[n]=1,1
        bal=n
        res=0

        for num in nums:
            if num==target: bal+=1
            else: bal-=1
            
            f[bal]+=1
            a[bal]=a[bal-1]+f[bal]
            res+=a[bal-1]
        return res