# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Strategy: middle element of array is the current Node value. All smaller elements are in the left child, all larger
are in the right child.
Build tree recursively.
'''
class Solution:
    def sortedArrayToBST(self, nums):
        if len(nums) == 0:
            return None
        
        sp = len(nums)//2
        
        return TreeNode(val=nums[sp], left=self.sortedArrayToBST(nums[:sp]), right=self.sortedArrayToBST(nums[sp+1:]))