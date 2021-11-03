# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
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