# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        nonenode = ListNode(None)
        curr = nonenode
        carry = 0

        while l1 or l2 or carry !=0:
            if l1 :
                v1 = l1.val
            else:
                v1 = 0
            
            if l2:
                v2 = l2.val
            else:
                v2 =0
            
            total = v1 + v2 + carry
            carry = total//10
            
            newval = total%10
            curr.next = ListNode(newval)
            curr = curr.next
        
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            
        headnode = nonenode.next

        return headnode


    
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        