# Problem: Rat Maze With Multiple Jumps 
# Difficulty: Medium 
# Date: 24 June 2026

""" 
Problem: 
Find a path for the rat from (0,0) to (n-1,n-1).
The rat can jump from 1 to mat[i][j] cells either:
- Right 
- Down 
Choose smaller jumps first, and for the same jump
length prefer right over down. 
"""

# --------------------------------------------------- 
# Approach: DFS + Memoization 
# Time Complexity: O(N² × maxJump) 
# Space Complexity: O(N²) 
# ---------------------------------------------------

class Solution:
	def shortestDist(self, mat):
		# code here
        n = len(mat)
        if mat[0][0] == 0:
            return [[-1]]
        ans = [[0] * n for _ in range(n)]
        dp = [[-1] * n for _ in range(n)]
        def dfs(i, j):
            if i >= n or j >= n or mat[i][j] == 0:
                return False
            if i == n - 1 and j == n - 1:
                ans[i][j] = 1
                return True
            if dp[i][j] != -1:
                return dp[i][j] == 1
            ans[i][j] = 1
            for jump in range(1, mat[i][j] + 1):
                if dfs(i, j + jump):
                    dp[i][j] = 1
                    return True
                if dfs(i + jump, j):
                    dp[i][j] = 1
                    return True
            ans[i][j] = 0
            dp[i][j] = 0
            return False
        if dfs(0, 0):
            return ans
        return [[-1]]
