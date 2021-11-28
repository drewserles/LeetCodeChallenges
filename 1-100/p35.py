'''
Wrote this recursively, could also write it iteratively. That would be a good exercise

Cleanup: exit condition is when L > R, otherwise it's still viable
'''

class Solution:
    def bin_search(self, nums, target, start_idx, end_idx):
        if start_idx > end_idx:
            return start_idx
        
        mid_idx = (start_idx + end_idx) // 2
        val = nums[mid_idx]

        # Found value
        if val == target:
            return mid_idx
        # midpoint value is larger than target -> search smaller (below) portion of array
        elif val > target:
            return self.bin_search(nums, target, start_idx, mid_idx - 1)
        # value is smaller than target -> search bigger half
        else:
            return self.bin_search(nums, target, mid_idx + 1, end_idx)

    def searchInsert(self, nums, target):
        return self.bin_search(nums, target, 0, len(nums)-1)


if __name__ == "__main__":
    sol = Solution()
    nums = [1,3,5]
    target = -1
    print(sol.searchInsert(nums, target))