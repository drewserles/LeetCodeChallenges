class Solution:
    def singleNumber(self, nums: int) -> int:
        return 2*sum(set(nums)) - sum(nums)


if __name__ == "__main__":
    sol = Solution()
    # T1
    inp = [2,2,1]
    exp = 1
    res = sol.singleNumber(inp)
    print(f'Test 1 - Expected: {exp}, result: {res}')
    # T2
    inp = [4,1,2,1,2]
    exp = 4
    res = sol.singleNumber(inp)
    print(f'Test 2 - Expected: {exp}, result: {res}')
    