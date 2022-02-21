'''
>Majority element is greater than half, not >= half.
-Straightforward to count the number of each element then return the max. Still in O(n),
but it doesn't take advantage of the fact that we're looking for a majority element - 
it would be the same solution for a most common element problem.
-Can't sort because that immediately takes us to O(n*logn) time.

I came up with something that had early stopping at least when majority is hit. There are
some interesting algorithms in the solution file but nothing more broadly relevant.
'''

class Solution:
    def majorityElement(self, nums):
        num_dict = {}
        maj_len = len(nums)//2
        for num in nums:
            if num not in num_dict:
                num_dict[num] = 1
                val = num
            elif num_dict[num] == maj_len:
                return num
            else:
                num_dict[num] += 1
        return val


if __name__ == "__main__":
    sol = Solution()
    nums = [3,2,3]
    print(sol.majorityElement(nums))