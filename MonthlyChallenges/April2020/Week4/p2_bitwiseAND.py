class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        diff = n-m
        run, common = 1, 0
        while run <= m:
            if diff < run:
                common += run
            run *= 2
        return m & n & common


if __name__ == "__main__":
    sol = Solution()
    m, n = 5, 7
    print(sol.rangeBitwiseAnd(m, n))