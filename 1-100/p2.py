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
    # Creates a new node to combine L1 and L2 values
    def addTwoNumbers_v1(self, l1, l2):
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

    '''
    Modifies L1 in place.
    -Keep a pointer at the start of L1 that will be returned at the end.
    -At each step, replace the value of the L1 node with l1.val + l2.val + carry
    -If L2 has gotten to its end then just ignore it going forward. No value to add to the sum
    -If L1 has gotten to its end then two options:
        -If L2 is also done then create another node with the carry (if there is one) or end if carry is 0
        -If L2 is not done then point L1 to L2
    '''
    def addTwoNumbers(self, l1, l2):
        carry, head, single = 0, l1, False

        while 1:
            val = carry + l1.val

            if l2 and not single:
                val += l2.val
                l2 = l2.next
                
            l1.val = val % 10
            carry = val // 10

            # The L1 train is ending. handle a couple situations. Not l2 was already incremented above so we point to l2 here, not l2.next
            if not l1.next:
                # if L1 is on the L2 chain, or if L2 is also done then we're done (L2 previously ended done or finishing at same time)
                if single or not l2:
                    if carry == 1:
                        l1.next = ListNode(1)
                    break
                # If l2 isn't done then switch L1 to the L2 chain 
                else:
                    single = True
                    l1.next = l2
            
            l1 = l1.next
        
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