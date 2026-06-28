# Problem: Ways to Tile the Floor 
# Difficulty: Medium 
# Date: 27 June 2026

""" 
Problem:
Count the number of ways to tile an n × m floor
using 1 × m tiles.

Tiles can be placed:
1. Horizontally (1 × m)
2. Vertically (m × 1)

Return the answer modulo 10^9 + 7.
"""

# --------------------------------------------------- 
# Approach: Dynamic Programming 
# Time Complexity: O(N) 
# Space Complexity: O(N) 
# ---------------------------------------------------

class Solution:
	def countWays(self, n, m):
		# Code here
		MOD = 10**9 + 7
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            if i < m:
                dp[i] = 1
            elif i == m:
                dp[i] = 2
            else:
                dp[i] = (dp[i - 1] + dp[i - m]) % MOD
        return dp[n]
