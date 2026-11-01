class Solution(object):
    def flatten(self, root):
 
        self.nextright = None
        def revpreorder(root):
            if root == None:
                return 
            
            revpreorder(root.right)
            revpreorder(root.left)

            root.left = None
            root.right = self.nextright
            self.nextright = root
        
        revpreorder(root)
        return self.nextright

            
