class Solution:
    def canJump(self, nums):
        min_jumps = [float('inf') for _ in range(len(nums)-1)] + [0]
        for i in reversed(range(len(nums)-1)):
            sz = nums[i]
            interval = min_jumps[i+1 : i+sz+1]
            if len(interval) > 0:
                min_jumps[i] = 1 + min(interval)
        return min_jumps[0]

if __name__ == "__main__":
    nums = [2,3,0,1,4]
    sol = Solution()
    print(sol.canJump(nums))