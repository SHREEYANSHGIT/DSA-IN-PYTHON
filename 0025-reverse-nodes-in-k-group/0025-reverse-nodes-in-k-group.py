# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):

    def reverseKTimes(self, start, k):

        prev = None
        curr = start

        while k > 0:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front
            k -= 1

        return prev, start, curr


    def reverseKGroup(self, head, k):

        if head is None or k == 1:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prevPair = dummy
        curr = head

        while curr:

            # Check if k nodes are available
            temp = curr
            count = 0

            while temp and count < k:
                temp = temp.next
                count += 1

            # Less than k nodes left
            if count < k:
                break

            # Reverse k nodes
            newHead, newTail, nextPair = self.reverseKTimes(curr, k)

            # Connect previous part
            prevPair.next = newHead
            newTail.next = nextPair

            # Move pointers
            prevPair = newTail
            curr = nextPair

        return dummy.next