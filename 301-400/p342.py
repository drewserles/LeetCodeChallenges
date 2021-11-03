import math
class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # Without loop
        if num <= 0:
            return False
        val = math.log(num, 4)
        return val == int(val)