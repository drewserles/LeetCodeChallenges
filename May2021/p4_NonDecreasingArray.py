# Medium. https://leetcode.com/problems/non-decreasing-array/

# Input: list of ints
# Return: Boolean
class Solution:
    def checkPossibility(self, nums):
        modified = False
        for i in reversed(range(len(nums)-1)):
            if nums[i] > nums[i+1]:
                if modified == True:
                    return False
                else:
                    modified = True
                    # nums[i] = nums[i+1]
        return True

if __name__ == "__main__":
    nums = [7, 8, 5, 10]
    sol = Solution()
    print(sol.checkPossibility(nums))