# Problem: Minimum Cost to Fill Given Weight 
# Difficulty: Medium 
# Date: 15 June 2026

"""
Problem:
Given costs of orange packets where cost[i]
represents the cost of a packet of weight (i+1) kg,
find the minimum cost to buy exactly W kg oranges.

cost[i] = -1 means that packet is unavailable. 
"""

# --------------------------------------------------- 
# Approach: Unbounded Knapsack (1D DP) 
# Time Complexity: O(N * W) 
# Space Complexity: O(W) 
# ---------------------------------------------------

class Solution:
    def minimumCost(self, cost, w):
        # code here
        INF = float('inf')
        dp = [INF] * (w + 1)
        dp[0] = 0
        n = len(cost)
        for i in range(1, w + 1):
            for j in range(n):
                wt = j + 1
                if cost[j] != -1 and wt <= i:
                    dp[i] = min(dp[i], dp[i - wt] + cost[j])
        return dp[w] if dp[w] != INF else -1
