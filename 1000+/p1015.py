class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        iters, prev_rem, rems = 0, 0, set()

        while 1:
            iters += 1
            new_rem = (prev_rem*10 + 1) % k
            if new_rem == 0:
                return iters
            elif new_rem in rems:
                return -1
            else:
                rems.add(new_rem)
                prev_rem = new_rem


if __name__ == "__main__":
    k = 7
    sol = Solution()
    print(sol.smallestRepunitDivByK(k))