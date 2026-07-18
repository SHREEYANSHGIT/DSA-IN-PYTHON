# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None or k == 0:
            return head
        curr = head
        prev = head
        start = head
        n = 1
        while curr.next is not None :
            curr=curr.next
            n +=1

        x = k%n
        if x == 0:
            return head
        for _ in range(0,n-x-1):
            prev = prev.next
        
        new_head = prev.next
        
        prev.next = None
        curr.next = start

        return new_head





        