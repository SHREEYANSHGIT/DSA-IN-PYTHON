# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):

        ### min heap
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap,(lists[i].val, i , lists[i]))
        
        ## create a new list for merge

        head = ListNode(0)
        tail = head

        while heap:

           value , index , node = heapq.heappop(heap)

           tail.next = node
           tail = tail.next

           if node.next:
            heapq.heappush(heap,(node.next.val , index ,node.next))

        return head.next


        