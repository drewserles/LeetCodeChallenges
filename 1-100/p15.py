from bisect import bisect_left
class Solution:
    '''
    Sort the list.
    Fix a value by iterating through nums, then fix another value by iterating through the remainder of the list. You don't need to look backwards because it's sorted

    >used the bisect library for the first time here to do a binary search

    This could be improved further with a pointer method so that we don't need to do a binary search each time. Try it
    '''
    def threeSum_v1(self, nums):
        nums.sort()
        sz = len(nums)
        res = set()
        for i in range(sz-2):
            v = 0 - nums[i]
            for j in range(i+1, sz-1):
                targ = v - nums[j]
                idx = bisect_left(nums, targ, j+1)
                if idx < len(nums) and nums[idx] == targ:
                    res.add( (nums[i], nums[j], targ) )
        return [list(x) for x in res]

    
    '''
    Second attempt using 3 indices.
    '''
    def threeSum(self, nums):
        nums.sort()
        res = []

        # first index - go start to finish
        for fi in range(len(nums) - 2):
            # If this number's the same as the previous index then skip since we want unique values
            if fi > 0 and nums[fi] == nums[fi-1]:
                continue

            # 2 more pointers - one starting just after fi, one at the end of the array
            si, ti = fi+1, len(nums)-1
            while si < ti:
                sum_val = nums[fi] + nums[si] + nums[ti]
                # If the sum is too big (>0)
                # OR If the third pointer value is the same as previous
                # move it down because we don't want duplicates
                # >I believe we should be able to take care of duplicates doing this and never having to check the second pointer. Confirm for myself
                # >yes because I'm moving both pointers in the match condition, so if we have duplicate matches then it will get picked up here
                if sum_val > 0 or ( ti < len(nums)-1 and nums[ti] == nums[ti+1]):
                    ti -= 1
                # too small then move up second index
                elif sum_val < 0:
                    si += 1
                # Match
                else:
                    res.append([nums[fi], nums[si], nums[ti]])
                    si += 1
                    ti -= 1
        return res


if __name__ == "__main__":
    sol = Solution()
    nums = [3,-1,-2]
    print(sol.threeSum(nums))