class Solution:
    

    def cherryPickup_0(self, grid):
        self.sz = len(grid)-1
        fnd = []
        res = set([0])
        def dfs_down_walk(grid, row_idx, col_idx, cherries):
            # Can go down or right from here
            if grid[row_idx][col_idx] == 1:
                cherries += 1
                grid = [x[:] for x in grid]
                grid[row_idx][col_idx] = 0
            elif grid[row_idx][col_idx] == -1:
                return
            # print(f'Row: {row_idx}, col: {col_idx}, cherries: {cherries}, board: {grid}')

            if row_idx == self.sz and col_idx == self.sz:
                fnd.append([cherries, grid])
            # Try going down
            if row_idx < self.sz:
                dfs_down_walk(grid, row_idx+1, col_idx, cherries)
            # Try going right
            if col_idx < self.sz:
                dfs_down_walk(grid, row_idx, col_idx+1, cherries)

        def dfs_up_walk(grid, row_idx, col_idx, cherries):
            # Can go down or right from here
            if grid[row_idx][col_idx] == 1:
                cherries += 1
                grid = [x[:] for x in grid]
                grid[row_idx][col_idx] = 0
            elif grid[row_idx][col_idx] == -1:
                return
            # print(f'Row: {row_idx}, col: {col_idx}, cherries: {cherries}, board: {grid}')

            if row_idx == 0 and col_idx == 0:
                res.add(cherries)
            # Try going down
            if row_idx > 0:
                dfs_up_walk(grid, row_idx-1, col_idx, cherries)
            # Try going right
            if col_idx > 0:
                dfs_up_walk(grid, row_idx, col_idx-1, cherries)

        
        
        # GO down to end
        dfs_down_walk(grid, 0, 0, 0)
        
        # Come back up to top
        for board in fnd:
            dfs_up_walk(board[1], self.sz, self.sz, board[0])
        
        return max(res)

    '''
    Second attempt to make it faster.
    Ideas: -don't modify the board, just save a set of squares where cherries have been picked up
    -If a combination of position and cherries has already been seen then end it. The paths from there would have been explored
        in a previous DFS.
    -
    '''
    def cherryPickup(self, grid):

if __name__ == "__main__":
    grid = [[0,1,-1],[1,0,-1],[1,1,1]]
    # grid = [[1,1,-1],[1,-1,1],[-1,1,1]]

    sol = Solution()
    print(sol.cherryPickup(grid))