'''
Cycle detection: use Floyd's algorithm
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def hasCycle(self, head):
        fast, slow = head, head

        # Find meeting point - where slow pointer and fast pointer meet
        while True:
            # Get to an end then there's no cycle
            if not (fast and fast.next and fast.next.next):
                return False
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True


if __name__ == "__main__":
    sol = Solution()

    #head = [3,2,0,-4]
    #pos = 1 # internal value: this is the answer
    
    n4 = ListNode(-4)
    n3 = ListNode(0, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(3, n2)
    n4.next = n2
    
    print(sol.hasCycle(n1))