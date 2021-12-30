'''
Do it without any Python string/binary conversions - multiply by 2
'''
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # Go through once and collect then go through again and sum
    def getDecimalValue_o(self, head):
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        r, m = 0, 1
        for v in reversed(vals):
            r += m*v
            m *= 2
        return r

    # Version 2 where you do it with a forward pass by shifting by base (mult by 2)
    # Oddly this is much slower on Leetcode. No idea why that would be the case
    def getDecimalValue(self, head):
        res = 0
        while head:
            res = 2*res + head.val
            head = head.next
        return res

if __name__ == "__main__":
    l4 = ListNode(0)
    l3 = ListNode(1, l4)
    l2 = ListNode(0, l3)
    l1 = ListNode(1, l2)

    sol = Solution()

    print(sol.getDecimalValue(l1))