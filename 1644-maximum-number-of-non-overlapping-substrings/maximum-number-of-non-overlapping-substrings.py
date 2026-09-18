class Solution:
    def maxNumOfSubstrings(self, s):
        fst = {c : len(s) - i - 1 for i, c in enumerate(s[::-1])}
        lst = {c : i for i, c in enumerate(s) }
        
        intervals = []
        for c in set(s):
            beg, end = fst[c], lst[c]
            bad, idx = False, beg
            
            while idx <= end:
                end = max(end, lst[s[idx]])
                if fst[s[idx]] < beg:
                    bad = True
                    break
                idx += 1

            if not bad:
                intervals.append((end, beg))
                
        ans, prev = [], -1
        for end, beg in sorted(intervals):
            if beg > prev:
                ans.append(s[beg:end + 1])
                prev = end
        
        return ans