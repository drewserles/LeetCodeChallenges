class Solution:
    def print_check(self, num):
        print(bin(num), bin(self.findComplement(num)))

    def findComplement(self, num: int) -> int:
        return num ^ 2**num.bit_length() - 1

if __name__ == "__main__":
    sol = Solution()

    sol.print_check(10)
    sol.print_check(1)
    sol.print_check(20)