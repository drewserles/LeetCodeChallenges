# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
A couple tricky Python bits this question reminded me of.
1. When doing a .append() on a function input array, like val_list.append(5) it modifies the source in memory so I can't be doing this when making recursive calls.
    Good solution is to make a copy with a new variable, or reassign this variable

2. Combining lists of lists is tough to get the output shape I need (nested list when results, empty single list for nothing)
    This comment on SO helped: https://stackoverflow.com/questions/2022031/python-append-vs-operator-on-lists-why-do-these-give-different-results
    The key point: "the + operator ads an array's elements to the original array"
    Examples
    [1,2,3] + [4,5] -> [1,2,3,4,5]. The second array's elements are added to the first
    [[1,2,3]] + [4,5] -> [[1,2,3], 4, 5]. We can have mixed type arrays in Python
    [[1,2,3]] + [[4,5],[6,7]] -> [[1,2,3],[4,5],[6,7]]
'''
class Solution:
    def hasPathSum(self, root, targetSum):

        def dfs(root, targetSum, val_list):
            if not root:
                return []
            val = targetSum - root.val
            next_arr = val_list + [root.val]
            # Found one
            if val == 0 and not root.left and not root.right:
                return [next_arr]
            # Go deepter
            return dfs(root.left, val, next_arr) + dfs(root.right, val, next_arr)

        return dfs(root, targetSum, [])


if __name__ == "__main__":
    sol = Solution()
    n4 = TreeNode(4)
    n3 = TreeNode(2)
    n2 = TreeNode(2, n3)
    n1 = TreeNode(1, n2, n4)
    targetSum = 5
    print(sol.hasPathSum(n1,  targetSum))