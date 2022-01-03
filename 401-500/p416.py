'''
Brute force solution is 2^n - each element is either in or out (in one partition or the other). You'd have to test every possibility

'''
import functools
class Solution:
    # 2^n solution. Too slow, but interesting idea on how to create permutations and flag
    def canPartition_2n(self, nums):
        res = [[]]
        for _ in nums:
            res = [x + [0] for x in res] + [x + [1] for x in res]
        
        for perm in res:
            left, right = 0, 0
            for idx in range(len(perm)):
                if perm[idx] == 0:
                    left += nums[idx]
                else:
                    right += nums[idx]

            if left == right:
                return True
        return False
    '''
    DFS with backtracking. Got help from comments on this one
    How does the @cache work? This takes it from a solution that runs over the timelimit to something that works
        -Stores previous results of the function with certain parameters, so when it's called again with the same params the result isn't recalculated
    '''
    def canPartition_dfs(self, nums):
        if sum(nums) % 2:
            return False
        targ = sum(nums) // 2
        l = len(nums)

        # @cache
        def dfs(cur_sum, idx):
            print(f'dfs. Current Sum: {cur_sum}, Array Idx: {idx}')
            # At the end of the line
            if idx == l:
                return cur_sum == targ
            # This value gets us to target
            elif cur_sum + nums[idx] == targ:
                return True
            # Recursively try indcluding this node in the sum
            elif cur_sum + nums[idx] < targ and dfs(cur_sum + nums[idx], idx+1):
                return True
            # Otherwise recursively try excluding this node
            else:
                return dfs(cur_sum, idx+1)

        return dfs(0, 0)

    '''
    Memoization approach ?
    To Do
    '''
    def canPartition(self, nums):
        if sum(nums) % 2:
            return False
        targ = sum(nums) // 2
        l = len(nums)

        





if __name__ == "__main__":
    sol = Solution()
    nums = [5,6,1,2]
    print(sol.canPartition(nums))