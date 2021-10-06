'''
Problem 442 (medium): https://leetcode.com/problems/find-all-duplicates-in-an-array/

'''

# This solution uses extra space (the "seen" set), so it's not what we want.
class Solution_set:
    def findDuplicates(self, nums):
        duplicates = []
        seen = set()
        for num in nums:
            if num in seen:
                duplicates.append(num)
            else:
                seen.add(num)
        return duplicates

# Another solution it to sort the input in place (using no extra memory)
# Once sorted, a duplicate element will be the same as the previous element in the array
class Solution_sort:
    def findDuplicates(self, nums):
        nums.sort()
        duplicates = []
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                duplicates.append(nums[i])
        return duplicates

'''
An even cooler solution - good idea to keep in my back pocket going forward.
It's a really cool problem if you take advantage of all the properties of the input.

We know that the values of the array are between 1 and the length of the array, and there are at most 2 of any number, never 3.
That means we can use each number as an index to refer to another location in the array and modify that location. If the location is in its modified form
    then we know we've seen the number (the number that led the the location) already.
The trick is, you still need the actual value at the location to check if it is a duplicate, so you need to modify in a way that doesn't lose the original information.

Solution: for each number in the array follow it to its index - 1. At that location, make the number negative (preserving its value but flagging that a number has led to this index).
If a future number leads to index with a negative entry, then you know the entry has been visited already so add the leading number to your duplicate array!

The idea of flagging visits is cool. I think I can use that again someday.
'''
class Solution:
    def findDuplicates(self, nums):
        duplicates = []
        for n in nums:
            val = abs(n)
            if nums[val-1] < 0:
                duplicates.append(val)
            else:
                nums[val-1] *= -1
        return duplicates


if __name__ == "__main__":
    nums = [4,3,2,7,8,2,3,1]
    sol = Solution()
    print(sol.findDuplicates(nums))