# Problem: 1s Surrounded by 0s
# Difficulty: Medium
# Date: 22 May 2026

""" Problem:
Given a binary matrix, count all cells containing 1
that cannot move out of the grid through adjacent 1s.
Movement is allowed only in four directions:
Up, Down, Left, and Right.
"""

class Solution:
    def cntOnes(self, grid):
        # code here
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return
            if grid[i][j] == 0:
                return
            grid[i][j] = 0
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        for i in range(n):
            if grid[i][0] == 1:
                dfs(i, 0)
            if grid[i][m - 1] == 1:
                dfs(i, m - 1)
        for j in range(m):
            if grid[0][j] == 1:
                dfs(0, j)
            if grid[n - 1][j] == 1:
                dfs(n - 1, j)
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
        return count
