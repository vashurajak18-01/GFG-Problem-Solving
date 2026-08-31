from typing import List

class Solution:
    def ratInMaze(self, maze: List[List[int]]) -> List[str]:
        # code here
        n = len(maze)
        ans = []
        vis = [[0 for _ in range(n)] for _ in range(n)]
        if maze[0][0] == 1:
            self.findPathHelper(0,0, maze, n, ans, "", vis)
        return ans

    def findPathHelper(self, i : int, j : int, a : List[List[int]], n : int, ans : List[str],move: str, vis: List[List[int]]):
        if i == n-1 and j == n-1:
            ans.append(move)
            return

        # ? Downward
        if i + 1 < n and not vis[i+1][j] and a[i+1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i+1, j, a, n, ans, move + "D", vis)
            vis[i][j] = 0

        # ? Left 
        if j - 1 >= 0  and not vis[i][j-1] and a[i][j-1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j-1, a, n, ans, move + "L", vis)
            vis[i][j] = 0

        # ? Right
        if j + 1 < n and not vis[i][j+1] and a[i][j+1] == 1:
            vis[i][j] = 1
            self.findPathHelper(i, j+1, a, n, ans, move + "R", vis)
            vis[i][j] = 0

        # ? Upward
        if i - 1 >= 0  and not vis[i-1][j] and a[i-1][j] == 1:
            vis[i][j] = 1
            self.findPathHelper(i-1, j, a, n, ans, move + "U", vis)
            vis[i][j] = 0
