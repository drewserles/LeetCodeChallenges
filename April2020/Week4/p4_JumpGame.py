class Solution:
    def canJump(self, nums) -> bool:
        length = len(nums)
        idx_get_end = length - 1
        for i in range(length-1, -1, -1):
            if nums[i] >= idx_get_end - i:
                idx_get_end = i
        return idx_get_end == 0

if __name__ == "__main__":
    sol = Solution()
    nums = [2,3,1,1,4]
    print(sol.canJump(nums))