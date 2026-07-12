class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        n=len(arr)

        arr=[(v,i)for i,v in enumerate(arr)]
        arr.sort()
        res=[0]*n

        r=1
        for i,(v,original_i) in enumerate(arr):
            if i>0 and arr[i][0]!=arr[i-1][0]:
                r+=1
            res[original_i]=r
        return res