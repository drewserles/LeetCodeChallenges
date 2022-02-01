# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode):
        def inorder_trav(root):
            if root is None:
                return []
            return inorder_trav(root.left) + [root.val] + inorder_trav(root.right)
        
        tree1 = inorder_trav(root1)
        tree2 = inorder_trav(root2)
        i,j = 0, 0
        res = []
        while i < len(tree1) and j < len(tree2):
            if tree1[i] <= tree2[j]:
                res.append(tree1[i])
                i += 1
            else:
                res.append(tree2[j])
                j += 1
        return res + tree1[i:] + tree2[j:]


if __name__ == "__main__":
    sol = Solution()
    # root1 = [2,1,4], root2 = [1,0,3]
    print(sol.getAllElements())