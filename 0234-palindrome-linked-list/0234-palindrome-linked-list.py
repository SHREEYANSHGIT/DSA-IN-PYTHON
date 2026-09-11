class Solution(object):
    def isPalindrome(self, head):
        slow = head
        fast = head

        # Find middle
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half
        curr = slow
        prev = None

        while curr is not None:
            front = curr.next
            curr.next = prev
            prev = curr
            curr = front

        # Compare first half and reversed second half
        shead = head
        nhead = prev

        while nhead is not None:
            if shead.val != nhead.val:
                return False

            shead = shead.next
            nhead = nhead.next

        return True