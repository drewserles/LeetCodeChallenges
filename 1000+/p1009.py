'''
Same as 476
'''
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        else:
            return 2**n.bit_length()-1 ^ n

if __name__ == "__main__":
    sol = Solution()
    n = 10
    print(sol.bitwiseComplement(n))