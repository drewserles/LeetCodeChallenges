'''
Problem 55: https://leetcode.com/problems/jump-game/
Step backwards through the array.
What matters is if a path exists to the end. The key is that any intermediate step that has a path to the end
would also be accessibly by a different, more direct, path. The number at each index is the maximum jump size.
'''
class Solution:
    def canJump(self, nums):
        end_idx = len(nums) - 1
        cur_idx = end_idx
        for i in range(end_idx, -1, -1):
            jump_required = cur_idx - i
            jump_possible = nums[i]
            if jump_possible >= jump_required:
                cur_idx = i
        return cur_idx == 0

if __name__ == "__main__":
    nums = [3,2,1,0,4]
    sol = Solution()
    print(sol.canJump(nums))