'''
Question was not very clear. Standing on the right side of the tree means moving down the tree, on the right side,
and seeing what you see on each level. So you want to return the rightmost node at each level.
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rightSideView(self, root):
        if not root: return []
        queue = [root]
        views = []
        while len(queue) > 0:
            next_level = []
            views.append(queue[-1].val)
            for n in queue:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            queue=next_level
        return views


if __name__ == "__main__":
    l5 = TreeNode(5)
    l4 = TreeNode(4)
    l3 = TreeNode(3)
    l2 = TreeNode(2, l4)
    l1 = TreeNode(1, l2, l3)

    sol = Solution()
    print(sol.rightSideView(l1))