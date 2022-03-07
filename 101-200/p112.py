# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


'''
Plan: DFS traversal returning True when the targetSum is reached
Note the sum needs to be reached at a leaf.
'''
class Solution:
    def hasPathSum_dfs(self, root, targetSum):
        if not root:
            return False
        val = targetSum - root.val
        # Sum achieved and it's a leaf
        if val == 0 and not root.left and not root.right:
            return True
        else:
            return self.hasPathSum(root.left, val) or self.hasPathSum(root.right, val)

    # try it as a BFS
    def hasPathSum(self, root, targetSum):
        queue = []
        if root:
            queue.append((root, targetSum))

        while len(queue) > 0:
            node,val = queue.pop(0)
            new_targ = val - node.val
            
            if new_targ == 0 and not node.left and not node.right:
                return True
            if node.left:
                queue.append((node.left, new_targ))
            if node.right:
                queue.append((node.right, new_targ))

        return False

if __name__ == "__main__":
    sol = Solution()
    n4 = TreeNode(4)
    n3 = TreeNode(3, n4)
    n2 = TreeNode(2)
    n1 = TreeNode(1, n2, n3)
    targetSum = 5
    print(sol.hasPathSum(None,  8))