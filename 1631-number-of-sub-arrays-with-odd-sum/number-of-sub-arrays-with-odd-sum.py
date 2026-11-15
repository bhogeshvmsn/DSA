
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        prefix = [0]

        for num in arr:
            prefix.append(prefix[-1] + num)

        even = 0
        odd = 0

        for num in prefix:
            if num % 2 == 0:
                even += 1
            else:
                odd += 1

        return (even * odd) % MOD
