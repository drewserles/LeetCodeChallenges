'''
v2 with obstacles
'''

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        # m is number of rows, n is number of columns
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid = [[abs(col-1) for col in row] for row in obstacleGrid]
        path_cnt = [1] + [0 for _ in range(m-1)]
        
        # Iterate once for each column - can't skip the first row/col because of the single square
        for c in range(n):
            for r in range(m):
                blocked = obstacleGrid[r][c]
                if r == 0:
                    path_sum = path_cnt[r]
                else:
                    path_sum = path_cnt[r] + path_cnt[r-1]
                path_cnt[r] = blocked*(path_sum)
        return path_cnt[-1]
            



if __name__ == "__main__":
    obstacleGrid = [[1,0,0],[0,1,0],[0,0,0]]

    sol = Solution()
    print(sol.uniquePathsWithObstacles(obstacleGrid))