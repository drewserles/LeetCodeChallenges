'''
Bitshift method
'''
class Solution:
    def isPowerOfTwo(self, n):
        while not n & 1 and n > 0:
            n >>= 1
        return n == 1

    # Very clever alternate trick! A number 1 less than a power of 2 is going to be all 1s where n is all 0s
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n-1) == 0
                





if __name__ == "__main__":
    sol = Solution()
    n = -16
    print(sol.isPowerOfTwo(n))