# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

    def printTree(self, root):
        queue = [root]
        res = []
        while len(queue) > 0:
            node = queue.pop(0)
            if node:
                res.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
        return res


if __name__ == "__main__":
    ll = TreeNode(1)
    lr = TreeNode(3)
    rl = TreeNode(6)
    rr = TreeNode(9)
    l = TreeNode(2, ll, lr)
    r = TreeNode(7, rl, rr)
    root = TreeNode(4, l, r)

    sol = Solution()
    print(sol.printTree(root))
    inverted = sol.invertTree()
    print(sol.printTree(inverted))
