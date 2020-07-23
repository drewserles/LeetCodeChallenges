class Solution:    
    def search_recurse(self, nums, target, low_idx, high_idx):
        c = (high_idx + low_idx) // 2
        # Found the number
        if nums[c] == target:
            return c
        # Size of 1
        if high_idx <= low_idx:
            return -1

        # This half is sorted.
        if nums[low_idx] < nums[c]:
            # Check if the target is in range of the sorted half
            if target >= nums[low_idx] and target <= nums[c]:
                return self.search_recurse(nums, target, low_idx, c-1)
            # Otherwise it should be in the unsorted half
            else:
                return self.search_recurse(nums, target, c+1, high_idx)
        # The other half is sorted
        else:
            if target >= nums[c+1] and target <= nums[high_idx]:
                return self.search_recurse(nums, target, c+1, high_idx)
            # Otherwise it should be in the unsorted half
            else:
                return self.search_recurse(nums, target, low_idx, c-1)


    def search(self, nums, target) -> int:
        if len(nums) == 0:
            return -1
        return self.search_recurse(nums, target, 0, len(nums)-1)

if __name__ == "__main__":
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(sol.search(nums, target))