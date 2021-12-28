class Solution:
    def rob(self, nums):
        # (include first house, does not include first house)
        # [1,3,2, 4]
        # (1, 0), (1, 3), (3, 3), // (3, 7)
        p1 = (nums[0],0)
        p2 = (0,0)
        for i in range(1, len(nums)-1):
            cur = nums[i]
            include_first = max(p1[0], p2[0] + cur)
            exclude_first = max(p1[1], p2[1] + cur)
            p1, p2 = (include_first, exclude_first), p1
        # Last value
        return max(p1[0], p1[1], p2[0], p2[1] + nums[-1])
            



if __name__ == '__main__':
    sol = Solution()
    nums = [4,2,1, 5]
    print(sol.rob(nums))