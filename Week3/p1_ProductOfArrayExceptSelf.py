# Given an array nums of n integers where n > 1,  return an array output such that
#   output[i] is equal to the product of all the elements of nums except nums[i].
# Solve without division and in O(n)
class Solution:
    def productExceptSelf(self, nums):
        sz = len(nums)
        up, down, output = sz*[1], sz*[1], sz*[1]
        for i in range(1, sz):
            up[i] = up[i-1]*nums[i-1]
        for i in range(sz-2,-1,-1):
            # tr *= nums[i+1]
            down[i] = down[i+1]*nums[i+1]
        for i in range(sz):
            output[i] = up[i]*down[i]
        return output
    def pes_space(self, nums):
        # Only allowed to use memory for output array
        sz = len(nums)
        output = sz*[1]
        tr = 1
        for i in range(1, sz):
            tr *= nums[i-1]
            output[i] *= tr
        tr = 1
        for i in range(sz-2,-1,-1):
            tr *= nums[i+1]
            output[i] *= tr
        return output



if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4]
    # nums=[1,0]
    print(sol.pes_space(nums))

# Breaks my mult total idea:
# Input:
# [1,0]
# Output:
# [0,0]
# Expected:
# [0,1]