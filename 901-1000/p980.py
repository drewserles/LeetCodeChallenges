'''
Find the number of viable paths from start to end. Robot can now move in 4 directions but can't visit a square twice, and there are obstacles.

This was a nice challenge writing it as a DFS exploration that finds all valid paths. Result beats 98.4% for speed which is cool!

I'm curious to see what other people did, maybe there are simpler approaches.
'''

class Solution:
    def uniquePathsIII(self, grid) -> int:
        self.n, self.m = len(grid), len(grid[0])
        self.graph = {}
        self.start, self.end = None, None
        self.num_blocks, self.path_len = 0, 0
        self.flat = [c for r in grid for c in r]
        self.grid_size = len(self.flat)

        # Build the Graph
        for idx in range(self.grid_size):
            # 4 possible moves from here
            l, r = idx - 1, idx + 1
            u, d = idx - self.m, idx + self.m
            val = []

            grid_val = self.flat[idx]
            if grid_val == 1:
                self.start = idx
            elif grid_val == 2:
                self.end = idx

            # If it is a dead end then have it going nowhere (empty val []) and count it
            if grid_val == -1:
                self.num_blocks += 1
            # If this isn't a dead end then build the graph. 
            else:
                if u >= 0:
                    val.append(u)
                if d < self.grid_size:
                    val.append(d)
                row_num = idx // self.m
                if l >= 0 and (l // self.m) == row_num:
                    val.append(l)
                if r < self.grid_size and (r // self.m) == row_num:
                    val.append(r)
            self.graph[idx] = val
        
        self.path_len = self.grid_size - self.num_blocks

        # Searching recursively
        visited = [0 for _ in range(self.grid_size)]
        return self.search(self.start, visited)

    def search(self, square, visited_squares):
        visited_squares = visited_squares[:]
        # Mark that we've visited this square
        visited_squares[square] = 1
        # print(visited_squares)
        # We've reached the end
        if square == self.end:
            # If we've visited every square return 1, otherwise return 0
            if sum(visited_squares) == self.path_len:
                return 1
            else:
                return 0
        # Otherwise continue on -> recursive step
        valid_paths = 0
        for next_square in self.graph[square]:
            if visited_squares[next_square] == 0:
                valid_paths += self.search(next_square, visited_squares)
        return valid_paths


if __name__ == "__main__":
    grid = [[0,1],[2,0]]

    sol = Solution()
    print(sol.uniquePathsIII(grid))