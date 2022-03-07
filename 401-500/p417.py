class Solution:
    def pacificAtlantic(self, heights):
        num_rows = len(heights)
        num_cols = len(heights[0])
        # Get a set of all squares that can reach the atlantic coast
        atl = set()
        visited = set()
        queue = []
        
        for j in range(num_cols):
            v = (num_rows-1, j)
            queue.append(v)
            visited.add(v)
            atl.add(v)
        for i in range(num_rows-1):
            v = (i, num_cols-1)
            queue.append(v)
            visited.add(v)
            atl.add(v)

        while len(queue) > 0:
            square = queue.pop(0)
            for r,c in [(-1, 0), (1,0), (0,-1), (0,1)]:
                i = square[0] + r
                j = square[1] + c
                if (i >= 0 and i < num_rows) and (j >= 0 and j < num_cols) and (i,j) not in visited and heights[i][j] >= heights[square[0]][square[1]]:
                    queue.append((i,j))
                    visited.add((i,j))
                    atl.add((i,j))
        

        # Get a set of all squares that can reach the pacific
        pac = set()
        visited = set()
        queue = []
        for j in range(num_cols):
            v = (0, j)
            queue.append(v)
            visited.add(v)

        for i in range(1, num_rows):
            v = (i, 0)
            queue.append(v)
            visited.add(v)

        pac = visited
        while len(queue) > 0:
            square = queue.pop(0)
            for r,c in [(-1, 0), (1,0), (0,-1), (0,1)]:
                i = square[0] + r
                j = square[1] + c
                if (i >= 0 and i < num_rows) and (j >= 0 and j < num_cols) and (i,j) not in visited and heights[i][j] >= heights[square[0]][square[1]]:
                    queue.append((i,j))
                    visited.add((i,j))
                    pac.add((i,j))
        # Find overlap
        return [list(x) for x in atl.intersection(pac)]



if __name__ == "__main__":
    sol = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    print(sol.pacificAtlantic(heights))