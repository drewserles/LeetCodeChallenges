'''
Find start and end position in O(logn). That means we don't want to walk through it, we wan't to dive and conquer
Approach:
-Check the middle element of the array. If it's less than the target recursively search the top half, if it's more, search the bottom half
-Challenge is what to do when you find the target? We want the extremes of the range, so we need to figure out where this target falls
What about a 2 stage approach?
1. Look for an instance. If you don't find one at all that's when we return [-1,-1], if you do go into a separate function.
2. Function 2: divide and conquer but has a direction, meaning when you find a value you look to the right of it for the upper bound and to the left of it for the lower bound
    Combine these for a min and max position

This looks complex but it's actually a pretty great solution judging by the comment submissions. Nice one
'''

class Solution:
    def searchRange(self, nums, target):
        def div_search(start_idx, end_idx):
            if start_idx > end_idx:
                return -1
            mid_idx = (end_idx + start_idx) // 2
            mid_val = nums[mid_idx]
            if mid_val == target:
                return [start_idx, mid_idx, end_idx]
            elif mid_val < target:
                return div_search(mid_idx+1, end_idx)
            else:
                return div_search(start_idx, mid_idx-1)

        def dir_search(fnd_idx, start_idx, end_idx, dir):
            if start_idx > end_idx:
                return fnd_idx
            mid_idx = (end_idx + start_idx) // 2
            mid_val = nums[mid_idx]
            if mid_val == target:
                # Searching up
                if dir == 1:
                    return dir_search(mid_idx, mid_idx+1, end_idx, dir)
                # searching down
                elif dir== -1:
                    return dir_search(mid_idx, start_idx, mid_idx-1, dir)

            elif mid_val < target:
                return dir_search(fnd_idx, mid_idx+1, end_idx, dir)
            else:
                return dir_search(fnd_idx, start_idx, mid_idx-1, dir)
        
        loc = div_search(0, len(nums)-1)

        if loc == -1:
            return [-1,-1]
        else:
            mid = loc[1]
            low = dir_search(-1, loc[0], mid-1, -1)
            high = dir_search(-1, mid+1, loc[2], 1)
            if low == -1:
                low = mid
            if high == -1:
                high = mid
            return [low, high]


if __name__ == "__main__":
    sol = Solution()
    nums = []
    target = 0
    print(sol.searchRange(nums, target))