# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        st1 = []
        st2 = []
        curr1 = l1
        curr2 = l2
        while curr1:
            st1.append(curr1.val)
            curr1 = curr1.next
        
        while curr2:
            st2.append(curr2.val)
            curr2 = curr2.next

        
        if len(st1)>len(st2):
            c = l1
        else:
            c = l2
        
        carry = 0
        head = None

        while st1 or st2 or carry:
            x = st1.pop() if st1 else 0
            y = st2.pop() if st2 else 0

            total = x + y + carry

            digit = total % 10
            carry = total // 10

            newnode = ListNode(digit)
            newnode.next = head
            head = newnode

        return head

