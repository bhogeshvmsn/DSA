from typing import List
from itertools import accumulate
from functools import cache

class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        s = list(accumulate(stoneValue, initial=0))
        
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= j:
                return 0
            
            ans = 0
            left_sum = 0
            total_sum = s[j + 1] - s[i]
            
            for k in range(i, j):
                left_sum += stoneValue[k]
                right_sum = total_sum - left_sum
                
                if left_sum < right_sum:
                    if ans >= left_sum * 2:
                        continue
                    ans = max(ans, left_sum + dfs(i, k))
                    
                elif left_sum > right_sum:
                    if ans >= right_sum * 2:
                        break
                    ans = max(ans, right_sum + dfs(k + 1, j))
                    
                else:
                    ans = max(ans, 
                              max(left_sum + dfs(i, k), 
                                  right_sum + dfs(k + 1, j)))
            
            return ans

        return dfs(0, len(stoneValue) - 1)   