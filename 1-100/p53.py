class Solution:
    def maxSubArray(self, nums) -> int:
        max_sum = nums[0]
        curr_sum = 0
        # Iterate through array and
        # -If a number is positive, add it to the current sum and if the sum is biggest yet record it
        # -If a number is negative and the total is <0 then start fresh. If not continue
        #   >This is for the case where there's a negative number sandwiched by bigger positive numbers
        for n in nums:
            curr_sum += n
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum


if __name__ == "__main__":
    sol = Solution()
    # T1
    inp = [-2,1,-3,4,-1,2,1,-5,4]
    exp = 6
    res = sol.maxSubArray(inp)
    print(f'Test 1 - Expected: {exp}, result: {res}')
    # T2
    inp = [-1, -2, -3, 0, -4]
    exp = 0
    res = sol.maxSubArray(inp)
    print(f'Test 1 - Expected: {exp}, result: {res}')