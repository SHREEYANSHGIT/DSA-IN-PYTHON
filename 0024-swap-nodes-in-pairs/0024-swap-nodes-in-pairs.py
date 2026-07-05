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


    def swapPairs(self, head):

        dummy = ListNode(0)
        dummy.next = head

        prevPair = dummy
        curr = head

        while curr and curr.next:

            newHead, newTail, nextPair = self.reverseKTimes(curr,2)

            prevPair.next = newHead
            newTail.next = nextPair

            prevPair = newTail
            curr = nextPair

        return dummy.next
        