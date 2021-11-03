# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    queue = [root]
    res = []
    while len(queue) > 0:
        node = queue.pop(0)
        if node:
            res.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
    return res

class Solution:
    def sumRecurse(self, root, tally):
        if root is None:
            return 0
        tally = tally*10 + root.val
        if root.left is None and root.right is None:
            return tally
        else:
            return self.sumRecurse(root.left, tally) + self.sumRecurse(root.right, tally)
    def sumNumbers(self, root):
        return self.sumRecurse(root, 0)



if __name__ == "__main__":
    ll = TreeNode(5)
    lr = TreeNode(1)
    l = TreeNode(9, ll, lr)
    r = TreeNode(0)
    root = TreeNode(4, l, r)

    sol = Solution()
    print(printTree(root))
    print(sol.sumNumbers(root))