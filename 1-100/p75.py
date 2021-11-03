'''
Do this with heap sort. 
1. Max heapify the input array (max heap property: each element is larger than its two children)
2. heap sort the array with the heap property

This is a general sorting solution in place. But we could also take advantage of the input being 0/1/2 and use a two pointer solution.
This is called the Dutch national flag problem: https://en.wikipedia.org/wiki/Dutch_national_flag_problem
'''

class Solution:
    # Max heap property. between start and end idx, bubble it down (in place)
    def bubbleDown(self, nums, root, end):
        # while there's at least one child in the array continue - could do this recursively as well
        while root <= (end-1)//2:
            swap = root
            # Left and right child are 2i, 2i+1 in array
            lc = 2*root+1
            rc = lc + 1
            if nums[lc] > nums[swap]:
                swap = lc
            if rc <= end and nums[rc] > nums[swap]:
                swap = rc
            if swap == root:
                break
            else:
                nums[root], nums[swap] = nums[swap], nums[root]
                root = swap

    # Put elements of nums into max heap, in place -> start at the end and work forwards
    def createMaxHeap(self, nums):
        start_idx = len(nums) // 2 - 1 # Want to start on the second to last row of the tree. Final row doesn't need heapifying
        end_idx = len(nums) - 1
        for i in range(start_idx, -1, -1):
            self.bubbleDown(nums, i, end_idx)

    # Heapsort step. Take an array with heap property and sort into ascending order
    def heapSort(self, nums):
        self.createMaxHeap(nums)
        i = len(nums)-1
        while i > 0:
            nums[0], nums[i] = nums[i], nums[0]
            i -= 1
            self.bubbleDown(nums, 0, i)

    def sortColors(self, nums):
        self.heapSort(nums)

    def sortColors2(self, nums):
        # i is non-1 position, k is non-2 position, j is traverser
        i, j, k = 0, 0, len(nums)-1
        while j <= k:
            # if it's a 0 swap it into place. Increment both - there will be no 0s between i and j to worry about, since
            # j has already considered them. We know a 0 is swapped in and any elemetns between i and j are 1s
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            # It's a 2. Swap it into the non-2 position. Key is we don't know what was swapped from k to j,
            # so need to consider it
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            # Otherwise it's a 1, just increment traverser
            else:
                j += 1




if __name__ == "__main__":
    # nums = [2,7,26,25,19,17,1,90,3,36]
    nums = [2,0,1]
    sol = Solution()
    # sol.sortColors(nums)
    sol.sortColors2(nums)
    print(nums)