'''
Problem 55 (medium): https://leetcode.com/problems/jump-game/
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

'''
Alternate solution going forwards through array. Keep track of the furthest spot you can get through
'''
class Solution:
    def canJump(self, nums):
        end_idx = len(nums)-1
        furthest = 0
        for i in range(len(nums)):
            if i > furthest:
                break
            furthest = max(furthest, i+nums[i])
            if furthest >= end_idx:
                return True
        return False

if __name__ == "__main__":
    nums = [0]
    sol = Solution()
    print(sol.canJump(nums))