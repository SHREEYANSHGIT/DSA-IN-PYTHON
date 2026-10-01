# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reorderList(self, head):
        slow = head
        fast = head
        start = head

        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        if fast.next is not None:
            fast = fast.next
            slow = slow.next

        # reverse
        curr = slow.next
        slow.next = None
        prev = None

        while curr:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        head2 = prev

        head1 = head


        while head2:
            c1 = head1.next
            c2 = head2.next

            head1.next = head2
            head2.next = c1

            head1 = c1
            head2 = c2

        return start