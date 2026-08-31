# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        arr=[]
        while head:
            arr.append(head.val)
            head=head.next
        n=len(arr)
        cri=[]
        for i in range(1,n-1):
            if arr[i-1]>arr[i]<arr[i+1] or arr[i-1]<arr[i]>arr[i+1]:
                cri.append(i)

        if len(cri)<2: return [-1,-1]
        mx=cri[-1]-cri[0]
        mn=inf
        for i in range(1,len(cri)):
            mn=min(mn,cri[i]-cri[i-1])
        return [mn,mx]
        