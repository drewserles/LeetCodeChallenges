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

    # Fast and slow pointer option
    def middleNode(self, head):
        p = head.next
        while p:
            if not p.next:
                return head.next
            else:
                head = head.next
                p = p.next.next
        return head

    # One pointer to run through and calculate middle
    def middleNode_v2(self, head):
        p1, p2 = head, head
        cnt = 0
        while p1:
            cnt += 1
            p1 = p1.next
        # How many to increment p2?
        # if the chain has 3, want to increment it once (go from 1->2)
        # if the chain has 7, want to increment it 3x (1->4)
        # if the chain has 8, want to incrememnt it 4x (1->5)
        # This looks like integer division
        for inc in range(cnt//2):
            p2 = p2.next
        return p2

if __name__ == "__main__":
    l6 = ListNode(6)
    l5 = ListNode(5, l6)
    l4 = ListNode(4, l5)
    l3 = ListNode(3, l4)
    l2 = ListNode(2)
    l1 = ListNode(1, l2)

    sol = Solution()
    print(sol.print_ll(l1))

    mid = sol.middleNode((l1))
    print(sol.print_ll(mid))