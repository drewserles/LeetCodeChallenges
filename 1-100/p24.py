'''
Very odd behaviour challenging how I understand single line swaps!
If I use "cur.next, cur.next.next = cur.next.next, cur"
Instead of "cur.next.next, cur.next = cur, cur.next.next"
the whole thing falls apart.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_ll(root):
    res = []
    while root:
        res.append(root.val)
        root = root.next
    return res

class Solution:
    def swapPairs(self, head):
        cur = head
        while cur and cur.next:
            
            # Special case: at the start
            if cur == head:
                # only time we need to move the head pointer
                head = head.next

            # whole rest
            else:
                prev.next = cur.next

            cur.next.next, cur.next = cur, cur.next.next
            prev = cur
            cur = cur.next
        return head



if __name__ == "__main__":
    sol = Solution()
    l5 = ListNode(5)
    l4 = ListNode(4)
    l3 = ListNode(3, l4)
    l2 = ListNode(2, l3)
    l1 = ListNode(1, l2)

    print(f'Before swap: {print_ll(l1)}')
    swap_head = sol.swapPairs(l1)
    print(f'After: {print_ll(swap_head)}')