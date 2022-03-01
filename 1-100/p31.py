'''
Cool problem, I felt good about figuring this one out. Involves in place sorting and a nice little algorithm.

Start thinking with smallest possible situation. One number can't be modified to create a next permutation
Two numbers can be modified if the second number is bigger than the first (swap them) but not if it's the other way around (already biggest number made of those 2 digits)
This applies to 3 numbers and onwards

The observation: if you move from right to left (end of array to start) and keep track of the max value, if you ever encounter a number that is less than your max
then you're able to make a bigger number with the ones you have there. Otherwise keep track of the max and keep moving.

How to make the next permutation when you know you have a group that's possible?
-Know that the number we stopped on needs to be involved in the move since if it was possible without this number we wouldn't have gotten this far
>Sort all numbers to the right of our stopping number
>Walk through those and find the smallest number that's bigger than the stopping number. Swap places 
>This gives the smalles number that's bigger than the current arrangement and only touches numbers up to swapping number (least significant digits).
'''

class Solution:
    def nextPermutation(self, nums) -> None:
        max = nums[-1]
        for i in reversed(range(len(nums)-1)):
            # if this number is bigger than max then need to keep going - array is still monotonically increasing
            if nums[i] >= max:
                max = nums[i]
            # Otherwise this index is less than the max. A next permutation is possible with the numbers visited so far
            else:
                # Sort the higher indices of the array
                nums[i+1:] = sorted(nums[i+1:])
                # Traverse that section and find the smalles number that's bigger than nums[i]. Swap them
                for j in range(i+1, len(nums)):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        return None


        # Array is fully descending. Next permutation is the ascending order
        nums.sort()
        


if __name__ == "__main__":
    sol = Solution()
    nums = [4,2,5,3,1]
    sol.nextPermutation(nums)
    print(nums)