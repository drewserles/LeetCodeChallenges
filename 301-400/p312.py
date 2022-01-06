'''
I can frame this as a dynamic programming problem working from the ground up, meaning from a single balloon left, up to pairs of balloons etc.

Recall that balloons can be broken in any order.
At each level I'll have to store all possible orderings, e.g. for 3 balloons at the 2 level I'd have 2+1=3 possible orderings (12, 13, 23)
I could probably store in a dictionary with tuples as the keys and values as the max sum.

It also might be easiest to store the *values* rather than the indices, because there could be a lot of overlap. The only challenge here is constructing the next layer up

The order matters at each step because it affects the numerical outcome. Also the balloon combos *must* be in increasing index order. You can have balloons in between removed
in previous pops but can't increase the order


Create a function that takes in a value and finds the biggest possible value from here by popping one balloon. Need the dynamic programming levels below this one.

Why is it so much faster to go from bottom up rather than top down? This is an interesting question I need to think about some more. It's a divide and conquer problem
This solution is really interesting: https://leetcode.com/problems/burst-balloons/discuss/1659527/C%2B%2BPythonJava-2-Simple-Solutions-oror-DP-and-Recursion-oror-Detailed-Explanation 
'''
class Solution:
    # This DFS is too slow even with caching. Note need to pass an immutable to cache
    # Going to need to try a dynamic programming approach
    # Memoization with recursion. I had the right idea to go from bottom up.
    def maxCoins(self, nums) -> int:
        N = 5
        for left in range(N - 2, -1, -1):
            for right in range(left + 2, N):
                print(left,right)

if __name__ == "__main__":
    sol = Solution()
    # nums = [35,16,83,87,84,59,48,41,20,54]
    nums = [3,1,5,8]
    print(sol.maxCoins(nums))


# def maxCoins(self, nums) -> int:
#     @cache
#     def coins(nums):
#         l = len(nums)
#         maxm = 0
#         for b in range(l):
#             if b == 0:
#                 low = 1
#             else:
#                 low = nums[b-1]
#             if b >= l-1:
#                 high = 1
#             else:
#                 high = nums[b+1]
#             val = low * nums[b] * high + self.maxCoins(nums[:b] + nums[b+1:])
#             if val > maxm:
#                 maxm = val
#         return maxm
#     return coins(tuple(nums))