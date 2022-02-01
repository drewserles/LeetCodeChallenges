'''
At least 3 ways to do this
'''

class Solution:
    # Approach 1: slice out section to move, reform array with it at the front
    def rotate_1(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

    # Approach 2: store section to move. Shift everything else to fill end of array.
    # Fill in the first part of the array with the move section
    def rotate_2(self, nums, k):
        k = k % len(nums)
        rot_sect = nums[-k:]
        # Shift non-rotate section to the end
        for i in reversed(range(len(nums)-k)):
            nums[i+k] = nums[i]
        for i in range(len(rot_sect)):
            nums[i] = rot_sect[i]

    # Approach 3: in place (no extra memory)
    # Strategy: reverse the whole list, then reverse the first k section then the second k section.
    # [1,2,3,4,5,6,7], k = 3 -> [7,6,5,4,3,2,1] -> [5,6,7,    1,2,3,4]
    def rotate_3(self, nums, k):
        k %= len(nums)
        L = len(nums)
        nums.reverse()
        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for i in range((L-k)//2):
            nums[i+k], nums[L-1-i] = nums[L-1-i], nums[i+k]

    # *not finished* Approach 3: Can I do it in place with constant extra space?
    # You could definitely do it in an O(n^2) way by just rewriting each time. Is there a better option?
    # Cycling through and displacing - this gets complicated, need cycle periodicity
    def rotate(self, nums, k):
        k %= len(nums)
        arr_len = len(nums)
        # Iterate over the indices to move
        for i in range(arr_len-k, arr_len):
            curr_idx = i
            next_idx = (i + k) % arr_len
            val = nums[curr_idx]
            while next_idx < arr_len:
                nums[next_idx], val = val, nums[next_idx]
                next_idx += k


if __name__ == "__main__":
    sol = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    sol.rotate_3(nums, k)
    print(nums)