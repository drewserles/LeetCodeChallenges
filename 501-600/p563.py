# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree_recurse(self, root):
        # Return the tilt of the subtree rooted at this node as well as the sum
        if not root:
            # Tilt, subtree sum
            return 0, 0
        else:
            lsum, ltilt = self.tree_recurse(root.left)
            rsum, rtilt = self.tree_recurse(root.right)
            tsum = root.val + lsum + rsum
            tilt = abs(lsum-rsum)
            tot_tilt = ltilt + rtilt + tilt
            return tsum, tot_tilt


    def findTilt(self, root):
        _, tilt = self.tree_recurse(root)
        return tilt


if __name__ == "__main__":
    n6 = TreeNode(7)
    n5 = TreeNode(5)
    n4 = TreeNode(3)
    n3 = TreeNode(9, None, n6)
    n2 = TreeNode(2, n4, n5)
    n1 = TreeNode(4, n2, n3)

    sol = Solution()
    print(sol.findTilt(n1))