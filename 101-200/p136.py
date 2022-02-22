class Solution:
    # This uses extra memory to create the sets so no good
    def singleNumber_v1(self, nums: int) -> int:
        return 2*sum(set(nums)) - sum(nums)

    # The trick is to use XOR. Each number that occurs twice will turn bits on and then off again on the second occurrence
    # Importantly, if there's overlap with existing on bits in the tally, the second occurrence just un-does the effect of the first.
    # So whatever is left is the singleton
    def singleNumber(self, nums):
        tally = 0
        for n in nums:
            tally ^= n
        return tally


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
    