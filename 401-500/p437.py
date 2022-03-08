# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
PathSum 3: different is now that the path can start at any point
I think this means that I need to track every possible running tally to that point
E.g. path of 5,2,1 to a leaf. The sums would be 5 at the first spot, then [7,2] at the second, then [8,3,1]
I'll call this a sumlist and recalculate it at each node and pass it forwards

Want to return the number of possible paths so need to return a count
Base case 1: root is Null, return 0
Base case 2:
'''
class Solution:
    def pathSum(self, root, targetSum):
        def dfs(root, path_sums):
            # Base: Null root return 0
            if not root:
                return 0
            # Update the existing paths to include this root's value - don't forget this node
            path_sums = [x + root.val for x in path_sums] + [root.val]

            # Current count of paths that meet the target
            path_count = sum(x==targetSum for x in path_sums)

            return path_count + dfs(root.left, path_sums) + dfs(root.right, path_sums)
        return dfs(root, [])

if __name__ == "__main__":
    sol = Solution()
    
    targetSum = 8
    print(sol.pathSum())