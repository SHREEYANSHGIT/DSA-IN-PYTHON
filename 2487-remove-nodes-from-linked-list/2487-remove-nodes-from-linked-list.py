class Solution(object):
    def removeNodes(self, head):
        st = []
        c = head

        while c:
            while st and st[-1].val < c.val:
                st.pop()

            st.append(c)
            c = c.next

        dummy = ListNode(0)
        prev = dummy

        for node in st:
            prev.next = node
            prev = node

        prev.next = None

        return dummy.next