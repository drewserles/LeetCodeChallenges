# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
Input: ascending-sorted linked list
Could do this the same way as p108 where we traverse the LL to populate an array, but that's not very interesting.
See if I can use the linked list directly.
'''
class Solution:
    def sortedListToBST(self, head):
        return head


if __name__ == "__main__":
    sol = Solution()
    l1 = ListNode(5)
    print(sol.sortedListToBST(l1))