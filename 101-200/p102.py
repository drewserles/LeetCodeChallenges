# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root):
        if not root: return []
        level_nodes = [root]
        res = []
        
        while len(level_nodes) > 0:
            res.append([node.val for node in level_nodes])
            level_nodes = [x for node in level_nodes for x in (node.left,node.right) if x]
        return res

if __name__ == "__main__":
    t7 = TreeNode(3)
    t6 = TreeNode(12, left=t7)
    t5 = TreeNode(10, right=t6)
    t4 = TreeNode(7)
    t3 = TreeNode(1)
    t2 = TreeNode(5, left=t3, right=t4)
    t1 = TreeNode(8, left=t2, right=t5)

    sol = Solution()
    print(sol.levelOrder(t1))