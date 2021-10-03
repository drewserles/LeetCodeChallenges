class Solution:
    def compute(self, strng):
      a = []
      for c in strng:
        if c == '#':
          if len(a) > 0:
            a.pop()
        else:
          a.append(c)
      return a
    def backspaceCompare(self, S: str, T: str) -> bool:
      return self.compute(S) == self.compute(T)


if __name__ == "__main__":
    sol = Solution()
    # T1
    S = "ab#c"
    T = "ad#c"
    exp = True
    res = sol.backspaceCompare(S, T)
    print(f'Test 1 - Expected: {exp}, result: {res}')
    # T2
    S = "a#c"
    T = "b"
    exp = False
    res = sol.backspaceCompare(S, T)
    print(f'Test 2 - Expected: {exp}, result: {res}')