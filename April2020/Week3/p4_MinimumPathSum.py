class Solution:
    def minPathSum(self, grid) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i==0 and j ==0:
                    continue
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                elif i == 0:
                    grid[i][j] += grid[i][j-1]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]



if __name__ == "__main__":
    sol = Solution()
    grid = [[1,3,1],
            [1,5,1],
            [4,2,1]]
    print(sol.minPathSum(grid))