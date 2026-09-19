# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodes(self, head):
        a = []
        curr= head
        while curr is not None:
            a.append(curr.val)
            curr = curr.next
        
        n = len(a)
        ans = [-1]*n
        st = []

        for i in range(n-1,-1,-1):
            while st and st[-1] <= a[i]:
                st.pop()
            
            if st and st[-1] > a[i]:
                ans[i] = st[-1]
            else:
                ans[i] = 0
            st.append(a[i])

        return ans 

        