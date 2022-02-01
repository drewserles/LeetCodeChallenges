'''
In progress
'''

class Solution:
    def findMaximumXOR(self, nums):
        res = 0
        # nums.sort()
        big_n = max(nums)
        for i in range(len(nums)):
            val = nums[i] ^ big_n
            if val > res:
                res = val
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [14,70,53,83,49,91,36,80,92,51,66,70]
    print(sol.findMaximumXOR(nums))