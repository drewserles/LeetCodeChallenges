class Solution:
    def minStartValue(self, nums) -> int:
        min_start, run_sum = 1, 1
        for n in nums:
            run_sum += n
            # If we've dipped below 1, increase the min_start value to get the sum back to 1 at this point
            if run_sum < 1:
                diff = 1 - run_sum #e.g. if we dip down to -3, we need +4 to get back to positive on this step
                min_start += diff
                run_sum = 1
        return min_start


if __name__ == "__main__":
    sol = Solution()
    nums = [-1,-2,-3]
    print(sol.minStartValue(nums))