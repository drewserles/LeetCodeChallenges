'''
Description:
    -Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Constraints:
    -The length of the array is in range [1, 20,000].
    -The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
===
Observations:
    -Could I tackle this in a similar way to the binary subarray problem?
'''
class Solution:
    def subarraySum(self, nums, k) -> int:
        tot, found = 0, 0
        seen = {}
        for n in nums:
            tot += n
            # running total is equal to K
            if tot == k:
                found += 1
            # we can drop a previous total to get to K.
            # This is not an else, because previous places that summed to K should be included too
            diff = tot - k
            if diff in seen:
                found += seen[diff]
            # Keep track of the total
            if tot in seen:
                seen[tot] += 1
            else:
                seen[tot] = 1
        return found




if __name__ == "__main__":
    sol = Solution()
    nums = [1, -1, 2] # Answer: 2
    k = 2
    print(sol.subarraySum(nums, k))