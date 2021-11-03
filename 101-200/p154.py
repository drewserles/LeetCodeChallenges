'''
Same as 153, but duplicates are allowed.
The cause of the issue is that the lowest could be sandwiched on either side of your divide.
E.g.
[3,3,3,1,3] and [3,1,3,3,3] are both valid.
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
        elif array[mid_idx] < array[end_idx]:
            return self.search_helper(array, start_idx, mid_idx)
        # If they're tied we need to do some fanciness
        else:
            if array[start_idx] == array[mid_idx]:
                return self.search_helper(array, start_idx+1, end_idx)
            else:
                return self.search_helper(array, start_idx, mid_idx)

        
    def findMin(self, nums):
        return self.search_helper(nums, 0, len(nums)-1)

if __name__ == "__main__":
    nums = [1,1,1,3]
    sol = Solution()
    print(sol.findMin(nums))