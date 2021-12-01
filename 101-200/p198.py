'''
Cool dynamic programming solution (memoization)
Just grow the number of houses one at a time. At each house record the max that can be stolen
    which is either the loot up to 2 houses ago + this house, or the loot up to past house - because of the adjacency requirement.

Good reminder to shrink problems down then grow them up.
'''
class Solution:
    def rob(self, nums):
        p1, p2 = 0,0
        for i in range(len(nums)):
            p2, p1 = p1, max(p1, p2 + nums[i])
        return p1



if __name__ == "__main__":
    sol = Solution()
    nums = [2,7,9,3,1]
    print(sol.rob(nums))