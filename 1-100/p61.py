'''
A couple thoughts:
-when k is equal to the length of the list we're back where we started. So do a k % len to figure out how many rotations we need
-Going to need to figure out the length of the list -> do one O(n) run through to count it
-Little bit of arithmetic to figure out what the head of the new list will be.
    >1 rotation the last node will become the first, 2 rotations the second last will become the first
    >L-1 jumps to the end, L-2 to the second end, etc -> you need (L - num rotations) to get to your new head

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def print_ll(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res
    def rotateRight(self, head, k):
        if head is None:
            return head
        # find length
        len = 0
        p = head
        while p is not None:
            len += 1
            if p.next is None:
                break # Want to keep a pointer on the end for link up reasons
            p = p.next
        # rotations required
        k %= len
        if k == 0:
            return head
        # Some rotations are required, so link up the old end with the old head
        p.next = head
        # Number of jumps to get to the new head -> want the one before the new head for pointer reasons so take another 1 off
        jumps = len-k-1
        # I
        p = head
        for _ in range(jumps):
            p = p.next
        head = p.next
        p.next = None
        return head
        


if __name__ == "__main__":
    sol = Solution()
    head = [1,2,3,4,5]
    
    
    for k in range(10):
        l5 = ListNode(5)
        l4 = ListNode(4, l5)
        l3 = ListNode(3, l4)
        l2 = ListNode(2, l3)
        l1 = ListNode(1, l2)
        res = sol.rotateRight(None, k)
        print(sol.print_ll(res))