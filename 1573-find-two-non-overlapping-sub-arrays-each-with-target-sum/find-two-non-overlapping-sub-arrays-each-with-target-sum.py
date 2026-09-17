class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        INT_MAX = int(1e5 + 1)
        i, j, s, n = 0, 0, arr[0], len(arr)
        l = [[j-i+1, i, j]] if s == target else []
        ss = sum(arr)
        if ss < 2*target:
            return -1 
        elif ss == 2*target:
            return n
        while i < n:
            if s < target:
                if j < n-1:
                    j += 1
                    s += arr[j]
                else:
                    break
            else:
                s -= arr[i]
                i += 1
            if s == target:
                l.append([j-i+1, i, j])
        res = INT_MAX
        random.shuffle(l)
        m = min(len(l), int(5e3))
        for p1 in range(m-1):
            for p2 in range(p1+1, m):
                d1, i1, j1 = l[p1]
                d2, i2, j2 = l[p2]
                if i2 > j1 or i1 > j2:
                    res = min(res, d1 + d2)
        return res if res != INT_MAX else -1