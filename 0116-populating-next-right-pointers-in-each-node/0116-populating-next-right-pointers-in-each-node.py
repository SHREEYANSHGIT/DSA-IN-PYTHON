"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        if root is None:
            return root
        queue = deque([root])
        level = 0

        while queue:
            level += 1
            prev = None
            newnext = None
            for _ in range(len(queue)):
                e = queue.popleft()
                newnext = e
                if prev is not None:
                    prev.next = newnext
                    prev = newnext
                else:
                    prev = newnext

    
                if e.left is not None:
                    queue.append(e.left)

                if e.right is not None:
                    queue.append(e.right)
                
                prev.next = None

            

        return root
