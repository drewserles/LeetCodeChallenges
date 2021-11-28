'''
First time doing this problem - July 2020
Given an array nums of n integers where n > 1,  return an array output such that
output[i] is equal to the product of all the elements of nums except nums[i].
Solve without division and in O(n)
'''
# class Solution:
#     def productExceptSelf(self, nums):
#         sz = len(nums)
#         up, down, output = sz*[1], sz*[1], sz*[1]
#         for i in range(1, sz):
#             up[i] = up[i-1]*nums[i-1]
#         for i in range(sz-2,-1,-1):
#             # tr *= nums[i+1]
#             down[i] = down[i+1]*nums[i+1]
#         for i in range(sz):
#             output[i] = up[i]*down[i]
#         return output
#     def pes_space(self, nums):
#         # Only allowed to use memory for output array
#         sz = len(nums)
#         output = sz*[1]
#         tr = 1
#         for i in range(1, sz):
#             tr *= nums[i-1]
#             output[i] *= tr
#         tr = 1
#         for i in range(sz-2,-1,-1):
#             tr *= nums[i+1]
#             output[i] *= tr
#         return output




'''
Second time doing this problem - November 2021
'''

class Solution:
    def productExceptSelf(self, nums):
        fwd, bwd = [1 for _ in range(len(nums))], [1 for _ in range(len(nums))]
        # go forward and build multiples, starting at idx 1. Write to previous index
        for i in range(1, len(nums)):
            fwd[i] = nums[i-1]*fwd[i-1]
        # backwards
        for i in reversed(range(0, len(nums)-1)):
            bwd[i] = nums[i+1]*bwd[i+1]
        
        return [fwd[i]*bwd[i] for i in range(len(nums))]


if __name__ == "__main__":
    sol = Solution()
    nums = [0,1]
    print(sol.productExceptSelf(nums))