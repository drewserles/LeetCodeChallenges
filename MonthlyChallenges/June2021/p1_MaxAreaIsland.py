'''
Medium: https://leetcode.com/problems/max-area-of-island/

Solution inspired by DFS. You can think of each square in the grid where there's land (1s) as a node,
and viable connections only go in the L, R, U, D directions.
Then from a node you can explore all connection recursively, marking each when visited. When you get to
a dead end (no further adjacent 1s to explore) then you've fully explored an island so return its size.
Track the biggest island found so far and return it at the end.
'''

# Input: list of list of [0,1]
# Return: Int, size of largest island
class Solution:
    def printGrid(self):
        for r in self.grid: print(r)
    
    def dfs(self, i, j):
        if (0 <= i < self.m) and (0 <= j < self.n) and self.grid[i][j] == 1:
            # Mark that it has been visited
            self.grid[i][j] = 2
            # Recurse on its 4 touching sides
            return 1 + self.dfs(i-1, j) + self.dfs(i+1, j) + self.dfs(i, j-1) + self.dfs(i, j+1)
        else:
            return 0
    
    def maxAreaOfIsland(self, grid):
        self.grid = grid
        self.m, self.n = len(self.grid), len(self.grid[0])
        
        # self.printGrid()
        
        biggest = 0
        for i in range(self.m):
            for j in range(self.n):
                biggest = max(biggest, self.dfs(i, j))
        
        return biggest


if __name__ == "__main__":
    input = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
            [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
    sol = Solution()
    print(f'Largest Island Found: {sol.maxAreaOfIsland(input)}')