# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Easy Printing
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

# Recursive DFS solution
class Solution:
    def findLeftRecurse(self, root, direction):
        # If it's null send back 0
        if root is None:
            return 0
        # If it's a leaf send back the value for a left leaf or 0 for a right leaf
        if root.left is None and root.right is None:
            return direction*root.val
        else:
            return self.findLeftRecurse(root.left, 1) + self.findLeftRecurse(root.right, 0)
    def sumOfLeftLeaves(self, root):
        # 1 if it's a left branch, 0 if it's a right. Start by sending 0 for the root/
        return self.findLeftRecurse(root, 0)



if __name__ == "__main__":
    rl = TreeNode(15)
    rr = TreeNode(7)
    l = TreeNode(9)
    r = TreeNode(20, rl, rr)
    # root = TreeNode(3, l, r)
    root = TreeNode(3, l)

    sol = Solution()
    print(printTree(root))
    print(sol.sumOfLeftLeaves(root))