'''
Problem 2 (medium): https://leetcode.com/problems/add-two-numbers/

Inputs are LL of digits from least significant to most. Add them together like normal addition, digit by digit keeping track of the carry.
Iterate until you get to the end of both linked lists. Could have an additional carry left over at the end that needs to be included, hence the
extra or condition on the while loop.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        carry = 0
        head, p = None, None
        while l1 or l2 or carry>0:
            next_val = carry
            if l1:
                next_val += l1.val
                l1 = l1.next
            if l2:
                next_val += l2.val
                l2 = l2.next
            new = ListNode(next_val % 10)
            if head is None:
                head = new
                p = head
            else:
                p.next = new
                p = p.next
            carry = next_val // 10
        return head


if __name__ == "__main__":
    # Testing this: l1 = [2,4,3], l2 = [5,6,4]
    l1_3 = ListNode(3)
    l1_2 = ListNode(4, l1_3)
    l1 = ListNode(2, l1_2)

    l2_3 = ListNode(4)
    l2_2 = ListNode(6, l2_3)
    l2 = ListNode(5, l2_2)

    sol = Solution()

    res_ll = sol.addTwoNumbers(l1, l2)
    res_l = []
    while res_ll:
        res_l.append(res_ll.val)
        res_ll = res_ll.next
    print(res_l)