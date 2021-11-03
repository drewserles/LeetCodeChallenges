'''
Problem 463 (easy): https://leetcode.com/problems/island-perimeter/

Move left to right through the grid.
Assume every land square has a perimeter of 4 and add it to the total. Then check to the left and above if that square was land too. If it is,
remove 2 from the perimeter total.

Interestingly, it looks like I did this problem in August 2018 and used the same method. That's kind of neat to have the record.
'''
class Solution:
    def  islandPerimeter(self, grid):
        rows, cols = len(grid), len(grid[0])
        perimeter = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2
        return perimeter


if __name__ == "__main__":
    grid = [[1, 0]]
    sol = Solution()
    print(sol.islandPerimeter(grid))