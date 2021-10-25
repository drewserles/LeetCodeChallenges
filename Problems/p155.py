'''
Many interesting ways of doing this. Here I'm maintaining a min heap (priority queue) as well as an array for the stack.

Check out my past submissions for some other cool ideas.
-It's pretty fast to just maintain a min value and whenever you pop off the min you do a min search on the stack to update min
-At each push you add on the min of the stack before it was added on. Then when it gets popped off you can update the min to what is contained
in the remaining stack. I like this one.
'''

import heapq
class MinStack:

    def __init__(self):
        self.stack = []
        self.heap = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        heapq.heappush(self.heap, val)
        

    def pop(self) -> None:
        val = self.stack.pop()
        self.heap.remove(val)
        heapq.heapify(self.heap)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.heap[0]
        

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    print(obj.getMin())
    obj.pop()
    print(obj.top())
    print(obj.getMin())
    print(obj.stack)
    print(obj.heap)