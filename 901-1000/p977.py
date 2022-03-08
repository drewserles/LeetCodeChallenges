'''
Obviously you could just square the values of the array and sort it, like 
for i in range(len(nums)):
    nums[i] = nums[i]**2
return sorted(nums)
But the point here is to do your own sorting and take advantage of the input properties.
-Since we're squaring the elements, the smallest value in the result is the one closest to 0
-There's a two-pointer approach where we start outside and work in
'''

class Solution:
    def sortedSquares(self, nums):
        res = [0]*len(nums)
        i,j = 0, len(nums)-1
        for p in reversed(range(len(res))):
            if abs(nums[i]) >= abs(nums[j]):
                res[p] = nums[i]**2
                i += 1
            else:
                res[p] = nums[j]**2
                j -= 1
        return res

if __name__ == "__main__":
    sol = Solution()
    nums = [-7,-3,2,3,11]
    print(sol.sortedSquares(nums))