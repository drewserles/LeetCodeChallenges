# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def work(self, root: TreeNode) -> int:
        # Observation: longest path doesn't necessarily go through origin. So need to track both
        # Also need to return a single number so just use another function to select at the end
        if root:
            l_max_str, l_max_wid = self.work(root.left)
            r_max_str, r_max_wid = self.work(root.right)
            straight = 1 + max(l_max_str, r_max_str) # longest path upwards from sub tree
            current_wid = 1 + l_max_str + r_max_str
            max_sub_wid = max(l_max_wid, r_max_wid, current_wid)
            return straight, max_sub_wid
        else:
            # Return max straight path, max sub tree width
            return 0, 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        straight, width = self.work(root)
        return max(width-1, 0)



if __name__ == "__main__":
    t4 = TreeNode(val=4)
    t5 = TreeNode(val=5, left=t4)
    t2 = TreeNode(val=2, left=t4, right=t5)
    t3 = TreeNode(val=3)
    t1 = TreeNode(val=1, left=t2, right=t3)
    #
    sol = Solution()
    print(sol.diameterOfBinaryTree(t5))