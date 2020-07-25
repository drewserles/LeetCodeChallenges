# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorder_traversal(self, node:TreeNode):
        #Generate tree by recursively calling
        # Base: if node is None, return None
        if not node:
            return [None]
        elif not node.left and not node.right:
            return [node.val]
        else:
            return [node.val] + self.preorder_traversal(node.left) + self.preorder_traversal(node.right)

    def bstFromPreorder(self, preorder) -> TreeNode:
        if len(preorder) == 0:
            return None
        gt = len(preorder)
        for i in range(1, gt):
            if preorder[i] > preorder[0]:
                gt = i
                break
        ls = preorder[1:gt]
        rs = preorder[gt:]
        return TreeNode(preorder[0], self.bstFromPreorder(ls), self.bstFromPreorder(rs))

if __name__ == "__main__":
    sol = Solution()
    # preorder = [8,5,1,7,10,12]
    # print(sol.bstFromPreorder(preorder))   
    t6 = TreeNode(12)
    t5 = TreeNode(10, right=t6)
    t4 = TreeNode(7)
    t3 = TreeNode(1)
    t2 = TreeNode(5, left=t3, right=t4)
    t1 = TreeNode(8, left=t2, right=t5)
    head = sol.bstFromPreorder([8,5,1,7,10,12])
    print(sol.preorder_traversal(t1))