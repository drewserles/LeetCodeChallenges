'''
Input LLs are sorted. Result should be a single LL, returning a head value thats pointing to the starting place

-maintain a slow pointer, which is the node where we're deciding what it's going to point to
-list1 and list2 are going to traverserse their respective lists.
At each step we want to do the same thing    
    -compare values, and find the smaller one.
    -slow gets pointed to this one, and the list pointer gets incremented

End when one of the lists is done
Create a dummy header to get around the edge case of starting off.
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        head = ListNode()
        slow = head
        while 1:
            if not list1:
                slow.next = list2
                break
            elif not list2:
                slow.next = list1
                break
            
            if list1.val <= list2.val:
                slow.next = list1
                list1 = list.next
            else:
                slow.next = list2
                list2 = list.next
            slow = slow.next


        return head.next


if __name__ == "__main__":
    sol = Solution()
    
    print(sol.function_name())