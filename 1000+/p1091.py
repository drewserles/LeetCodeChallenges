'''
Return the shortest path that can be achieved with conditions. I can frame this as a BFS problem.
-Can only move to 0 squares, can move to 8 adjacent squares.

BFS strategy: queue up nodes(grid squares) to be explored next. For each square, we:
    -Look at all 8 adjacent squares. Check if it's the final square (bottom right corner), if yes return its distance from start
    -Otherwise, if they meet the requirement of being i) 0 value and (ii) not already seen, then add them to the queue
    -Record a path length value with each entry. The key here is we don't care how we got to a node
        >we'll get to a node in the shortest time by definition of BFS. Then we see where we can explore from there
        >The worry that e.g. the path to finish involves a previous node that has already been visited isn't valid because that other path will be found
        by exploring from the previous node directly.
'''


class Solution:
    def shortestPathBinaryMatrix(self, grid) -> int:
        n = len(grid)-1
        queue = []
        seen = set()
        if grid[0][0] == 0:
            queue.append((0, 0, 1))
            seen.add((0,0))
        while len(queue) > 0:
            node = queue.pop(0)
            if node[0] == n and node[1] == n:
                return node[2]
            for r in [-1, 0, 1]:
                for c in [-1, 0, 1]:
                    row = node[0] + r
                    col = node[1] + c
                    # explore it
                    if 0 <= row <= n and 0 <= col <= n and (row,col) not in seen and grid[row][col] == 0:
                        queue.append((row, col, node[2]+1))
                        seen.add((row,col))

        return -1



if __name__ == "__main__":
    sol = Solution()
    grid = [[1,0,0],[1,1,0],[1,1,0]]
    print(sol.shortestPathBinaryMatrix(grid))