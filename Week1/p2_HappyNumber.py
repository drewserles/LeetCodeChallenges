#n is positive, so >0
class Solution:
    def square_digs(self, n):
      tot = 0
      while n > 0:
        tot += (n % 10)**2
        n //= 10
      return tot
    
    def isHappy(self, n: int) -> bool:
      seen = set()
      while n > 1:
        if n in seen:
          return False
        else:
          seen.add(n)
          n = self.square_digs(n)
      return True

if __name__ == '__main__':
    sol = Solution()
    # T1
    inp = 19
    exp = True
    res = sol.isHappy(inp)
    print(f'Test 1 - Expected: {exp}, result: {res}')
    # T2
    inp = 5
    exp = False
    res = sol.isHappy(inp)
    print(f'Test 2 - Expected: {exp}, result: {res}')
