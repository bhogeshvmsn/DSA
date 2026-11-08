class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d=defaultdict(int)
        for i in t:
            d[i]+=1
        formed,total=0,len(d)
        l=r=0
        len_ans=float('inf')
        subl,subr=0,0

        while r<len(s):
            c=s[r]
            if c in d:
                d[c]-=1
                if d[c]==0:
                    formed+=1
            while l<=r and formed==total:
                cur_len=r-l+1
                if cur_len<len_ans:
                    len_ans=cur_len
                    subl,subr=l,r+1
                c=s[l]
                if c in d:
                    if d[c]==0:
                        formed-=1
                    d[c]+=1
                l+=1
            r+=1
        return "" if len_ans==float('inf') else s[subl:subr]