# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Strategy: BFS traversal of a tree. Construct the next level to explore base on the children of the current level and include Nulls.
While exploring a level also keep track of its width.
    The existence of a node creates a width of 1. Gaps of null children are fine if they end up being enclosed.
    Need a little algorithm to return the width of a layer given its

There's a question about counting Nulls here that I don't have an answer for that would change everything.
Do you count all actual Nulls or the possible Nulls in the middle? Yes you do. E.g. [1,3,2,5,null,null,9,6,null,null,7]
gives 8 instead of 4
'''


class Solution:
    def widthOfBinaryTree(self, root):
        level = [(root, 0)]
        max_width = 0
        while len(level) > 0:
            next_level = []
            left = -1
            width = 0
            for node in level:
                # Track width 
                if node[0] is not None:
                    if left == -1:
                        left = node[1]
                    width = node[1] - left + 1
                    
                    next_level.append((node[0].left, 2*node[1]))
                    next_level.append((node[0].right, 2*node[1]+1))
            level = next_level
            if width > max_width:
                max_width = width
        return max_width


                # Create next level

if __name__ == "__main__":
    sol = Solution()
    
    t6 = TreeNode(9)
    t5 = TreeNode(3)
    t4 = TreeNode(5)

    t2 = TreeNode(3, t4, t5)
    t3 = TreeNode(2, None, t6)

    t1 = TreeNode(1, t2, t3)

    print(sol.widthOfBinaryTree(t1))