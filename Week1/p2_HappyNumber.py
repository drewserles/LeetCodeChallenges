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
        