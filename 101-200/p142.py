'''
Return the listnode that starts the cycle

Really intersting problem. The solution uses Floyd's cycle detection algorithm: https://en.wikipedia.org/wiki/Cycle_detection
I had help from the comments when doing this - try doing it again in the future and see if fully get it.

Hint: do the math and find where the fast and slow pointers meet. Then use what we know about the meeting position to find 
cycle start node distance from linked list stat.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next

class Solution:
    def detectCycle(self, head):
        fast, slow = head, head

        # Find meeting point - where slow pointer and fast pointer meet
        while True:
            # Get to an end then there's no cycle
            if not (fast and fast.next and fast.next.next):
                return None
            
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        # Single step from head and from meeting point. The point where those two meet is start of the cycle
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow


if __name__ == "__main__":
    sol = Solution()

    #head = [3,2,0,-4]
    #pos = 1 # internal value: this is the answer
    
    n4 = ListNode(-4)
    n3 = ListNode(0, n4)
    n2 = ListNode(2, n3)
    n1 = ListNode(3, n2)
    n4.next = n2
    
    res = sol.detectCycle(n1)
    if not res:
        print('no cycle')
    else:
        print(res.val)