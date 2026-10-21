# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        head1 = ListNode(0)
        c1 = head1
        head2 = ListNode(0)
        c2 = head2

        c = head
        f = 0
        while c is not None:
            f = c.next
            if c.val < x:
                c1.next = c
                c1 = c1.next
            else:
                c2.next = c
                c2 = c2.next
            
            c = f
        c2.next = None
        c1.next = head2.next
        return head1.next




        