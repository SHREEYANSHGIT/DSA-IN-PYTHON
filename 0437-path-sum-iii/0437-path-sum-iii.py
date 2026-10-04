class Solution(object):

    def find(self, root, targetSum, hm, tsum):

        if root is None:
            return 0

        tsum += root.val

        count = hm.get(tsum - targetSum, 0)

        hm[tsum] = hm.get(tsum, 0) + 1

        count += self.find(root.left, targetSum, hm, tsum)
        count += self.find(root.right, targetSum, hm, tsum)

        hm[tsum] -= 1

        return count

    def pathSum(self, root, targetSum):

        hm = {0: 1}

        return self.find(root, targetSum, hm, 0)