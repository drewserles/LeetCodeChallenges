'''
Cool, this runs comparatively quickly!
General idea: each number in num can be either in or out in the power set, giving 2^N possibilities.
One way to do this would be to iterate from 0 to 2^N-1, and use the number's bit values to decide if the corresponding array position number is in or out of the result.
This steps from all numbers out at 0 (empty set) to all numbers in at 2^N-1 (whole set) and hits every combination in between

There are two other interesting ideas from the solution.
1. Cascade: start with the empty set and consider each number in nums one at a time. Add that value to each of the existing lists in the result set
2. Backtracking i.e. DFS: 
'''


class Solution:
    def subsets(self, nums):
        res = []
        for i in range(2**len(nums)):
            vals = []
            pos = 0

            while i > 0:
                if i & 1:
                    vals.append(nums[pos])
                pos += 1
                i >>= 1
            res.append(vals)
        return res

    def subsets_cascade(self, nums):
        res = [[]]
        for num in nums:
            res += [curr + [num] for curr in res]
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,1,4]
    print(sol.subsets_cascade(nums))