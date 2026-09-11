class Solution(object):
    def deleteDuplicates(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy
        curr = head

        if curr is None:
            return dummy.next

        front = curr.next

        while front is not None:

            if curr.val == front.val:
                while front is not None and curr.val == front.val:
                    front = front.next
                prev.next = front
                curr = front

                if curr is not None:
                    front = front.next

            else:
                prev = curr
                curr = front
                front = front.next

        return dummy.next