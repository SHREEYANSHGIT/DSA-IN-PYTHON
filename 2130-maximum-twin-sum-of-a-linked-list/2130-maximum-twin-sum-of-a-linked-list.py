# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        slow = head
        fast = head.next.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            if fast.next.next is None :
                fast = fast.next
            else : 
                fast = fast.next.next
            
        
        
        shead = head
        curr = slow.next
        prev =None
        front = curr.next
        
        while curr is not None:
            curr.next = prev
            prev =curr 
            curr = front 
            if front is not None:
                front = front.next
        
        slow.next = prev
        nhead = prev
        maxi = float('-inf')
        while nhead is not None:
            v = nhead.val + shead.val
            maxi = max(maxi,v)
            shead = shead.next
            nhead = nhead.next
        
        return maxi


            
