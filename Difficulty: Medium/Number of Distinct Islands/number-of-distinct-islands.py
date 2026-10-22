import sys

sys.setrecursionlimit(10**8)

class Solution:
    def dfs(self, r, c, base_r, base_c, shape,
            visited, rows, cols, grid):

        visited[r][c] = 1

        shape.append((r - base_r, c - base_c))

        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        for x, y in directions:
            new_i = r + x
            new_j = c + y

            if (new_i < 0 or new_j < 0 or
                new_i >= rows or new_j >= cols):
                continue

            if grid[new_i][new_j] == "W":
                continue

            if visited[new_i][new_j] == 1:
                continue

            self.dfs(
                new_i, new_j, base_r, base_c,
                shape, visited, rows, cols, grid
            )

    def countDistinctIslands(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        unique_islands = set()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "L" and visited[r][c] == 0:
                    shape = []

                    self.dfs(
                        r, c, r, c, shape,
                        visited, rows, cols, grid
                    )

                    unique_islands.add(tuple(shape))

        return len(unique_islands)