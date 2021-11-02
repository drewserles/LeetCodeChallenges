'''
I remember doing this problem back in ~2016 on Project Euler and having the insight that the number of paths
to square X is the sum of the paths to the two squares that can reach X (one left, one up). That was a cool breakthrough.

Nice variation in my solution here is you don't need to keep track of a whole grid, just one column's worth. Then you can
update the value at each index of the column with the value at index-1. This represents the square to the left summed with the square above.
'''

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # m is number of rows, n is number of columns
        path_cnt = [1 for _ in range(m)]
        
        # Iterate once for each column
        for _ in range(1, n):
            # go down the rows, ignoring the top row since it's always 1. Update the values to sum the square 
            # above and to the left
            for r in range(1, m):
                path_cnt[r] += path_cnt[r-1]
        return path_cnt[-1]
            



if __name__ == "__main__":
    m = 3
    n = 7

    sol = Solution()
    print(sol.uniquePaths(m, n))