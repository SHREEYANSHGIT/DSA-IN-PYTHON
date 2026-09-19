class Solution(object):
    def removeNodes(self, head):
        st = []
        c = head

        while c:
            while st and st[-1].val < c.val:
                st.pop()

            st.append(c)
            c = c.next

        keep = set(st)

        dummy = ListNode(0)
        prev = dummy
        curr = head

        while curr:
            if curr in keep:
                prev.next = curr
                prev = curr

            curr = curr.next

        prev.next = None

        return dummy.next