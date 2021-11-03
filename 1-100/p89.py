'''
I really liked this problem.
The first number (0) and the last have to be 1 bit apart,
the last number can be a 1 in most significant bit and 0 for all the rest. E.g. 100 for n=3

If you go up to n=4 then we have to move from 100, and the only way to do that it is go to 1100.
The important thing to notice is that the last 3 digits are still the same as the previous step, so
we could walk through all the previous sequence in reverse but not with an additional 1 at the front.
This gets us all the numbers up to 1111 and ends with 1000.
'''

class Solution:
    def grayCode(self, n):
        res = [0, 1]
        for i in range(1, n):
            sig_bit = 2**i
            res += [x + sig_bit for x in res[::-1]]
        return res

sol = Solution()
print(sol.grayCode(4))
