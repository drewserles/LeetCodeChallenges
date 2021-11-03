'''
Divide and conquer problem.
It asks for a solution in O(log n) so that's a strong hint to break it up into halves.

The key observation
'''

class Solution:
    def search_helper(self, array, start_idx, end_idx):
        # base case
        if start_idx == end_idx:
            return array[start_idx]
        # recursion
        mid_idx = (end_idx + start_idx) // 2
        # If the middle element is larger than the last, then the transition occurs between them
            # Search top half of the array
        if array[mid_idx] > array[end_idx]:
            return self.search_helper(array, mid_idx+1, end_idx)
        # Otherwise the min element is contained in the lower half (including the middle)
        else:
            return self.search_helper(array, start_idx, mid_idx)

        
    def findMin(self, nums):
        return self.search_helper(nums, 0, len(nums)-1)

if __name__ == "__main__":
    nums = [11,13,15,-11]
    sol = Solution()
    print(sol.findMin(nums))