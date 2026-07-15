class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        e=0
        o=0

        for nums in range(1,n*2+1):
            if nums %2==0: e+=nums
            else:o+=nums

        return gcd(e,o)