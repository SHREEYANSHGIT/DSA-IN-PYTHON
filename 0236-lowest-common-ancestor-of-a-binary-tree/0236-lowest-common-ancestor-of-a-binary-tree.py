class Solution(object):
    def dfs(self,root,p,q):
        if root == None:
            return 
        if root == p :
            return p
        if root == q :
            return q
        l = None
        if root.left:
            l = self.dfs(root.left,p,q)
        r = None
        if root.right:
            r = self.dfs(root.right,p,q)
        
        if l and r:
            return root 
        
        if l and not r:
            return l
        if r and not l:
            return r
            
    def lowestCommonAncestor(self, root, p, q):
        return self.dfs(root,p,q)

        