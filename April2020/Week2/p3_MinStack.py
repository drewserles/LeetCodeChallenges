class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = None
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min is None or x < self.min:
            self.min = x
        

    def pop(self) -> None:
        top = self.stack.pop()
        if top == self.min:
            if len(self.stack) == 0:
                self.min = None
            else:
                self.min = min(self.stack)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min


# Easy to do something that gets the minimum by recalculating it each time.
# What about something that tracks the minimimum so it can be retrieved in constant time?
if __name__ == "__main__":
    sol = MinStack()
    sol.push(0)
    sol.push(1)
    print(sol.getMin())
    print(sol.getMin())


